title: Flink DataStream API教程
date: 2019-07-08
tags: Flink

[TOC]

在本文中，我们将从头开始，介绍从设置Flink项目到在Flink集群上运行流分析程序。

Wikipedia提供了一个IRC频道，其中记录了对Wiki的所有编辑。我们将在Flink中读取此通道，并计算每个用户在给定时间窗口内编辑的字节数。这很容易使用Flink在几分钟内实现，但它将为您提供一个良好的基础，从而开始自己构建更复杂的分析程序。

## 设置Maven项目

我们将使用Flink Maven Archetype来创建我们的项目结构。有关此内容的更多详细信息，请参阅[Java API快速入门](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/projectsetup/java_api_quickstart.html)。出于我们的目的，运行命令是这样的：

```
$ mvn archetype:generate \
    -DarchetypeGroupId=org.apache.flink \
    -DarchetypeArtifactId=flink-quickstart-java \
    -DarchetypeVersion=1.8.0 \
    -DgroupId=wiki-edits \
    -DartifactId=wiki-edits \
    -Dversion=0.1 \
    -Dpackage=wikiedits \
    -DinteractiveMode=false
```

您可以编辑`groupId`，`artifactId`而`package`如果你喜欢。使用上面的参数，Maven将创建一个如下所示的项目结构：

```
$ tree wiki-edits
wiki-edits/
├── pom.xml
└── src
    └── main
        ├── java
        │   └── wikiedits
        │       ├── BatchJob.java
        │       └── StreamingJob.java
        └── resources
            └── log4j.properties
```

我们的`pom.xml`文件已经在根目录中添加了Flink依赖项，并且有几个示例Flink程序`src/main/java`。我们可以删除示例程序，因为我们将从头开始：

```
$ rm wiki-edits/src/main/java/wikiedits/*.java
```

作为最后一步，我们需要将Flink Wikipedia连接器添加为依赖关系，以便我们可以在我们的程序中使用它。编辑`dependencies`部分`pom.xml`，使其看起来像这样：

```
<dependencies>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-java</artifactId>
        <version>${flink.version}</version>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-streaming-java_2.11</artifactId>
        <version>${flink.version}</version>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-clients_2.11</artifactId>
        <version>${flink.version}</version>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-connector-wikiedits_2.11</artifactId>
        <version>${flink.version}</version>
    </dependency>
</dependencies>
```

注意添加的依赖项`flink-connector-wikiedits_2.11`。（此示例和Wikipedia连接器的灵感来自Apache Samza 的*Hello Samza*示例。）

## 写一个Flink程序

接下来是编码。启动您喜欢的IDE并导入Maven项目或打开文本编辑器并创建文件`src/main/java/wikiedits/WikipediaAnalysis.java`：

```java
package wikiedits;

public class WikipediaAnalysis {

    public static void main(String[] args) throws Exception {

    }
}
```

该计划现在非常基础，但我们会慢慢填充。请注意，我不会在此处提供import语句，因为IDE可以自动添加它们。在本节结束时，如果您只想跳过并在编辑器中输入，我将使用import语句显示完整的代码。

Flink程序的第一步是创建一个`StreamExecutionEnvironment` （或者`ExecutionEnvironment`，如果您正在编写批处理作业）。这可用于设置执行参数并创建从外部系统读取的源。所以让我们继续把它添加到main方法：

```
StreamExecutionEnvironment see = StreamExecutionEnvironment.getExecutionEnvironment();
```

接下来，我们将创建一个从Wikipedia IRC日志中读取的源：

```
DataStream<WikipediaEditEvent> edits = see.addSource(new WikipediaEditsSource());
```

这创建了一个我们可以进一步处理`DataStream`的`WikipediaEditEvent`元素。出于本示例的目的，我们感兴趣的是确定每个用户在特定时间窗口中添加或删除的字节数，比如说五秒。为此，我们首先要指定我们要在用户名上键入流，也就是说此流上的操作应考虑用户名。在我们的例子中，窗口中编辑的字节的总和应该是每个唯一的用户。对于键入流，我们必须提供一个`KeySelector`，如下所示：

```
KeyedStream<WikipediaEditEvent, String> keyedEdits = edits
    .keyBy(new KeySelector<WikipediaEditEvent, String>() {
        @Override
        public String getKey(WikipediaEditEvent event) {
            return event.getUser();
        }
    });
```

这为我们提供了一个`WikipediaEditEvent`具有`String`密钥的用户名。我们现在可以指定我们希望在此流上加上窗口，并根据这些窗口中的元素计算结果。窗口指定要在其上执行计算的Stream的切片。在无限的元素流上计算聚合时需要Windows。在我们的例子中，我们将说我们想要每五秒聚合一次编辑的字节总和：

```
DataStream<Tuple2<String, Long>> result = keyedEdits
    .timeWindow(Time.seconds(5))
    .fold(new Tuple2<>("", 0L), new FoldFunction<WikipediaEditEvent, Tuple2<String, Long>>() {
        @Override
        public Tuple2<String, Long> fold(Tuple2<String, Long> acc, WikipediaEditEvent event) {
            acc.f0 = event.getUser();
            acc.f1 += event.getByteDiff();
            return acc;
        }
    });
```

第一个调用，`.timeWindow()`指定我们希望有五秒钟的翻滚（非重叠）窗口。第二个调用为每个唯一键指定每个窗口切片的*折叠变换*。在我们的例子中，我们从一个初始值开始，`("", 0L)`并在该时间窗口中为用户添加每个编辑的字节差异。生成的Stream现在包含`Tuple2<String, Long>`每五秒钟发出一次的用户。

剩下要做的就是将流打印到控制台并开始执行：

```
result.print();

see.execute();
```

最后一次调用是启动实际Flink工作所必需的。所有操作（例如创建源，转换和接收器）仅构建内部操作的图形。只有在`execute()`被调用时 才会在集群上抛出或在本地计算机上执行此操作图。

到目前为止完整的代码是这样的：

```
package wikiedits;

import org.apache.flink.api.common.functions.FoldFunction;
import org.apache.flink.api.java.functions.KeySelector;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.KeyedStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.streaming.connectors.wikiedits.WikipediaEditEvent;
import org.apache.flink.streaming.connectors.wikiedits.WikipediaEditsSource;

public class WikipediaAnalysis {

  public static void main(String[] args) throws Exception {

    StreamExecutionEnvironment see = StreamExecutionEnvironment.getExecutionEnvironment();

    DataStream<WikipediaEditEvent> edits = see.addSource(new WikipediaEditsSource());

    KeyedStream<WikipediaEditEvent, String> keyedEdits = edits
      .keyBy(new KeySelector<WikipediaEditEvent, String>() {
        @Override
        public String getKey(WikipediaEditEvent event) {
          return event.getUser();
        }
      });

    DataStream<Tuple2<String, Long>> result = keyedEdits
      .timeWindow(Time.seconds(5))
      .fold(new Tuple2<>("", 0L), new FoldFunction<WikipediaEditEvent, Tuple2<String, Long>>() {
        @Override
        public Tuple2<String, Long> fold(Tuple2<String, Long> acc, WikipediaEditEvent event) {
          acc.f0 = event.getUser();
          acc.f1 += event.getByteDiff();
          return acc;
        }
      });

    result.print();

    see.execute();
  }
}
```

您可以使用Maven在IDE或命令行上运行此示例：

```
$ mvn clean package
$ mvn exec:java -Dexec.mainClass=wikiedits.WikipediaAnalysis
```

第一个命令构建我们的项目，第二个命令执行我们的主类。输出应该类似于：

```
1> (Fenix down,114)
6> (AnomieBOT,155)
8> (BD2412bot,-3690)
7> (IgnorantArmies,49)
3> (Ckh3111,69)
5> (Slade360,0)
7> (Narutolovehinata5,2195)
6> (Vuyisa2001,79)
4> (Ms Sarah Welch,269)
4> (KasparBot,-245)
```

每行前面的数字告诉您输出的打印接收器的哪个并行实例。

这应该让您开始编写自己的Flink程序。要了解更多信息，您可以查看我们的[基本概念](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/api_concepts.html)指南和 [DataStream API](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/datastream_api.html)。如果您想了解如何在自己的机器上设置Flink群集并将结果写入[Kafka](http://kafka.apache.org/)，请坚持参加奖励练习。

## 奖金练习：在群集上运行并写入Kafka

请按照我们的[本地安装教程](https://ci.apache.org/projects/flink/flink-docs-release-1.8/tutorials/local_setup.html)在您的计算机上设置Flink分发，并 在继续之前参考[Kafka快速入门](https://kafka.apache.org/0110/documentation.html#quickstart)以设置Kafka安装。

作为第一步，我们必须添加Flink Kafka连接器作为依赖关系，以便我们可以使用Kafka接收器。将其添加到`pom.xml`依赖项部分中的文件：

```
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-connector-kafka-0.11_2.11</artifactId>
    <version>${flink.version}</version>
</dependency>
```

接下来，我们需要修改我们的程序。我们将移除`print()`水槽，而是使用Kafka水槽。新代码如下所示：

```
result
    .map(new MapFunction<Tuple2<String,Long>, String>() {
        @Override
        public String map(Tuple2<String, Long> tuple) {
            return tuple.toString();
        }
    })
    .addSink(new FlinkKafkaProducer011<>("localhost:9092", "wiki-result", new SimpleStringSchema()));
```

还需要导入相关的类：

```
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaProducer011;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.api.common.functions.MapFunction;
```

注意我们是如何第一个转换的流`Tuple2<String, Long>`来流`String`使用MapFunction。我们这样做是因为将简单字符串写入Kafka更容易。然后，我们创建了一个卡夫卡水槽。您可能必须使主机名和端口适应您的设置。`"wiki-result"` 是在我们运行程序之前我们将要创建的Kafka流的名称。使用Maven构建项目，因为我们需要jar文件在集群上运行：

```
$ mvn clean package
```

生成的jar文件将位于`target`子文件夹中：`target/wiki-edits-0.1.jar`。我们稍后会用到它。

现在我们准备启动Flink集群并运行写入Kafka的程序。转到安装Flink的位置并启动本地群集：

```
$ cd my/flink/directory
$ bin/start-cluster.sh
```

我们还必须创建Kafka主题，以便我们的程序可以写入它：

```
$ cd my/kafka/directory
$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic wiki-results
```

现在我们准备在本地Flink集群上运行我们的jar文件：

```
$ cd my/flink/directory
$ bin/flink run -c wikiedits.WikipediaAnalysis path/to/wikiedits-0.1.jar
```

如果一切按计划进行，那么该命令的输出应该与此类似：

```
03/08/2016 15:09:27 Job execution switched to status RUNNING.
03/08/2016 15:09:27 Source: Custom Source(1/1) switched to SCHEDULED
03/08/2016 15:09:27 Source: Custom Source(1/1) switched to DEPLOYING
03/08/2016 15:09:27 TriggerWindow(TumblingProcessingTimeWindows(5000), FoldingStateDescriptor{name=window-contents, defaultValue=(,0), serializer=null}, ProcessingTimeTrigger(), WindowedStream.fold(WindowedStream.java:207)) -> Map -> Sink: Unnamed(1/1) switched to SCHEDULED
03/08/2016 15:09:27 TriggerWindow(TumblingProcessingTimeWindows(5000), FoldingStateDescriptor{name=window-contents, defaultValue=(,0), serializer=null}, ProcessingTimeTrigger(), WindowedStream.fold(WindowedStream.java:207)) -> Map -> Sink: Unnamed(1/1) switched to DEPLOYING
03/08/2016 15:09:27 TriggerWindow(TumblingProcessingTimeWindows(5000), FoldingStateDescriptor{name=window-contents, defaultValue=(,0), serializer=null}, ProcessingTimeTrigger(), WindowedStream.fold(WindowedStream.java:207)) -> Map -> Sink: Unnamed(1/1) switched to RUNNING
03/08/2016 15:09:27 Source: Custom Source(1/1) switched to RUNNING
```

您可以看到各个运营商如何开始运行。只有两个，因为窗口之后的操作由于性能原因而折叠成一个操作。在Flink，我们称之为*链接*。

您可以通过使用Kafka控制台使用者检查Kafka主题来观察程序的输出：

```
bin/kafka-console-consumer.sh  --zookeeper localhost:2181 --topic wiki-result
```

您还可以查看应在[http：// localhost：8081上](http://localhost:8081/)运行的Flink仪表板。您将获得群集资源和正在运行的作业的概述：

[![JobManager概述](https://ci.apache.org/projects/flink/flink-docs-release-1.8/page/img/quickstart-example/jobmanager-overview.png)](https://ci.apache.org/projects/flink/flink-docs-release-1.8/page/img/quickstart-example/jobmanager-overview.png)

如果单击正在运行的作业，您将获得一个视图，您可以在其中检查单个操作，例如，查看已处理元素的数量：

[![作业视图示例](https://ci.apache.org/projects/flink/flink-docs-release-1.8/page/img/quickstart-example/jobmanager-job.png)](https://ci.apache.org/projects/flink/flink-docs-release-1.8/page/img/quickstart-example/jobmanager-job.png)