# 事物

## 事物的定义

事务（Transaction）是由一系列对系统中数据进行访问或更新的操作所组成的一个程序执行逻辑单元（Unit）。在计算机术语中，事务通常就是指数据库事务 。

在数据库管理系统（DBMS）中，事务是数据库恢复和并发控制的基本单位。它是一个操作序列，这些操作要么都执行，要么都不执行，它是一个不可分割的工作单位。例如，银行转帐工作：从源帐号扣款并使目标帐号增款，这两个操作必须要么全部执行，要么都不执行，否则就会出现该笔金额平白消失或出现的情况。所以，应该把他们看成一个事务。在现代数据库中，事务还可以实现其他一些事情，例如，确保你不能访问别人写了一半的数据；但是基本思想是相同的——事务是用来确保**无论发生什么情况，你使用的数据都将处于一个合理的状态**：

> transactions are there to ensure, that no matter what happens, the data you work with will be in a sensible state. 

 它保证在任何情况下都不会出现在转账后从一个帐户中扣除了资金，而未将其存入另一个帐户的情况。



##  事务的目的

数据库事务通常包含了一个序列的对数据库的读/写操作。包含有以下两个目的：

> 1. 为数据库操作序列提供了一个从失败中恢复到正常状态的方法，同时提供了数据库即使在异常状态下仍能保持一致性的方法。
> 2. 当多个应用程序在并发访问数据库时，可以在这些应用程序之间提供一个隔离方法，以防止彼此的操作互相干扰。

当事务被提交给了DBMS，则DBMS需要确保该事务中的所有操作都成功完成且其结果被永久保存在数据库中，如果事务中有的操作没有成功完成，则事务中的所有操作都需要回滚，回到事务执行前的状态；同时，该事务对数据库或者其他事务的执行无影响，所有的事务都好像在独立的运行。 

Martin Kleppmann在他的《Designing Data-Intensive Applications》一书中有提到：

> Transactions are not a law of nature; they were created with a purpose, namely to simplify the programming model for applications accessing a database. By using transactions, the application is free to ignore certain potential error scenarios and concurrency issues, because the database takes care of them instead (we call these safety guarantees).

在现实情况下，失败的风险很高。在一个数据库事务的执行过程中，有可能会遇上事务操作失败、数据库系统或操作系统出错，甚至是存储介质出错等情况。而上述Martin的话说明了事务的存在，就是为了能够简化我们的编程模型，不需要我们去考虑各种各样的潜在错误和并发问题 。我们在实际使用事务时，不需要考虑数据库宕机，网络异常，并发修改等问题，整个事务要么提交，要么回滚，非常方便。所以本质上来说，**事务的出现了是为了应用层服务的，而不是数据库系统本身的需要** 。



## 事务的ACID属性

为了保持数据库的一致性，在事务处理之前和之后，都遵循某些属性，也就是大家耳熟能详的ACID属性：

- 原子性（Atomicity）：即不可分割性，事务中的操作要么全不做，要么全做
- 一致性（Consistency）：一个事务在执行前后，数据库都必须处于一致性状态
- 隔离性（Isolation）：多个事务并发执行时，一个事务的执行不应影响其他事务的执行
- 持久性（Durability）：事务处理完成后，对数据的修改就是永久的，即便系统故障也不会丢失

并非任意的对数据库的操作序列都是数据库事务。ACID属性是一系列操作组成事务的必要条件。总体而言，ACID属性提供了一种机制，使每个事务都”作为一个单元，完成一组操作，产生一致结果，事务彼此隔离，更新永久生效“，从而来确保数据库的正确性和一致性。




# 参考文献

按引用先后顺序：

1. *Stack Overflow: [What is a database transaction?](https://stackoverflow.com/questions/974596/what-is-a-database-transaction)*
2. *Communcations and Information Processing: First International Conference, ICCIP 2012, Aveiro, Portugal, March 7-11, 2012, Proceedings, 第 2 部分*
3. *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems, 第25节*
4. 