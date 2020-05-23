title: VxLAN协议详解
date: 2020-03-12
tags: VxLAN
template: carticle

[TOC]

## VxLAN简介

### 背景

任何技术的产生，都有其特定的时代背景与实际需求，VXLAN正是为了解决云计算时代虚拟化中的一系列问题而产生的一项技术。那么我们先看看 VXLAN 到底要解决哪些问题。

-  **虚拟机规模受网络设备表项规格的限制**

  对于同网段主机的通信而言，报文通过查询MAC表进行二层转发。服务器虚拟化后，数据中心中VM的数量比原有的物理机发生了数量级的增长，伴随而来的便是虚拟机网卡MAC地址数量的空前增加。一般而言，接入侧二层设备的规格较小，MAC地址表项规模已经无法满足快速增长的VM数量。

- **传统网络的隔离能力有限**

  虚拟化（虚拟机和容器）的兴起使得一个数据中心会有动辄上万的机器需要通信，而传统的 VLAN 技术在标准定义中只有12比特，也就只能支持 4096 个网络上限，已经显然满足不了不断扩展的数据中心规模。

- **虚拟机迁移范围受限**

  虚拟机迁移，顾名思义，就是将虚拟机从一个物理机迁移到另一个物理机，但是要求在迁移过程中业务不能中断。要做到这一点，需要保证虚拟机迁移前后，其IP地址、MAC地址等参数维持不变。这就决定了，虚拟机迁移必须发生在一个二层域中。而传统数据中心网络的二层域，将虚拟机迁移限制在了一个较小的局部范围内。此外，解决这个问题同时还需保证二层的广播域不会过分扩大，这也是云计算网络的要求。

传统“二层+三层”的网络在应对这些要求时变得力不从心，虽然通过很多改进型的技术比如堆叠、SVF、TRILL等可以构建物理上的大二层网络，可以将虚拟机迁移的范围扩大。但是，构建物理上的大二层，难免需要对原来的网络做大的改动，并且大二层网络的范围依然会受到种种条件的限制。

为了解决这些问题，有很多方案被提出来，VxLAN就是其中之一。VxLAN 是 VMware、Cisco 等一众大型企业共同推出的，目前标准文档在 [RFC7348](https://tools.ietf.org/html/rfc7348)。

### 定义

在介绍完VxLAN要解决的问题也就是技术背景之后，接下来正式阐述一下VxLAN的定义，也就是它到底是什么。

VXLAN 全称是 `Virtual eXtensible Local Area Network`，虚拟可扩展的局域网。它是一种 Overlay 技术，采用L2 over L4（MAC-in-UDP）封装方式，是NVO3（Network Virtualization over Layer 3）中的一种网络虚拟化技术，将二层报文用三层协议进行封装，可实现虚拟的二层网络在三层范围内进行扩展，同时满足数据中心大二层虚拟迁移和多租户的需求。RFC7348上的介绍是这样的：



*A framework for overlaying virtualized layer 2 networks over lay 3 networks.*



### 意义

针对大二层网络，VxLAN技术的出现很好的解决了云计算时代背景下数据中心在物理网络基础设施上实施服务器虚拟化的隔离和可扩展性问题：

- 通过24比特的VNI可以支持多达16M的VXLAN段的网络隔离，对用户进行隔离和标识不再受到限制，可满足海量租户。
- 除VXLAN网络边缘设备，网络中的其他设备不需要识别虚拟机的MAC地址，减轻了设备的MAC地址学习压力，提升了设备性能。
- 通过采用MAC in UDP封装来延伸二层网络，实现了物理网络和虚拟网络解耦，租户可以规划自己的虚拟网络，不需要考虑物理网络IP地址和广播域的限制，大大降低了网络管理的难度。



## VxLAN组网模型

VxLAN主要用于数据中心网络。VxLAN技术将已有的三层物理网络作为Underlay网络，在其上构建出虚拟的二层网络，即Overlay网络。Overlay网络通过Mac-in-UDP封装技术、利用Underlay网络提供的三层转发路径，实现租户二层报文跨越三层网络在不同的站点间传递。对于租户来说，Underlay网络是透明的，同一租户的不同站点就像是工作在一个局域网中。同时，在同一个物理网络上可以构建多个VxLAN网络，每个VxLAN网络由唯一的VNI标识，不同VxLAN之间互不影响，从而实现租户网络之间的隔离。

<img src="https://heriam.coding.net/api/share/download/3b7a1d98-ef3f-466b-8653-fc85c6c02c96" onerror="this.src='http://img.wandouip.com/crawler/article/2019420/83ab2b8df3af8e5e148a9cd4c4d63491';this.onerror=null"/>

如上图所示，VxLAN的典型网络模型中主要包含以下几个基本元素：

- VM (Virtual Machine): 虚拟机。在一台服务器上可以创建多台虚拟机，不同的虚拟机可以属于不同的 VXLAN。处于相同VxLAN的虚拟机处于同一个逻辑二层网络，彼此之间二层互通；属于不同VxLAN的虚拟机之间二层隔离。
- VxLAN Tunnel: VxLAN隧道。“隧道”是一个逻辑上的概念，它并不新鲜，比如大家熟悉的GRE。说白了就是将原始报文“变身”下，加以“包装”，好让它可以在承载网络（比如IP网络）上传输。从主机的角度看，就好像原始报文的起点和终点之间，有一条直通的链路一样。而这个看起来直通的链路，就是“隧道”。顾名思义，“VXLAN隧道”便是用来传输经过VXLAN封装的报文的，它是建立在两个VTEP之间的一条虚拟通道。Vxlan 通信双方（图中的虚拟机）认为自己是通过二层VSI直接通信，并不知道底层网络的存在。
- VTEP (VxLAN Tunnel Endpoints): VXLAN隧道端点。VXLAN网络的边缘设备，是VXLAN隧道的起点和终点，VXLAN报文的封装和解封装处理均在这上面进行。VTEP可以理解为Overlay网络立足于Underlay物理网络之上的支脚点，分配有物理网络的IP地址，该地址与虚拟网络无关。VXLAN报文中源IP地址为隧道一端节点的VTEP地址，目的IP地址为隧道另一端节点的VTEP地址，一对VTEP地址就对应着一个VXLAN隧道。VTEP 可以是一个独立的网络设备（比如交换机），也可以是一台物理服务器（比如虚拟机所在的宿主机）。
- VNI (VXLAN Network Identifier): VXLAN 网络标识符。以太网数据帧中VLAN只占了12比特的空间，这使得VLAN的隔离能力在数据中心网络中力不从心。而VNI的出现，就是专门解决这个问题的。VNI是一种类似于VLAN ID的用户标示，一个VNI代表了一个租户，即使多个终端用户属于同一个VNI，也表示一个租户。VNI
  由24比特组成，支持多达16M的租户。属于不同VNI的虚拟机之间不能直接进行二层通信。VXLAN报文封装时，给VNI分配了足够的空间使其可以支持海量租户的隔离。
- IP核心设备/隧道中间设备: 网络中普通的路由/转发设备，不参与VxLAN处理，仅需根据封装后的VxLAN报文的目的VTEP IP地址沿着VxLAN隧道路径进行普通的三层转发。
- VSI (Virtual Switch Instance): 虚拟交换实例。VTEP上为每个VxLAN提供二层交换服务的虚拟交换实例。VSI可以看做是VTEP上的一台针对某个VxLAN内的数据帧进行二层转发的虚拟交换机，它具有传统以太网交换机的所有功能，包括源MAC地址学习、MAC地址老化、泛洪等。VSI与VxLAN一一对应。
- VSI-Interface: VSI的虚拟三层接口。类似于Vlan-Interface，用来处理跨VNI即跨VXLAN的流量。VSI-Interface与VSI一一对应，在没有跨VNI流量时可以没有VSI-Interface。



## VxLAN报文格式

VXLAN是MAC in UDP的网络虚拟化技术，所以其报文封装是在原始以太报文之前添加了一个UDP头及VXLAN头封装：VTEP会将VM发出的原始报文封装成一个新的UDP报文，并使用物理网络的IP和MAC地址作为外层头，对网络中的其他设备只表现为封装后的参数。也就是说，网络中的其他设备看不到VM发送的原始报文。

如果服务器作为VTEP，那从服务器发送到接入设备的报文便是经过封装后的报文，这样，接入设备就不需要学习VM的MAC地址了，它只需要根据外层封装的报文头负责基本的三层转发就可以了。因此，虚拟机规模就不会受网络设备表项规格的限制了。

当然，如果网络设备作为VTEP，它还是需要学习VM的MAC地址。但是，从对报文进行封装的角度来说，网络设备的性能还是要比服务器强很多。

下图是 VxLAN 协议的报文，白色的部分是虚拟机发出的原始报文（二层帧，包含了 MAC 头部、IP 头部和传输层头部的报文），前面加了VxLAN 头部用来专门保存 VxLAN 相关的内容，再前面是标准的 UDP 协议头部（UDP 头部、IP 头部和 MAC 头部）用来在物理网路上传输报文。

从这个报文中可以看到三个部分：

1. 最外层的 UDP 协议报文用来在底层物理网络上传输，也就是 VTEP 之间互相通信的基础；
2. 中间是 VXLAN 头部，VTEP 接受到报文之后，去除前面的 UDP 协议部分，根据这部分来处理 VxLAN 的逻辑，主要是根据 VNI 发送到最终的虚拟机；
3. 最里面是原始的二层帧，也就是虚拟机所见的报文内容。

<img src="https://Heriam.coding.net/api/share/download/ad57c0e1-1648-4a4c-a8a1-e0c2f2f41e2a" onerror="this.src='https://download.huawei.com/mdl/imgDownload?uuid=83046341c6764fcf82b688857ec9e8d7.png';this.onerror=null"/>

VxLAN报文各个部分解释如下：

- Outer Ethernet/MAC Header: 外层以太头。14字节，如果有VLAN TAG则为18字节。
  - SA：发送报文的虚拟机所属VTEP的MAC地址。
  - DA：到达目的VTEP的路径上下一跳设备的MAC地址。
  - VLAN Type：可选字段，当报文中携带VLAN Tag时，该字段取值为0x8100。
  - Ethernet Type：以太报文类型，IP协议报文该字段取值为0x0800。
- Outer IP Header: 外层IP头。20字节。其中，源IP地址（Outer Src. IP）为源VM所属VTEP的IP地址，目的IP地址（Outer Dst. IP）为目的VM所属VTEP的IP地址。IP协议号（Protocol）为17（0x11），指示内层封装的是UDP报文。

- Outer UDP Header: 外层UDP头。8字节。其中，UDP目的端口号（UDP Destination Port）固定为4789，指示内层封装报文为VxLAN报文。UDP源端口号（UDP Source Port）为原始以太帧通过哈希算法计算后的随机任意值，可以用于VxLAN网络VTEP节点之间ECMP负载均衡。
- VxLAN Header: VxLAN头。8字节。
  - Flags: 8比特，RRRRIRRR。“I”位为1时，表示VXLAN头中的VXLAN ID有效；为0，表示VXLAN ID无效。“R”位保留未用，设置为0。
  - VxLAN ID (VNI): 24比特，用于标识一个单独的VXLAN网络。这也是 VxLAN 能支持千万租户的地方。
  - Reserved: 两个保留字段，分别为24比特和8比特。
- Original L2 Frame: 原始以太网报文。

从报文的封装可以看出，VXLAN头和原始二层报文是作为UDP报文的载荷存在的。在VTEP之间的网络设备，只需要根据Outer MAC Header和Outer IP Header进行转发，利用UDP Source Port进行负载分担，这一过程，与转发普通的IP报文完全相同。这样，除了VTEP设备，现网的大量设备无需更换或升级即可支持VXLAN网络。

VxLAN协议比原始报文多出50字节的内容，这会降低网络链路传输有效数据的比例。此外，新增加的VXLAN报文封装也引入了一个问题，即MTU值的设置。一般来说，虚拟机的默认MTU为1500 Bytes，也就是说原始以太网报文最大为1500字节。这个报文在经过VTEP时，会封装上50字节的新报文头（VXLAN头8字节+UDP头8字节+外部IP头20字节+外部MAC头14字节），这样一来，整个报文长度达到了1550字节。而现有的VTEP设备，一般在解封装VXLAN报文时，要求VXLAN报文不能被分片，否则无法正确解封装。这就要求VTEP之间的所有网络设备的MTU最小为 1550字节。如果中间设备的MTU值不方便进行更改，那么设置虚拟机的MTU值为1450，也可以暂时解决这个问题。

VxLAN头部最重要的是VNID字段，其他的保留字段主要是为了未来的扩展，很多厂商都会加以运用来实现自己组网的一些特性。



## VxLAN运行机制

### 隧道建立

网络中存在多个VTEP，那么这其中哪些VTEP间需要建立VXLAN隧道呢？如前所述，通过VXLAN隧道，“二层域”可以突破物理上的界限，实现大二层网络中VM之间的通信。所以，连接在不同VTEP上的VM之间如果有“大二层”互通的需求，这两个VTEP之间就需要建立VXLAN隧道。换言之，同一大二层域内的VTEP之间都需要建立VXLAN隧道。

一般而言，隧道的建立不外乎手工方式和自动方式两种。

####手工方式

这种方式需要用户手动指定VXLAN隧道的源和目的IP地址分别为本端和对端VTEP的IP地址，也就是人为的在本端VTEP和对端VTEP之间建立静态VXLAN隧道。以华为CE系列交换机为例，以上配置是在NVE（Network Virtualization Edge）接口下完成的。配置过程如下：

```reStructuredText
#
interface Nve1   //创建逻辑接口NVE 1
 source 1.1.1.1   //配置源VTEP的IP地址（推荐使用Loopback接口的IP地址）
 vni 5000 head-end peer-list 2.2.2.2  
 vni 5000 head-end peer-list 2.2.2.3   
#
```

其中，vni 5000 head-end peer-list 2.2.2.2和vni 5000 head-end peer-list 2.2.2.3的配置，表示属于VNI 5000的对端VTEP有两个，IP地址分别为2.2.2.2和2.2.2.3。根据这两条配置，VTEP上会生成如下所示的一张表：

```reStructuredText
<HUAWEI> display vxlan vni 5000 verbose
    BD ID                  : 10
    State                  : up
    NVE                     : 288
    Source                 : 1.1.1.1
    UDP Port               : 4789
    BUM Mode               : head-end
    Group Address         : - 
    Peer List              : 2.2.2.2 2.2.2.3 
```

根据上表中的Peer List，本端VTEP就可以知道属于同一VNI的对端VTEP都有哪些，这也就决定了同一大二层广播域的范围。当VTEP收到BUM（Broadcast&Unknown-unicast&Multicast，广播&未知单播&组播）报文时，会将报文复制并发送给Peer List中所列的所有对端VTEP（这就好比广播报文在VLAN内广播）。因此，这张表也被称为“头端复制列表”。当VTEP收到已知单播报文时，会根据VTEP上的MAC表来确定报文要从哪条VXLAN隧道走。而此时Peer List中所列的对端，则充当了MAC表中“出接口”的角色。在后面的报文转发流程中，你将会看到头端复制列表是如何在VXLAN网络中指导报文进行转发的。

####自动方式

自动方式下VXLAN隧道的建立需要借助于其他的协议，例如通过BGP/EVPN(Ethernet Virtual Private Network)或ENDP(Enhanced Neighbor Discovery Protocol)发现远端VTEP后，自动在本端和远端VTEP之间建立VXLAN隧道。

### 二层MAC学习

通过上节的内容，我们大致了解 VxLAN 报文的发送过程。概括地说就是虚拟机的报文通过 VTEP 添加上 VxLAN 以及外部的UDP/IP报文头，然后发送出去，对方 VTEP 收到之后拆除 VxLAN 头部然后根据 VNI 把原始报文发送到目的虚拟机。

这个过程是双方已经知道所有通信所需信息的情况下的转发流程，但是在第一次通信之前还有很多问题有解决：

- VTEP是如何对报文进行封装？
- 发送方虚拟机怎么知道对方的 MAC 地址？
- VTEP怎么知道目的虚拟机在哪一台宿主机上？

要回答这些问题，我们还是回到 VxLAN 协议报文上，看看一个完整的 VxLAN 报文需要哪些信息。

- 内层报文：通信的虚拟机双方要么直接使用 IP 地址，要么通过 DNS 等方式已经获取了对方的 IP 地址。因此网络层的源和目的地址已经知道。同一个网络的虚拟机需要通信，还需要知道对方虚拟机的 MAC 地址，**VxLAN需要一个机制来实现类似传统网络 ARP 的功能**。
- VxLAN 头部：只需要知道 VNI，这一般是直接配置在 VTEP 上的，要么是提前规划固定的，要么是根据内部报文自动生成的，也不需要担心。
- UDP 头部：最重要的是源端口和目的端口，源端口是系统生成并管理的，目的端口也是固定的，比如 IANA 规定的 4789 端口，这部分也不需要担心。
- 外层IP头部：外层IP头部关心的是隧道两端VTEP的IP地址，源地址可以很简单确定，目的地址是**目的虚拟机所在宿主机关联的VTEP IP 地址**，这个也需要由某种方式来确定。
- 外层MAC头部：如果目的VTEP 的 IP 地址确定了，根据路由表查找到下一跳的MAC 地址可以通过经典的 ARP 方式来获取，毕竟 VTEP 网络在同一个三层，经典网络架构那一套就能直接用了。

总结一下，一个 VxLAN 报文需要确定两个地址信息：目的虚拟机的 MAC 地址和目的 VTEP 的 IP 地址，如果 VNI 也是动态感知的，那么 VTEP 就需要一个三元组：

**(内层目的虚机MAC, VNI, 外层目的VTEP IP)**

组成为控制平面的表来记录对端地址可达情况。VXLAN有着与传统以太网非常相似的MAC学习机制，当VTEP接收到VXLAN报文后，会记录源VTEP的IP、虚拟机MAC和VNI到本地MAC表中，这样当VTEP接收到目的MAC为此虚拟机的MAC时，就可以进行VXLAN封装并转发。VXLAN学习地址的时候仍然保存着二层协议的特征，节点之间不会周期性的交换各自的转发表。对于不认识的MAC地址，VXLAN一般依靠组播或控制中心来获取路径信息。组播的概念是同个 VxLAN 网络的 VTEP 加入到同一个组播网络，如果需要知道以上信息，就在组内发送多播来查询；控制中心的概念是在某个集中式的地方保存了所有虚拟机的上述信息，自动化告知 VTEP 它需要的信息。

####组播方式

每个多播组对应一个多播IP地址，vtep 建立的时候会通过配置加入到多播组（具体做法取决于实现），往这个多播IP地址发送的报文会发给多播组的所有主机。为什么要使用多播？因为vxlan的底层网络是三层的，广播地址无法穿越三层网络，要给vxlan 网络所有vtep发送报文只能通过多播。 通过组播的方式承载ARP的广播报文可以实现整个VxLAN网络下的地址解析以及VSI的MAC地址学习，在这个过程中，只需要有一次多播，因为VTEP有自动学习的能力，后续的报文都是通过单播直接发送的。也可以看到，多播报文非常浪费，每次的多播其实只有一个报文是有效的，如果某个多播组的 vtep 数量很多，这个浪费是非常大的。但是多播组也有它的实现起来比较简单，不需要中心化的控制，只要底层网络支持多播，只需配置好多播组就能自动发现了。因为并不是所有的网络设备都支持多播，再加上多播方式带来的报文浪费，在实际生产中这种方式很少用到。综上，VXLAN和传统VLAN网络数据平面一样，数据经过未知单播泛洪->MAC表项及ARP表项建立->单播转发的过程，我们称之为自学习模式。但自学习方式过于简单，其大量的泛洪报文以及无法智能调整的缺点，使得这样的控制平面构建方式不适合SDN网络。

<img src="https://Heriam.coding.net/api/share/download/a07e6d26-fd6b-438b-9ae3-b83469d61ee5" onerror="this.src='https://download.huawei.com/mdl/imgDownload?uuid=2ece2b33a14841f0bc23ac79e18934fb.png';this.onerror=null"/>

####控制器方式

VTEP发送报文最关键的就是知道对方虚拟机的 MAC 地址和虚拟机所在主机的 VTEP IP 地址，如果实现知道这两个信息，那么就不需要多播了。SDN最大的特点就是转控分离，集中控制。按照这个指导思想，将控制功能单独剥离出来成为一个单独的设备便是很自然的事了。这个设备就是 Controller。Controller可以是一个或者一组硬件设备，也可以是一套软件。Controller与网络中所有设备建立连接，整个VXLAN网络的数据转发都由Controller来管理。Controller与设备连接的接口称为南向接口，可以使用OpenFlow、Netconf等协议；对用户提供服务的接口称为北向接口，也可以提供API以便与其他管理平台对接或进行深度开发。基于Controller的南向接口，可以通过OpenFlow或OVSDB协议的方式向VTEP设备下发远端MAC地址表项。具体不在这里进行展开讲述。

<img src="https://Heriam.coding.net/api/share/download/e450606f-05c2-4a06-a0b8-38e1b9479a0f" onerror="this.src='https://pic1.zhimg.com/80/v2-1418f38fb92e6feab3287dd174317e94_1440w.jpg';this.onerror=null"/>

### BUM报文转发

前面描述的报文转发过程都是已知单播报文转发，如果VTEP收到一个未知地址的BUM报文如何处理呢。与传统以太网BUM报文转发类似，VTEP会通过泛洪的方式转发流量。BUM（Broadcast, Unknown-unicast, Multicast）即广播、未知单播、组播流量。根据对泛洪流量的复制方式不同可分为单播路由方式（头端复制）和组播路由方式（核心复制）两种。

#### 单播路由方式泛洪（头端复制）

在头端复制方式下，VTEP负责复制报文，采用单播方式将复制后的报文通过本地接口发送给本地站点，并通过VXLAN隧道发送给VXLAN内的所有远端VTEP。

如下图所示，当VTEP 1上的VM 1发出BUM报文后，VTEP 1判断数据所属的VXLAN，通过该VXLAN内所有本地接口和VXLAN Tunnel转发报文。通过VXLAN Tunnel转发报文时，封装VXLAN头、UDP头和IP头，将泛洪报文封装于单播报文中，发送到VXLAN内的所有远端VTEP。

远端VTEP收到VXLAN报文后，解封装报文，将原始数据在本地站点的VXLAN内泛洪。为避免环路，远端VTEP从VXLAN隧道上接收到报文后，不会再将其泛洪到其他的VXLAN隧道。

<img src="https://Heriam.coding.net/api/share/download/51d6cba1-24e0-4eb5-9266-ec3f20dc5af9" onerror="this.src='https://download.huawei.com/mdl/imgDownload?uuid=7d90fdc0009f4476a0890dbb8e0392c5.png';this.onerror=null"/>



通过头端复制完成BUM报文的广播，不需要依赖组播路由协议。

#### 组播路由方式泛洪（核心复制）

组播路由方式的组网中同一个VXLAN内的所有VTEP都加入同一个组播组，利用组播路由协议（如PIM）在IP网络上为该组播建立组播转发表项，VTEP上相应生成一个组播隧道。

与头端复制方式不同，当VTEP 1上的VM 1发出BUM报文后，VTEP 1不仅在本地站点内泛洪，还会为其封装组播目的IP地址，封装后的报文根据已建立的组播转发表项转发到IP网络。

在组播报文到达IP网络中的中间设备时，该设备根据已建立的组播表项对报文进行复制并转发。

远端VTEP（VTEP 2和VTEP 3）接收到报文后，解封装报文，将原始的数据帧在本地站点的指定VXLAN泛洪。为了避免环路，远端VTEP从VXLAN隧道上接收到报文后，不会再将其泛洪到其他的VXLAN隧道。

由于泛洪流量使用了组播技术，所以整个组网中的网络设备需要支持组播路由协议（如PIM等）来建立组播路径以便组播报文转发。





## 参考文献

1. [vxlan 协议原理简介](https://cizixs.com/2017/09/25/vxlan-protocol-introduction/)
2. [华为悦读汇技术发烧友：认识VXLAN](https://forum.huawei.com/enterprise/zh/thread-334207.html)
3. [华为VxLAN技术白皮书](https://doc01.homedo.com/Files/Documents/PreparationAttachment/%E5%8D%8E%E4%B8%BA/100112539/%E5%8D%8E%E4%B8%BACloudEngine%2012800%E4%BA%A4%E6%8D%A2%E6%9C%BAVXLAN%E6%8A%80%E6%9C%AF%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)