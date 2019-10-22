title: Flink 词汇表
date: 2019-10-11
tags: Flink

[TOC]

#### Flink应用程序集群

Flink应用程序集群是指仅执行一个[Flink作业](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-job)专用的[Flink集群](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-cluster)。该[Flink集群](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-cluster)的生命周期与对应Flink作业的生命周期相同。在*工作模式下，*以前的Flink应用程序集群也称为Flink集群。点击查看与[Flink Session Cluster](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-session-cluster)的比较。

#### Flink集群

一种分布式系统，通常由一个[Flink Master](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-master)和一个或多个 [Flink TaskManager](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-taskmanager)进程组成。

#### 事件

事件是有关由应用程序建模的域的状态更改的声明。事件可以是流或批处理应用程序的输入和/或输出。事件是特殊类型的[记录](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#Record)。

#### 执行图

见[物理图](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#physical-graph)

#### 函数

函数由用户实现，并封装Flink程序的应用程序逻辑。大多数函数由相应的[算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)包装 。

#### 实例

术语*实例*用于描述在运行期间特定类型的特定实例（通常是 [算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)或[函数](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#function)）。由于Apache Flink主要是用Java编写的，因此它对应于Java中的*Instance*或*Object*的定义。在Apache Flink的上下文中，术语“ *并行实例”*也经常用来强调相同[算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)或[函数](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#function)类型的多个实例正在并行运行。

#### Flink作业

Flink作业是Flink程序的运行时表示形式。Flink作业既可以提交到长期运行的[Flink会话集群](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-session-cluster)，也可以作为独立的[Flink应用程序集群启动](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-application-cluster)。

#### 作业图

请参阅[逻辑图](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#logical-graph)

#### Flink JobManager

JobManager是[Flink Master中](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-master)运行的组件之一。JobManager负责监督单个作业的[任务](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#task)执行。历史上，整个[Flink Master](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-master)都称为JobManager。

#### 逻辑图

逻辑图是描述流处理程序的高级逻辑的有向图。节点是[算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)，边指示输入/输出关系或数据流或数据集。

#### 受管状态

受管状态描述了已在框架中注册的应用程序状态。对于受管状态，Apache Flink将特别关注持久性和可伸缩性。

#### Flink Master

Flink Master是[Flink群集](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-cluster)的Master。它包含三个不同的组件：Flink Resource Manager（资源管理器），Flink Dispatcher（FLink 调度器）和每个运行的[Flink Job](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-job)的[Flink JobManager](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-jobmanager)。

#### 算子

[逻辑图的](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#logical-graph)节点。算子执行某种操作，通常由[Function](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#function)执行。Source和SInk是用于数据摄取和数据出口的特殊算子。

#### 算子链

一个算子链由两个或多个连续的[算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)组成，中间没有任何重新分配（rebalance）。同一算子链中的算子无需经过序列化或Flink的网络堆栈即可直接将记录彼此转发。

#### 分区

分区是整个数据流或数据集的独立子集。通过将每个[记录](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#Record)分配给一个或多个分区，将数据流或数据集划分为多个分区。[任务](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#task)在运行时消费数据流或数据集的分区。改变数据流或数据集分区方式的转换通常称为重新分区（repartitioning）。

#### 物理图

物理图是转换[逻辑图](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#logical-graph)以在分布式运行时中执行的结果。节点是[任务](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#task)，边指示数据流或数据集的输入/输出关系或[分区](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#partition)。

#### 记录

记录是数据集或数据流的组成元素。[算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)和 [函数](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#Function)接收记录作为输入，并发出记录作为输出。

#### Flink会话集群

长期运行的[Flink群集](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-cluster)，它接受多个[Flink作业](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-job)来执行。此Flink群集的生存期未绑定到任何Flink作业的生存期。以前，Flink群集在*会话模式下*也称为Flink会话群集。与[Flink应用程序集群](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-application-cluster)进行比较 。

#### 状态后端

对于流处理程序，[Flink作业](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-job)的状态后端确定如何在每个TaskManager（TaskManager的Java堆或（嵌入式）RocksDB）上存储其 [状态](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#managed-state)，以及在检查点上写入状态的位置（[Flink Master](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-master)或文件系统的Java堆） ）。

#### 子任务

子任务是负责处理数据流[分区](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#partition)的[任务](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#task)。术语“子任务”强调针对同一[算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)或[算子链](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator-chain)有多个并行任务 。

#### 任务

[物理图的](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#physical-graph)节点。任务是基本工作单元，由Flink的运行时执行。任务恰好封装了[算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)或[算子链](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator-chain)的一个并行实例 。

#### Flink任务管理器

TaskManager是[Flink群集](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#flink-cluster)的工作进程。[Tasks](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#task)安排在TaskManager中执行。它们彼此通信以在连续的任务之间交换数据。

#### 转换

将转换应用于一个或多个数据流或数据集，并产生一个或多个输出数据流或数据集。转换可能会更改数据流或数据集的每个记录，但也可能仅更改其分区或执行聚合。虽然 [算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)和[函数](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#function)是Flink API的“物理”部分，但转换只是API概念。具体来说，大多数（但不是全部）转换是由某些[算子](https://ci.apache.org/projects/flink/flink-docs-release-1.9/concepts/glossary.html#operator)实现的。