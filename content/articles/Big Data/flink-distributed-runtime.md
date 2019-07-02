title: Flink 分布式运行时环境
date: 2019-07-01
tags: Flink

[TOC]

## 任务和算子链

对于分布式执行，Flink将多个算子子任务链串联成任务。每个任务由一个线程执行。将算子链接到任务是一项有用的优化：它可以减少线程到线程切换和缓冲的开销，并在降低延迟的同时提高整体吞吐量。可以配置链接行为; 有关详细信息，请参阅[链接文档](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/stream/operators/#task-chaining-and-resource-groups)。

下图中的示例数据流由五个子任务执行，因此具有五个并行线程。

![算子链接到任务](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/tasks_chains.svg)

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/runtime.html#top)

## 工作经理，任务经理，客户

Flink运行时包含两种类型的进程：

- 该**JobManagers**（也称为*大师*）协调分布式执行。他们安排任务，协调检查点，协调故障恢复等。

  总是至少有一个Job Manager。高可用性设置将具有多个JobManagers，其中一个始终是*领导者*，其他人处于*待机状态*。

- 该**TaskManagers**（也叫*工人*）执行*任务*（或者更具体地说，子任务）的数据流，以及缓冲器和交换数据*流*。

  必须始终至少有一个TaskManager。

JobManagers和TaskManagers可以通过多种方式启动：作为[独立集群](https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/deployment/cluster_setup.html)直接在计算机上，在容器中，或由[YARN](https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/deployment/yarn_setup.html)或[Mesos](https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/deployment/mesos.html)等资源框架管理。TaskManagers连接到JobManagers，宣布自己可用，并被分配工作。

该**客户端**是不运行时和程序执行的一部分，而是被用来准备和发送的数据流的JobManager。之后，客户端可以断开连接或保持连接以接收进度报告。客户端既可以作为触发执行的Java / Scala程序的一部分运行，也可以在命令行进程中运行`./bin/flink run ...`。

![执行Flink数据流所涉及的过程](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/processes.svg)

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/runtime.html#top)

## 任务槽和资源

每个worker（TaskManager）都是一个*JVM进程*，可以在不同的线程中执行一个或多个子任务。为了控制工人接受的任务数量，工人有所谓的**任务槽**（至少一个）。

每个*任务槽*代表TaskManager的固定资源子集。例如，具有三个插槽的TaskManager将其1/3的托管内存专用于每个插槽。切换资源意味着子任务不会与来自托管内存的其他作业的子任务竞争，而是具有一定量的预留托管内存。请注意，这里没有CPU隔离; 当前插槽只分离任务的托管内存。

通过调整任务槽的数量，用户可以定义子任务如何相互隔离。每个TaskManager有一个插槽意味着每个任务组在一个单独的JVM中运行（例如，可以在一个单独的容器中启动）。拥有多个插槽意味着更多子任务共享同一个JVM。同一JVM中的任务共享TCP连接（通过多路复用）和心跳消息。它们还可以共享数据集和数据结构，从而减少每任务开销。

![具有任务槽和任务的TaskManager](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/tasks_slots.svg)

默认情况下，Flink允许子任务共享插槽，即使它们是不同任务的子任务，只要它们来自同一个作业。结果是一个槽可以保存作业的整个管道。允许此*插槽共享*有两个主要好处：

- Flink集群需要与作业中使用的最高并行度一样多的任务槽。无需计算程序总共包含多少任务（具有不同的并行性）。
- 更容易获得更好的资源利用率。没有插槽共享，非密集 *源/ map（）*子任务将阻止与资源密集型*窗口*子任务一样多的资源。通过插槽共享，将示例中的基本并行性从2增加到6可以充分利用时隙资源，同时确保繁重的子任务在TaskManagers之间公平分配。

![具有共享任务槽的TaskManagers](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/slot_sharing.svg)

API还包括可用于防止不期望的时隙共享的*资源组*机制。

根据经验，一个很好的默认任务槽数就是CPU核心数。使用超线程，每个插槽然后需要2个或更多硬件线程上下文。

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/runtime.html#top)

## 州后端

存储键/值索引的确切数据结构取决于所选的[状态后端](https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/state_backends.html)。一个状态后端将数据存储在内存中的哈希映射中，另一个状态后端使用[RocksDB](http://rocksdb.org/)作为键/值存储。除了定义保存状态的数据结构之外，状态后端还实现逻辑以获取键/值状态的时间点快照，并将该快照存储为检查点的一部分。

![检查点和快照](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/checkpoints.svg)

[ 回到顶部](https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/runtime.html#top)

## 保存点

用Data Stream API编写的程序可以从**保存点**恢复执行。保存点允许更新程序和Flink群集，而不会丢失任何状态。

[保存点](https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/savepoints.html)是**手动触发的检查点**，它[捕获](https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/savepoints.html)程序的快照并将其写入状态后端。他们依靠常规的检查点机制。在执行期间，程序会定期在工作节点上创建快照并生成检查点。对于恢复，仅需要最后完成的检查点，并且一旦完成新检查点就可以安全地丢弃旧检查点。

保存点与这些定期检查点类似，不同之处在于它们**由用户触发，**并且在较新的检查点完成时**不会自动过期**。可以[从命令行](https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/cli.html#savepoints)创建保存点，也可以通过[REST API](https://ci.apache.org/projects/flink/flink-docs-release-1.8/monitoring/rest_api.html#cancel-job-with-savepoint)取消作业。