title: Flink用例
date: 2019-06-20
tags: Flink

[TOC]

Apache Flink因其丰富的功能集而成为开发和运行多种不同类型应用程序的绝佳选择。Flink的功能包括支持流和批处理，复杂的状态管理，事件时间处理语义以及状态的精确一次一致性保证。此外，Flink可以部署在各种资源提供者（如YARN，Apache Mesos和Kubernetes）上，也可以作为裸机硬件上的独立群集。配置为高可用性，Flink没有单点故障。Flink已被证明可扩展到数千个核心和TB级的应用程序状态，提供高吞吐量和低延迟，并为世界上最苛刻的流处理应用程序提供支持。

下面，我们将探讨由Flink提供支持的最常见类型的应用程序，并指出实际示例。

- [事件驱动的应用程序](https://flink.apache.org/usecases.html#eventDrivenApps)
- [数据分析应用](https://flink.apache.org/usecases.html#analytics)
- [数据管道应用](https://flink.apache.org/usecases.html#pipelines)

## 事件驱动的应用程序

### 什么是事件驱动的应用程序？

事件驱动的应用程序是一个有状态的应用程序，它从一个或多个事件流中提取事件，并通过触发计算，状态更新或外部操作对传入事件做出反应。

事件驱动的应用程序是传统应用程序设计的演变。传统应用一般具有独立的计算和数据存储层，在此体系结构中，应用程序从远程事务数据库读取数据并将数据持久化。

相反，事件驱动的应用程序基于有状态流处理应用程序。在这种设计中，数据和计算是共同定位的，即本地（内存或磁盘）数据访问。通过定期将检查点写入远程持久存储来实现容错。下图描绘了传统应用程序体系结构和事件驱动应用程序之间的差异。



![img](https://flink.apache.org/img/usecases-eventdrivenapps.png)

### 事件驱动的应用程序有哪些优点？

事件驱动的应用程序不是查询远程数据库，而是在本地访问其数据，从而在吞吐量和延迟方面产生更好的性能。远程持久存储的定期检查点可以异步和递增完成。因此，检查点对常规事件处理的影响非常小。但是，事件驱动的应用程序设计提供的不仅仅是本地数据访问。在分层体系结构中，多个应用程序共享同一数据库是很常见的。因此，需要协调数据库的任何更改，例如由于应用程序更新或扩展服务而更改数据布局。由于每个事件驱动的应用程序都负责自己的数据，因此更改数据表示或扩展应用程序只需要较少的协调。

### Flink如何支持事件驱动的应用程序？

事件驱动应用程序的限制由流处理器处理时间和状态的程度来定义。Flink的许多杰出功能都围绕着这些概念。Flink提供了一组丰富的状态原语，可以管理非常大的数据量（最多几TB），并且具有精确一次性的一致性保证。此外，Flink支持事件时间，高度可定制的窗口逻辑，以及通过`ProcessFunction`实现高级业务逻辑提供的细粒度时间控制。此外，Flink还提供了一个用于复杂事件处理（CEP）的库，用于检测数据流中的模式。

然而，Flink在事件驱动应用程序方面的出色功能是savepoint。保存点是一致的状态快照，可用作兼容应用程序的起点。给定保存点，可以更新应用程序或调整其规模，或者可以启动应用程序的多个版本以进行A / B测试。

### 什么是典型的事件驱动应用程序？

- [欺诈识别](https://sf-2017.flink-forward.org/kb_sessions/streaming-models-how-ing-adds-models-at-runtime-to-catch-fraudsters/)
- [异常检测](https://sf-2017.flink-forward.org/kb_sessions/building-a-real-time-anomaly-detection-system-with-flink-mux/)
- [基于规则的警报](https://sf-2017.flink-forward.org/kb_sessions/dynamically-configured-stream-processing-using-flink-kafka/)
- [业务流程监控](https://jobs.zalando.com/tech/blog/complex-event-generation-for-business-process-monitoring-using-apache-flink/)
- [Web应用程序（社交网络）](https://berlin-2017.flink-forward.org/kb_sessions/drivetribes-kappa-architecture-with-apache-flink/)

## 数据分析应用

### 什么是数据分析应用程序？

分析工作从原始数据中提取信息和洞察力。传统上，分析在记录事件的有界数据集上作为批量查询或应用程序执行。为了将最新数据合并到分析结果中，必须将其添加到分析的数据集中，并重新运行查询或应用程序。结果将写入存储系统或作为报告发出。

借助先进的流处理引擎，还可以实时地执行分析。流式查询或应用程序不是读取有限数据集，而是摄取实时事件流，并在消耗事件时不断生成和更新结果。结果要么写入外部数据库，要么保持为内部状态。仪表板应用程序可以从外部数据库读取最新结果或直接查询应用程序的内部状态。

Apache Flink支持流式和批量分析应用程序，如下图所示。

![img](https://flink.apache.org/img/usecases-analytics.png)

### 流式分析应用程序有哪些优势？

与批量分析相比，连续流分析的优势不仅限于因消除定期导入和查询执行而从事件到洞察的低得多的延迟。与批量查询相比，流式查询不必处理输入数据中的人为边界，这些边界是由定期导入和输入的有界性质引起的。

另一方面是更简单的应用程序架构。批处理分析管道由若干独立组件组成，以定期调度数据提取和查询执行。可靠地操作这样的管道并非易事，因为一个组件的故障会影响管道的后续步骤。相比之下，在像Flink这样的复杂流处理器上运行的流分析应用程序包含从数据摄取到连续结果计算的所有步骤。因此，它可以依赖于引擎的故障恢复机制。

### Flink如何支持数据分析应用程序？

Flink为连续流式传输和批量分析提供了非常好的支持。具体来说，它具有符合ANSI标准的SQL接口，具有用于批处理和流式查询的统一语义。无论是在记录事件的静态数据集上还是在实时事件流上运行，SQL查询都会计算相同的结果。对用户定义函数的丰富支持可确保在SQL查询中执行自定义代码。如果需要更多的自定义逻辑，Flink的DataStream API或DataSet API提供更多的低级控制。此外，Flink的Gelly库为批量数据集上的大规模和高性能图形分析提供算法和构建块。

### 什么是典型的数据分析应用程序？

- [电信网络的质量监控](http://2016.flink-forward.org/kb_sessions/a-brief-history-of-time-with-apache-flink-real-time-monitoring-and-analysis-with-flink-kafka-hb/)
- [分析](https://techblog.king.com/rbea-scalable-real-time-analytics-king/)移动应用程序中[的产品更新和实验评估](https://techblog.king.com/rbea-scalable-real-time-analytics-king/)
- 对消费者技术中[的实时数据](https://eng.uber.com/athenax/)进行[特别分析](https://eng.uber.com/athenax/)
- 大规模图分析

## 数据管道应用

### 什么是数据管道？

提取 - 转换 - 加载（ETL）是在存储系统之间转换和移动数据的常用方法。通常会定期触发ETL作业，以将数据从事务数据库系统复制到分析数据库或数据仓库。

数据管道与ETL作业具有相似的用途。它们可以转换和丰富数据，并可以将数据从一个存储系统移动到另一个。但是，它们以连续流模式运行，而不是定期触发。因此，他们能够从连续生成数据的源中读取记录，并以低延迟将其移动到目的地。例如，数据管道可能会监视文件系统目录中的新文件，并将其数据写入事件日志。另一个应用程序可能会将事件流实现到数据库，或者逐步构建和优化搜索索引。

下图描述了定期ETL作业和连续数据管道之间的差异。

![img](https://flink.apache.org/img/usecases-datapipelines.png)

### 数据管道有哪些优势？

连续数据流水线优于周期性ETL作业的明显优势是减少了将数据移动到目的地的延迟。此外，数据管道更通用，可用于更多用例，因为它们能够连续消耗和发送数据。

### Flink如何支持数据管道？

Flink的SQL接口（或表API）可以解决许多常见的数据转换或丰富任务，并支持用户定义的函数。通过使用更通用的DataStream API，可以实现具有更高级要求的数据管道。Flink为各种存储系统（如Kafka，Kinesis，Elasticsearch和JDBC数据库系统）提供了丰富的连接器。它还具有连续的文件系统源，用于监视以时间分区方式写入文件的目录和接收器。

### 什么是典型的数据管道应用？

- 电子商务中[的实时搜索索引构建](https://ververica.com/blog/blink-flink-alibaba-search)
- 电子商务中[持续的ETL](https://jobs.zalando.com/tech/blog/apache-showdown-flink-vs.-spark/)