title: Flink入门
date: 2019-06-13

[TOC]

### 一、架构
Apache Flink是一个分布式处理引擎和框架，用于对无界和有界数据流进行状态计算。Flink可在所有常见的集群环境中运行，可以内存级速度和任意规模执行计算。

接下来首先我们阐述Flink的架构。

#### 处理无界和有界数据

任何类型的数据都是作为事件流产生的。信用卡交易，传感器测量，机器日志或网站或移动应用程序上的用户交互，所有这些数据都作为流生成。

数据可以作为*无界*或*有界*流处理。

1. **无界流**有一个开始但没有明确定义的结束。它们不会终止，并且数据在生成时即提供。必须连续处理无界流，即必须在摄取事件后立即处理事件。无法等待所有输入数据到达，因为输入是无界的，并且在任何时间点都不会完成。处理无界数据通常要求以特定顺序摄取事件，例如事件发生的顺序，以便能够推断结果完整性。无界流的处理也称为流处理。
2. **有界流**具有明确定义的开始和结束。可以通过在执行任何计算之前先摄取所有数据的方式来处理有界流。处理有界流不需要有序摄取，因为可以始终对有界数据集进行排序。有界流的处理也称为批处理。

![](https://flink.apache.org/img/bounded-unbounded.png)

**Apache Flink擅长处理无界和有界数据集。**精确控制时间和状态使Flink的运行时能够在无界流上运行任何类型的应用程序。有界流由算法和数据结构内部处理，这些算法和数据结构专为固定大小的数据集而设计，从而产生出色的性能。

#### 随处部署应用程序

Apache Flink是一个分布式系统，需要计算资源才能执行应用程序。Flink可与所有常见的集群资源管理器（Resource Manager, 如[Hadoop YARN](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html)，[Apache Mesos](https://mesos.apache.org/)和[Kubernetes）集成，](https://kubernetes.io/)但也可以设置为作为独立集群运行。

Flink旨在很好地运作以上列出的每个资源管理器。这是通过与资源管理器对应的部署模式实现的，这些模式允许Flink以其惯用方式与每个资源管理器进行交互。

部署Flink应用程序时，Flink会根据应用程序配置的并行性自动识别所需资源，并从资源管理器请求它们。如果发生故障，Flink会通过请求新资源来替换发生故障的容器。提交或控制应用程序的所有通信都通过REST调用进行。这简化了Flink在许多环境中的集成。

#### 以任何规模运行应用程序

Flink旨在以任何规模运行有状态流应用程序。应用程序并行化为数千个在集群中分布和同时执行的任务。因此，应用程序可以利用几乎无限量的CPU，主内存，磁盘和网络IO。而且，Flink很容易保持非常大的应用程序状态。其异步和增量检查点算法确保对处理延迟的影响最小，同时保证“精确一次”的状态一致性。

[用户报告了](https://flink.apache.org/poweredby.html)在其生产环境中运行的Flink应用程序[令人印象深刻的可扩展性的数字](https://flink.apache.org/poweredby.html)，例如：

- 应用程序**每天**处理**数万亿个事件**，
- 应用程序维护**多个TB的状态**，
- 应用程序**在数千个内核的运行**。

#### 利用内存中性能

有状态Flink应用程序针对本地状态访问进行了优化。任务状态始终保留在内存中，如果状态大小超过可用内存，则保存在访问高效的磁盘上数据结构中。因此，任务通过访问本地（通常是内存中）状态来执行所有计算，从而产生非常低的处理延迟。Flink通过定期和异步地将本地状态checkpoint到持久存储来保证在出现故障时的“精确一次”的状态一致性。

![](https://flink.apache.org/img/local-state.png)

### 二、应用

Apache Flink是一个用于对无界和有界数据流进行有状态计算的框架。Flink在不同的抽象级别提供多个API，并为常见用例提供专用库。

在这里，我们介绍Flink易于使用和富有表现力的API和库。

#### 流处理应用的构建元素

可以由流处理框架构建和执行的应用程序的类型由框架控制*流*，*状态*和*时间*的程度来定义。在下文中，我们描述了流处理应用程序的这些构建块，并解释了Flink处理它们的方法。

##### 流

显然，流是流处理的一个基本元素。但是，流可以具有不同的特征，这些特征会影响流的处理方式。Flink是一个多功能的处理框架，可以处理任何类型的流。

- **有界**和**无界**流：流可以是无界的或有界的，即固定大小的数据集。Flink具有完美支持处理无界流的成熟功能，同时也有专门的算子来有效地处理有界流。
- **实时**和**记录**流：所有数据都作为流生成。有两种方法可以处理数据。在生成时实时处理它或将流持久保存到存储系统（例如，文件系统或对象存储库），并在以后处理它。Flink应用程序可以处理记录或实时流。

##### 状态

每个有意义的流应用程序都是有状态的，只有对单个事件进行转换的应用才不需要状态。运行基本业务逻辑的任何应用程序都需要记住事件或中间结果，以便在以后的时间点访问它们，例如在收到下一个事件时或在特定持续时间之后。

![](https://flink.apache.org/img/function-state.png)

应用状态是Flink中的“一等公民”。可以通过Flink在状态处理环境中提供的所有功能来确认这一点：

- **多状态基元**：Flink为不同的数据结构提供状态基元，例如原子值，列表或映射。开发人员可以根据函数的访问模式选择最有效的状态原语。
- **可插拔状态后端**：应用程序状态由可插拔状态后端管理和checkpoint。Flink具有不同的状态后端，可以在内存或[RocksDB](https://rocksdb.org/)中存储状态，[RocksDB](https://rocksdb.org/)是一种高效的嵌入式磁盘数据存储。也可以插入自定义状态后端。
- **精确一次的状态一致性**：Flink的checkpoint和恢复算法可确保在发生故障时应用程序状态的一致性。因此，故障是透明处理的，不会影响应用程序的正确性。
- **非常大的状态**：由于其异步和增量检查点算法，Flink能够维持几兆兆字节的应用程序状态。
- **可扩展的应用程序**：Flink通过将状态重新分配给更多或更少的workers来支持有状态应用程序的伸缩。

##### 时间

时间是流应用程序的另一个重要组成部分，大多数事件流都具有固有的时间语义，因为每个事件都是在特定时间点生成的。此外，许多常见的流计算都基于时间，比如 windows aggregations, sessionization, pattern detection, 以及time-based joins。流处理的一个重要方面是应用程序如何测量时间，即事件时间和处理时间的差异。

Flink提供了一组丰富的与时间相关的功能。

- **事件时间模式**：使用事件时间语义处理流的应用程序根据事件的时间戳计算结果。因此，无论是否处理记录的或实时的事件，事件时间处理都允许准确和一致的结果。
- **水印支持**：Flink使用水印来推断事件时间应用中的时间。水印也是一种灵活的机制，可以权衡延迟和结果的完整性。
- **延迟数据处理**：当使用水印在事件时间模式下处理流时，可能会在所有相关事件到达之前完成计算。这类事件被称为迟发事件。Flink具有多个选项来处理延迟事件，例如通过侧输出重新路由它们并更新以前完成的结果。
- **处理时间模式**：除了事件时间模式之外，Flink还支持处理时间语义，该处理时间语义执行由处理机器的挂钟时间触发的计算。处理时间模式适用于具有严格的低延迟要求、可以容忍近似结果的某些应用。

#### 分层API

Flink提供三层API。每个API在简洁性和表达性之间提供不同的权衡，并针对不同的用例。

![](https://flink.apache.org/img/api-stack.png)

我们简要介绍每个API，讨论其应用，并显示代码示例。

##### ProcessFunctions

[ProcessFunctions](https://ci.apache.org/projects/flink/flink-docs-stable/dev/stream/operators/process_function.html)是Flink提供的最具表现力的功能接口。Flink提供ProcessFunction来处理来自一个或两个输入流的单个事件，或被分组在一个窗口中的事件。ProcessFunctions提供对时间和状态的细粒度控制。ProcessFunction可以任意修改其状态并注册将在未来触发回调函数的定时器。因此，ProcessFunctions可以根据许多[有状态事件驱动的应用的](https://flink.apache.org/usecases.html#eventDrivenApps)需要实现复杂的每事件业务逻辑。

以下显示了一个`KeyedProcessFunction`对一个 `KeyedStream`进行操作，匹配 `START`以及`END`事件的示例。当一个`START`事件被接收，则该函数在状态中记住其时间戳并且注册一个4小时的计时器。如果在计时器触发之前收到`END`事件，则该函数计算事件`END`和`START`事件之间的持续时间，清除状态并返回值。否则，计时器只会超时并清除状态。

```java
/**
 * Matches keyed START and END events and computes the difference between 
 * both elements' timestamps. The first String field is the key attribute, 
 * the second String attribute marks START and END events.
 */
public static class StartEndDuration
    extends KeyedProcessFunction<String, Tuple2<String, String>, Tuple2<String, Long>> {

  private ValueState<Long> startTime;

  @Override
  public void open(Configuration conf) {
    // obtain state handle
    startTime = getRuntimeContext()
      .getState(new ValueStateDescriptor<Long>("startTime", Long.class));
  }

  /** Called for each processed event. */
  @Override
  public void processElement(
      Tuple2<String, String> in,
      Context ctx,
      Collector<Tuple2<String, Long>> out) throws Exception {

    switch (in.f1) {
      case "START":
        // set the start time if we receive a start event.
        startTime.update(ctx.timestamp());
        // register a timer in four hours from the start event.
        ctx.timerService()
          .registerEventTimeTimer(ctx.timestamp() + 4 * 60 * 60 * 1000);
        break;
      case "END":
        // emit the duration between start and end event
        Long sTime = startTime.value();
        if (sTime != null) {
          out.collect(Tuple2.of(in.f0, ctx.timestamp() - sTime));
          // clear the state
          startTime.clear();
        }
      default:
        // do nothing
    }
  }

  /** Called when a timer fires. */
  @Override
  public void onTimer(
      long timestamp,
      OnTimerContext ctx,
      Collector<Tuple2<String, Long>> out) {

    // Timeout interval exceeded. Cleaning up the state.
    startTime.clear();
  }
}
```

这个例子说明了`KeyedProcessFunction`的表现力，但也强调了它是一个相当冗长的接口。

##### The DataStream API

[DataStream API](https://ci.apache.org/projects/flink/flink-docs-stable/dev/datastream_api.html)为诸如窗口等许多常见的流处理操作提供原语。DataStream API可用于Java和Scala，基于如`map()`，`reduce()`和`aggregate()`等方法。可以通过扩展接口，或像Java或Scala中lambda函数一样来定义函数。

以下示例显示如何对点击流进行会话化并计算每个会话的点击次数。

```java
// a stream of website clicks
DataStream<Click> clicks = ...

DataStream<Tuple2<String, Long>> result = clicks
  // project clicks to userId and add a 1 for counting
  .map(
    // define function by implementing the MapFunction interface.
    new MapFunction<Click, Tuple2<String, Long>>() {
      @Override
      public Tuple2<String, Long> map(Click click) {
        return Tuple2.of(click.userId, 1L);
      }
    })
  // key by userId (field 0)
  .keyBy(0)
  // define session window with 30 minute gap
  .window(EventTimeSessionWindows.withGap(Time.minutes(30L)))
  // count clicks per session. Define function as lambda function.
  .reduce((a, b) -> Tuple2.of(a.f0, a.f1 + b.f1));
```

##### SQL & Table API

Flink具有两个关系型API，[Table API和SQL](https://ci.apache.org/projects/flink/flink-docs-stable/dev/table/index.html)。这两个API都是用于批处理和流处理的统一API，即，在无界的实时流或有界的记录流上以相同的语义执行查询，并产生相同的结果。Table API和SQL利用[Apache Calcite](https://calcite.apache.org/)进行解析，验证和查询优化。它们可以与DataStream和DataSet API无缝集成，并支持用户定义的标量，聚合和表值函数。

Flink的关系型API旨在简化[数据分析](https://flink.apache.org/usecases.html#analytics)，[数据pipelining和ETL应用](https://flink.apache.org/usecases.html#pipelines)的定义。

以下示例显示用于会话化点击流并计算每个会话的点击次数的SQL查询。这与DataStream API示例中的用例相同。

```sql
SELECT userId, COUNT(*)
FROM clicks
GROUP BY SESSION(clicktime, INTERVAL '30' MINUTE), userId
```

#### 库

Flink具有几个用于常见数据处理用例的库。这些库通常嵌入在API中，而不是完全独立的。因此，他们可以从API的所有功能中受益，并与其他库集成。

- **[复杂事件处理（CEP）](https://ci.apache.org/projects/flink/flink-docs-stable/dev/libs/cep.html)**：模式检测是事件流处理的一个非常常见的用例。Flink的CEP库提供了一个API来指定事件的模式（想想正则表达式或状态机）。CEP库与Flink的DataStream API集成，以便在DataStream上评估模式。CEP库的应用包括网络入侵检测，业务流程监控和欺诈检测。
- **[DataSet API](https://ci.apache.org/projects/flink/flink-docs-stable/dev/batch/index.html)**：DataSet API是Flink用于批处理应用程序的核心API。DataSet API的原语包括 *map*， *reduce*，*（外部）join*，*co-group*和 *iterate*。所有操作都由算法和数据结构支持，这些算法和数据结构对内存中的序列化数据进行操作，并在数据大小超过内存预算时溢出到磁盘。Flink的DataSet API的数据处理算法是受传统数据库运算符的启发，例如混合散列连接或外部合并排序。
- **[Gelly](https://ci.apache.org/projects/flink/flink-docs-stable/dev/libs/gelly/index.html)**：Gelly是一个可扩展的图形处理和分析库。Gelly在DataSet API之上实现并与之集成。因此，它受益于其可扩展且强大的算子。Gelly具有[内置算法](https://ci.apache.org/projects/flink/flink-docs-stable/dev/libs/gelly/library_methods.html)，例如标签传播，三角形枚举和页面排名，但也提供了一种[ Graph API](https://ci.apache.org/projects/flink/flink-docs-stable/dev/libs/gelly/graph_api.html)从而简化自定义图算法的实现。

### 三、运行

由于许多流应用程序旨在以最短的停机时间连续运行，因此流处理器必须提供出色的故障恢复，以及在应用程序运行时监视和维护应用程序的工具。

Apache Flink非常关注流处理的运维方面。在这里，我们将解释Flink的故障恢复机制，并介绍其管理和监督正在运行的应用程序的功能。

#### 全天候运行您的应用程序

机器和过程故障在分布式系统中无处不在。像Flink这样的分布式流处理器必须从故障中恢复，以便能够24/7全天候运行流应用程序。显然，这不仅意味着在故障后重新启动应用程序，而且还要确保其内部状态保持一致，以便应用程序可以继续处理，就像从未发生过故障一样。

Flink提供了多种功能，以确保应用程序保持运行并保持一致：

- **一致的检查点**：Flink的恢复机制基于应用程序状态的一致检查点。如果发生故障，将重新启动应用程序并从最新检查点加载其状态。结合可重置流源，此功能可以保证*精确一次的状态一致性*。
- **高效检查点**：如果应用程序保持TB级状态，则checkpoint应用程序的状态可能非常昂贵。Flink可以执行异步和增量检查点，以便将检查点对应用程序的延迟SLA的影响保持在非常小的水平。
- **端到端精确一次**：Flink为特定存储系统提供事务接收器，保证数据只写出一次，即使出现故障。
- **与集群管理器集成**：Flink与集群管理器紧密集成，例如[Hadoop YARN](https://hadoop.apache.org/)，[Mesos](https://mesos.apache.org/)或[Kubernetes](https://kubernetes.io/)。当进程失败时，将自动启动一个新进程来接管其工作。
- **高可用性设置**：Flink具有高可用性模式，可消除所有单点故障。HA模式基于[Apache ZooKeeper](https://zookeeper.apache.org/)，这是一种经过验证的可靠分布式协调服务。

#### 更新，迁移，暂停和恢复您的应用程序

需要维护为关键业务服务提供支持的流应用程序。需要修复错误，并且需要实现改进或新功能。但是，更新有状态流应用程序并非易事。通常，人们不能简单地停止应用程序并重新启动固定版本或改进版本，因为人们无法承受丢失应用程序的状态。

Flink的*Savepoints*是一个独特而强大的功能，可以解决更新有状态应用程序和许多其他相关挑战的问题。保存点是应用程序状态的一致快照，因此与检查点非常相似。但是，与检查点不同，保存点需要手动触发，并且在应用程序停止时不会自动删除保存点。保存点可用于启动状态兼容的应用程序并初始化其状态。保存点具有以下功能：

- **应用程序演变**：保存点可用于演进应用程序。一个应用程序的固定或改进版本可以从先前版本的保存点重新启动。也可以从较早的时间点（假设存在这样的保存点）启动应用程序，以修复由有缺陷的版本产生的错误结果。
- **群集迁移**：使用保存点，可以将应用程序迁移（或克隆）到不同的群集。
- **Flink版本更新**：可以使用保存点迁移应用程序以在新的Flink版本上运行。
- **应用程序扩展**：保存点可用于增加或减少应用程序的并行性。
- **A / B测试和假设情景**：可以通过启动同一保存点的所有版本来比较两个（或更多）不同版本的应用程序的性能或质量。
- **暂停和恢复**：可以通过获取保存点并停止应用程序来暂停应用程序。在以后的任何时间点，都可以从保存点恢复应用程序。
- **存档**：可以存档，以便能够将应用程序的状态重置为较早的时间点。

#### 监控您的应用程序

与任何其他服务一样，需要对连续运行的流应用程序进行监督，并将其集成到组织的运营基础架构（即监控和日志记录服务）中。监控有助于预测问题并提前做出反应。通过日志记录可以进行根因分析调查失败。最后，通过一个易于访问的接口来控制运行应用程序的是一个重要特性。

Flink与许多常见的日志记录和监视服务很好地集成，并提供REST API来控制应用程序和查询信息。

- **Web UI**：Flink具有Web UI，可以检查，监视和调试正在运行的应用程序。它还可用于提交执行或取消执行。
- **日志记录**：Flink实现了流行的slf4j日志记录界面，并与日志框架[log4j](https://logging.apache.org/log4j/2.x/)或[logback](https://logback.qos.ch/)集成。
- **指标**：Flink具有复杂的指标系统，可收集和报告系统和用户定义的指标。指标可以导出到多个报告器，包括[JMX](https://en.wikipedia.org/wiki/Java_Management_Extensions)，Ganglia，[Graphite](https://graphiteapp.org/)，[Prometheus](https://prometheus.io/)，[StatsD](https://github.com/etsy/statsd)，[Datadog](https://www.datadoghq.com/)和[Slf4j](https://www.slf4j.org/)。
- **REST API**：Flink公开REST API以提交新应用程序、生成正在运行的应用程序的保存点或取消应用程序。REST API还公开元数据和收集运行或已完成应用程序的指标。