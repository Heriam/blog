Title: Spark Streaming 编程手册翻译
Date: 2018-06-13
Tags: Spark, Programming

###**综述 **

Spark Streaming是Spark API核心的扩展，支持实时数据流的可扩展，高吞吐量，容错流处理。数据可以从像卡夫卡，水槽，室壁运动，或TCP套接字许多来源摄入，并且可以使用与像高级别功能表达复杂的算法来处理`map`，`reduce`，`join`和`window`。最后，处理后的数据可以推送到文件系统，数据库和实时仪表板。实际上，您可以将Spark的 [机器学习](https://spark.apache.org/docs/latest/ml-guide.html)和 [图形处理](https://spark.apache.org/docs/latest/graphx-programming-guide.html)算法应用于数据流。

![Spark Streaming](https://spark.apache.org/docs/latest/img/streaming-arch.png)

在内部，它的工作原理如下。Spark Streaming接收实时输入数据流并将数据分成批，然后由Spark引擎处理，以批量生成最终结果流。

![Spark Streaming](https://spark.apache.org/docs/latest/img/streaming-flow.png)

Spark Streaming提供了一个高层抽象，称为*离散流*或*DStream*，它表示连续的数据流。DStream可以通过Kafka，Flume和Kinesis等来源的输入数据流创建，也可以通过在其他DStream上应用高级操作来创建。在内部，DStream表示为一系列 [RDD](https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.rdd.RDD)。

本指南将向您介绍如何开始使用DStream编写Spark Streaming程序。您可以使用Scala，Java或Python（Spark 1.2中引入）编写Spark Streaming程序，所有这些都在本指南中介绍。您将在本指南中找到标签，让您在不同语言的代码片段之间进行选择。

**注意：** Python中有一些或者不同或者不可用的API。在本指南中，您将找到标记Python API来突出显示这些差异。

***

###一个简单的例子

在介绍如何编写自己的Spark Streaming程序的细节之前，让我们快速了解一下简单的Spark Streaming程序的外观。假设我们想要统计从侦听TCP套接字的数据服务器接收到的文本数据中的单词数量。你需要做的只是如下。

首先，我们创建一个 [JavaStreamingContext](https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/streaming/api/java/JavaStreamingContext.html)对象，它是所有流式传输功能的主要入口点。我们使用两个执行线程创建一个本地StreamingContext，批处理间隔为1秒。

```java
import org.apache.spark.*;
import org.apache.spark.api.java.function.*;
import org.apache.spark.streaming.*;
import org.apache.spark.streaming.api.java.*;
import scala.Tuple2;

// Create a local StreamingContext with two working thread and batch interval of 1 second
SparkConf conf = new SparkConf().setMaster("local[2]").setAppName("NetworkWordCount");
JavaStreamingContext jssc = new JavaStreamingContext(conf, Durations.seconds(1));
```

使用这个上下文，我们可以创建一个DStream，它表示来自某个TCP源的流数据，用主机名（例如`localhost`）和端口（例如`9999`）来指定。

```java
// Create a DStream that will connect to hostname:port, like localhost:9999
JavaReceiverInputDStream<String> lines = jssc.socketTextStream("localhost", 9999);
```

这里lines`的DStream即表示将从数据服务器接收的数据流。该流中的每条记录都是一行文本。然后，我们想把空格分成单词。

```java
// Split each line into words
JavaDStream<String> words = lines.flatMap(x -> Arrays.asList(x.split(" ")).iterator());
```

`flatMap`是一个DStream操作，它通过从源DStream中的每个记录生成多个新记录来创建一个新的DStream。在这种情况下，每行将被分割成多个单词，单词流表示为 `words` DStream。请注意，我们使用[FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.api.java.function.FlatMapFunction)对象定义了转换 。正如我们将要发现的那样，Java API中有许多这样的便利类可以帮助定义DStream转换。

接下来，我们要计算这些单词。

```java
// Count each word in each batch
JavaPairDStream<String, Integer> pairs = words.mapToPair(s -> new Tuple2<>(s, 1));
JavaPairDStream<String, Integer> wordCounts = pairs.reduceByKey((i1, i2) -> i1 + i2);

// Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.print();
```

