title: OpenShift 详细教程 - 基础知识入门
date: 2019-04-19
tags: OpenShift

[TOC]

### 简介

自由和开放源码的云计算平台使开发人员能够创建、测试和运行他们的应用程序，并且可以把它们部署到云中。

OpenShift是红帽的云开发平台即服务（PaaS）。是一个基于主流的容器技术Docker和K8s构建的开源容器云平台。底层以Docker作为容器引擎驱动，以K8s作为容器编排引擎组件，并提供了开发语言，中间件，DevOps自动化流程工具和web console用户界面等元素，提供了一套完整的基于容器的应用云平台。

Openshift提供比任何PaaS更多的灵活性，它支持用于Java、Python、PHP、Perl、node.js、go和Ruby的更多的开发框架，包括 Spring、Seam、Weld、CDI、Rails、Rack、Symfony、Zend Framework、Twisted、Django和Java E。数据库语言则支持MySQL、MongoDB和PostgreSQL。

另外它还提供了多种集成开发工具如Eclipse integration，JBoss Developer Studio和 Jenkins等。

OpenShift Online服务构建在Red Hat Enterprise Linux上。Red Hat Enterprise Linux提供集成应用程序，运行库和一个配置可伸缩的多用户单实例的操作系统，以满足企业级应用的各种需求。

建立在红帽开源领导地位基础上的OpenShift旨在终结PaaS的厂商锁定，使用户可以选择自 己应用运行在哪个云提供商的云中。OpenShift将作为在线服务来提供。

OpenShift使用的架构由单个节点组成，以容纳应用程序代码和服务，同时还有一系列的单独代理来管理节点和提供服务。除此之外，OpenShift的架构还包括一个消息系统将节点和代理绑定到一起，并且使用[RESTful](https://baike.baidu.com/item/RESTful)的API同外部工具整合。

Openshift包括社区版和企业版：

- 社区版： Openshift Origin

- 企业版： Openshift Online/Openshift Enterprise

### 重要概念

system:admin为默认的集群管理员，拥有最高的权限。该用户没有密码，登陆依赖于证书密钥。

Service Account 是 Openshift 中专门供程序和组件使用的账号。不同的用户或组关联不同的角色，同时关联不同的SCC（security context constriant）安全上下文。

### 总体架构

自底而上包括几个层次：基础架构层，容器引擎层，容器编排层，PaaS服务层，界面及工具层。

- 基础架构层：为Openshift平台的运行提供基础的运行环境。Openshift支持运行在物理机，虚拟机（kvm,vmware,virtual box等），公有云（阿里云，AWS等），私有云，混合云上。

- 容器引擎层：以当前主流的Docker作为容器引擎。

- 容器编排层：以Google的k8s进行容器编排。

- PaaS服务层：容器云平台的最终目的是为上层应用服务提供支持，提高开发，测试，部署，运维的速度和效率。用户在Openshift云平台上可以快速的获取和部署一个数据库，缓存等。

- 界面及工具层：Openshift提供了多种用户的接入渠道：Web控制台，命令行，RestFul接口等。

### 核心组件

####Master节点：主控节点

**集群内的管理组件都运行在Master节点上。Master节点负责集群的配置管理，维护集群的状态。**Master节点运行的服务组件：

- API Server：负责提供Web console和RESTful API。集群内所有节点都会访问API Server，更新节点的状态及其上的容器状态。
- 数据源（Data store）：集群内所有状态信息都会存储在后端的一个etcd的分布式数据库中。
- 调度控制器（Scheduler）：负责按用户输入的要求寻找合适的计算节点。
- 复制控制器（Replication Controller）：负责监控当前容器实例的数量和用户部署指定的数量是否匹配，若有容器异常退出，复制控制器发现实际数少于部署定义数，从而触发部署新的实例。

#### Node节点：计算节点

接收Master节点的指令，运行和维护Docker容器。Master节点也可以是Node节点，只是在一般环境中，其运行容器的功能是关闭的。

#### Project

在k8s中使用命名空间来分隔资源。同一个命名空间中，某一个对象的名称在其分类中必须唯一，但在不同命名空间中的对象则可以同名。Openshift集成了k8s命名空间的概念，而且在其上定义了Project对象的概念，**每一个Project会和一个namespace相关联**。

#### Pod

在Openshift中的容器都会Pod包裹，即容器都运行在Pod内部，**一个Pod可以运行一个或多个容器，绝大多少情况下，一个Pod内部运行一个容器**。

#### Service

由于容器是一个非持久化的对象，所有对容器的修改在容器销毁后都会丢失，而且每个容器的IP地址会不断变化。k8s提供了Service组件，当部署某个应用时，会创建一个Service对象，该对象与一个或多个Pod关联，同时每个Service分配一个相对恒定的IP，通过访问该IP及相应的端口，请求就会转发到对应Pod端口。除了可通过IP，也可以通过域名访问Service，格式为：..svc.cluster.local

#### Router和Route

<u>Service提供了一个通往后端Pod集群的稳定入口，但是Service的IP地址只是集群内部的节点和容器可见。外部需通过Router（路由器）来转发。Router组件是Openshift集群中一个重要的组件，它是外界访问集群内容器应用的入口。用户可以创建Route（路由规则）对象，一个Route会与一个Service关联，并绑定一个域名。Route规则被Router加载。当集群外部的请求通过指定域名访问应用时，域名被解析并指向Router所在的计算机节点上，Router获取该请求，然后根据Route规则定义转发给与这个域名对应的Service后端所关联的Pod容器实例。上述转发流程类似于nginx。Router负责将集群外的请求转发到集群的容器，Service则负责把来自集群内部的请求转发到指定的容器中。</u>

#### Persistent Storage

容器默认是非持久化的，所有的修改在容器销毁时都会丢失。Docker提供了持久化卷挂载的能力，Openshift除了提供持久化卷挂载的能力，还提供了一种持久化供给模型即PV（Persistent Volume）和PVC（Persistent Volume Claim）。在PV和PVC模型中，集群管理员会创建大量不同大小和不同特性的PV。用户在部署应用时显式的声明对持久化的需求，创建PVC，在PVC中定义所需要的存储大小，访问方式。Openshift集群会自动寻找符合要求的PV与PVC自动对接。

#### Registry

Openshift内部的镜像仓库，主要用于存放内置的S2I构建流程所产生的镜像。

#### S2I

Source to Image，负责将应用源码构建成镜像。步骤：

1）用户输入源代码仓库的地址

2）选择S2I构建的基础镜像

3）触发构建

4）S2I构建执行器从指定的源码仓库地址下载代码

5）S2I构建执行器实例化Builder镜像，并将代码注入到Builder镜像

6）S2I构建执行器按照预定义的逻辑执行源代码的编译，构建

7）生成新的镜像

8）S2I构建执行器将新镜像Push到Registry

9）更新相关的Image Stream信息

### 核心流程

1）创建应用：用户通过web控制台或oc命令创建应用，Openshift平台根据用户输入的源码地址和Builder镜像，生成构建配置Builder config和部署配置Deployment config，Service，Route等。

2）触发构建

3）实例化构建：平台根据Builder config实例化Builder对象，下载代码，并将代码注入到Builder对象，执行编译，构建

4）生成新镜像并Push到Registry

5）更新相关的Image Stream信息

6）触发部署：当Image Stream更新后，触发平台部署镜像

7）实例化镜像部署：平台根据Deployment config实例化部署，生成Deploy对象

8）生成Replication Controller

9）部署容器：通过Replication Controller，平台将pod及容器部署到各个节点上

10）用户访问：用户通过浏览器访问Route对象中定义的应用域名

11）请求处理并返回：请求到达Router组件后，通过Route转发给相关联的Service，最终到对应的容器实例。

### 优点
支持快速部署，实现敏捷开发。

提供动态伸缩功能，将过程简化至只需更改一个值。

管理资源，为容器分配合适的资源，提高资源利用率。

有对应的平台自动化运维工具，大大减少运维负担。

在大规模集群时提供方便高效的管理方法。

有完善的结构，部署以后能快速地测试应用。

丰富的接口，提供给各种插件与二次开发使用

上手难度：是基于docker和k8s的开源项目，有丰富的社区技术支持。还有关于openshift中文参考书。
