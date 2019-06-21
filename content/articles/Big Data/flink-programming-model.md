title: Flink Dataflow 编程模型
date: 2019-06-21
tags: Flink

[TOC]

Apache Flink是一个用于分布式流和批处理数据处理的开源平台。Flink的核心是流数据流引擎，为数据流上的分布式计算提供数据分发，通信和容错。Flink基于流引擎之上构建批处理，覆加本地迭代支持，内存托管和程序优化。

## 抽象层次

Flink提供不同级别的抽象来开发流/批处理应用程序。

![编程抽象级别](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/levels_of_abstraction.svg)

- 最低级抽象只提供**stateful streaming**。它通过[Process Function](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/stream/operators/process_function.html)嵌入到[DataStream API中](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/datastream_api.html)。它允许用户自由处理来自一个或多个流的事件，并使用一致的容错*状态*。此外，用户可以注册事件时间和处理时间回调，允许程序实现复杂的计算。

- 在实践中，大多数应用程序不需要上述低级抽象，而是针对**Core API**编程， 如[DataStream API](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/datastream_api.html)（有界/无界流）和[DataSet API](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/index.html)（有界数据集）。这些流畅的API提供了用于数据处理的通用构建块，例如各种形式的用户指定的转换，连接，聚合，窗口，状态等（transformations, joins, aggregations, windows, state, etc.）。在这些API中处理的数据类型在相应的编程语言中表示为类。

  低级*Process Function*与*DataStream API*集成在一起，因此只能对某些操作进行低级抽象。 *DataSet API* 提供有限数据集额外的原语支持，如循环/迭代。

- **Table API** 是以表为中心的声明性DSL ，此处的表是动态改变的表（当表示流时）。[Table API](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/table_api.html) 遵循（扩展）关系模型：表有一个模式连接（类似于在关系数据库中的表）和API提供可比的操作，如select, project, join, group-by, aggregate等。Table API程序以声明方式定义*应该执行的逻辑操作，*而不是准确指定 *操作代码的外观*。虽然Table API可以通过各种类型的用户定义函数进行扩展，但它的表现力不如*Core API*，但使用更简洁（编写的代码更少）。此外，Table API程序还会通过优化程序，在执行之前应用优化规则。

  可以在表和*DataStream* / *DataSet*之间无缝转换，允许程序混合*Table API*以及*DataStream* 和*DataSet* API。

- Flink提供的最高级抽象是**SQL**。这种抽象在语义和表达方面类似于*Table API*，但是将程序表示为SQL查询表达式。在[SQL](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/table_api.html#sql)抽象与表API紧密地相互作用，和SQL查询可以通过定义表来执行*表API*。

## 程序和数据流

Flink程序的基本构建块是**流**和**转换**。（请注意，Flink的DataSet API中使用的DataSet也是内部流 - 稍后会详细介绍。）从概念上讲，*流*是（可能永无止境的）数据记录流，而*转换*是将一个或多个流作为一个或多个流的操作。输入，并产生一个或多个输出流。

执行时，Flink程序映射到**流数据流**，由**流**和转换**运算符组成**。每个数据流都以一个或多个**源**开头，并以一个或多个**接收器**结束。数据流类似于任意有**向无环图** *（DAG）*。尽管通过*迭代*结构允许特殊形式的循环 ，但为了简单起见，我们将在大多数情况下对其进行掩饰。

![DataStream程序及其数据流。](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/program_dataflow.svg)

通常，程序中的转换与数据流中的运算符之间存在一对一的对应关系。但是，有时一个转换可能包含多个转换运算符。

源流和接收器记录在[流连接器](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/connectors/index.html)和[批处理连接器](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/connectors.html)文档中。[DataStream运算符](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/stream/operators/index.html)和[DataSet转换](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/dataset_transformations.html)中记录了[转换](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/dataset_transformations.html)。

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#top)

## 并行数据流

Flink中的程序本质上是并行和分布式的。在执行期间，*流*具有一个或多个**流分区**，并且每个*运算符*具有一个或多个**运算符子任务**。运算符子任务彼此独立，并且可以在不同的线程中执行，并且可能在不同的机器或容器上执行。

运算符子任务的数量是该特定运算符的**并行**度。流的并行性始终是其生成运算符的并行性。同一程序的不同运算符可能具有不同的并行级别。

![并行数据流](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/parallel_dataflow.svg)

流可以*以一对一*（或*转发*）模式或以*重新分发*模式在两个运营商之间传输数据：

- **一对一**流（例如，在上图中的*Source*和*map（）*运算符之间）保留元素的分区和排序。这意味着*map（）*运算符的subtask [1] 将以与*Source*运算符的subtask [1]生成的顺序相同的顺序看到相同的元素。
- **重新分配**流（在上面的*map（）*和*keyBy / window*之间，以及 *keyBy / window*和*Sink之间*）重新分配流。每个*运算符子任务*将数据发送到不同的目标子任务，具体取决于所选的转换。实例是 *keyBy（）* （其通过散列密钥重新分区），*广播（）* ，或*重新平衡（）* （其重新分区随机地）。在*重新分配*交换中，元素之间的排序仅保留在每对发送和接收子任务中（例如，*map（）的*子任务[1] 和子任务[2]*keyBy / window*）。因此，在此示例中，保留了每个密钥内的排序，但并行性确实引入了关于不同密钥的聚合结果到达接收器的顺序的非确定性。

有关配置和控制并行性的详细信息，请参阅[并行执行](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/parallel.html)的文档。

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#top)

## 视窗

聚合事件（例如，计数，总和）在流上的工作方式与批处理方式不同。例如，不可能计算流中的所有元素，因为流通常是无限的（无界）。相反，流上的聚合（计数，总和等）由**窗口**限定，例如*“在最后5分钟内计数”*或*“最后100个元素的总和”*。

Windows可以是*时间驱动的*（例如：每30秒）或*数据驱动*（例如：每100个元素）。人们通常区分不同类型的窗口，例如*翻滚窗口*（没有重叠）， *滑动窗口*（具有重叠）和*会话窗口*（由不活动间隙打断）。

![时间和计数Windows](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/windows.svg)

可以在此[博客文章中](https://flink.apache.org/news/2015/12/04/Introducing-windows.html)找到更多窗口示例。更多详细信息在[窗口文档中](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/stream/operators/windows.html)。

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#top)

## 时间

当在流程序中引用时间（例如定义窗口）时，可以参考不同的时间概念：

- **事件时间**是创建**事件的时间**。它通常由事件中的时间戳描述，例如由生产传感器或生产服务附加。Flink通过[时间戳分配器](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/event_timestamps_watermarks.html)访问事件时间戳。
- **摄取时间**是事件在源操作员处输入Flink数据流的时间。
- **处理时间**是执行基于时间的操作的每个操作员的本地时间。

![事件时间，摄取时间和处理时间](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/event_ingestion_processing_time.svg)

有关如何处理时间的更多详细信息，请参阅[事件时间文档](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/event_time.html)。

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#top)

## 有状态的操作

虽然数据流中的许多操作只是一次查看一个单独的*事件*（例如事件解析器），但某些操作会记住多个事件（例如窗口操作符）的信息。这些操作称为**有状态**。

状态操作的状态保持在可以被认为是嵌入式键/值存储的状态中。状态被分区并严格地与有状态运营商读取的流一起分发。因此，只有在*keyBy（）*函数之后才能在*键控流*上访问键/值状态，并且限制为与当前事件的键相关联的值。对齐流和状态的密钥可确保所有状态更新都是本地操作，从而保证一致性而无需事务开销。此对齐还允许Flink重新分配状态并透明地调整流分区。

![状态和分区](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/state_partitioning.svg)

有关更多信息，请参阅有关[状态](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/stream/state/index.html)的文档。

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#top)

## 容错检查点

Flink使用**流重放**和**检查点**的组合实现容错。检查点与每个输入流中的特定点以及每个操作符的对应状态相关。通过恢复运算符的状态并从检查点重放事件，可以从检查点恢复流数据流，同时保持一致性*（恰好一次处理语义）*。

检查点间隔是在执行期间用恢复时间（需要重放的事件的数量）来折衷容错开销的手段。

[容错内部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/internals/stream_checkpointing.html)的描述提供了有关Flink如何管理检查点和相关主题的更多信息。有关启用和配置检查点的详细信息，请参阅[检查点API文档](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/stream/state/checkpointing.html)。

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#top)

## 批量流媒体

Flink执行[批处理程序](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/index.html)作为流程序的特殊情况，其中流是有界的（有限数量的元素）。甲*数据集*在内部视为数据流。因此，上述概念以相同的方式应用于批处理程序，并且它们适用于流程序，除了少数例外：

- [批处理程序的容错](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/fault_tolerance.html)不使用检查点。通过完全重放流来进行恢复。这是可能的，因为输入有限。这会使成本更多地用于恢复，但使常规处理更便宜，因为它避免了检查点。
- DataSet API中的有状态操作使用简化的内存/核外数据结构，而不是键/值索引。
- DataSet API引入了特殊的同步（超级步骤）迭代，这些迭代只能在有界流上进行。有关详细信息，请查看[迭代文档](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/iterations.html)。

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#top)

## 下一步