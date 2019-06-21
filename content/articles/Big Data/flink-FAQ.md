title: Flink FAQ
date: 2019-06-21
tags: Flink

[TOC]

### Apache Flink仅用于（近）实时处理用例吗？

Flink是一个非常通用的系统，用于数据处理和数据驱动的应用程序，*数据流*作为核心构建块。这些数据流可以是实时数据流或存储的历史数据流。例如，在Flink的视图中，文件是存储的字节流。因此，Flink支持实时数据处理和应用程序，以及批处理应用程序。

流可以是*无界的*（没有结束，事件不断发生）或受*限制*（流有开始和结束）。例如，来自消息队列的Twitter馈送或事件流通常是无界的流，而来自文件的字节流是有界流。

### 如果一切都是流，为什么Flink中有DataStream和DataSet API？

有界流通常比无界流更高效。在（近）实时处理无限事件流需要系统能够立即对事件起作用并产生中间结果（通常具有低延迟）。处理有界流通常不需要产生低延迟结果，因为无论如何数据都是旧的（相对而言）。这允许Flink以简单且更高效的方式处理数据。

DataStream API 捕获无界和有界的流的连续处理，以支持低等待时间的结果以及对事件和时间（包括事件时间）灵活反应的模型。

DataSet API 具有加快有界的数据流的处理的技术。将来，社区计划将这些优化与DataStream API中的技术相结合。

### Flink如何与Hadoop栈相关联？

Flink独立于[Apache Hadoop，](https://hadoop.apache.org/)并且在没有任何Hadoop依赖性的情况下运行。

但是，Flink与许多Hadoop组件集成得非常好，例如*HDFS*，*YARN*或*HBase*。与这些组件一起运行时，Flink可以使用HDFS读取数据，或写入结果和检查点/快照。Flink可以通过YARN轻松部署，并与YARN和HDFS Kerberos安全模块集成。

### Flink可运行的其他栈是什么？

用户在[Kubernetes](https://kubernetes.io/)，[Mesos](https://mesos.apache.org/)， [Docker](https://www.docker.com/)上运行Flink ，甚至作为独立服务运行。

### 使用Flink有哪些先决条件？

- 您需要*Java 8*来运行Flink作业/应用程序。
- Scala API（可选）基于Scala 2.11。
- [Apache ZooKeeper](https://zookeeper.apache.org/)需要高度可用且没有单点故障的设置。
- 对于可以从故障中恢复的高可用流处理设置，Flink需要某种形式的分布式存储用于检查点（HDFS / S3 / NFS / SAN / GFS / Kosmos / Ceph / ...）。

### Flink支持多大的规模？

用户可在非常小的配置（少于5个节点）和1000个节点以及TB级的状态上运行Flink作业。

### Flink是否仅限于内存数据集？

对于DataStream API，Flink支持大于内存的状态来配置RocksDB状态后端。

对于DataSet API，所有操作（delta迭代除外）都可以扩展到主内存之外。