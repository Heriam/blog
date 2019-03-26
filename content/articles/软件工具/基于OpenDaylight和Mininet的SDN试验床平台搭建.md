Title: 基于OpenDaylight和Mininet的SDN试验床平台搭建
Date: 2016-07-01
Tags: OpenDaylight, Mininet, SDN

<div><font face="Times New Roman">
<p><strong>整体架构：</strong>  </p>
<hr />
<p><img alt="" src="http://img.blog.csdn.net/20151228064819181" /></p>
<hr />
<p><strong>一、虚拟机安装和镜像加载</strong>
<font size=2><em>本部分过程非常简单，所以不详细描述，基本流程稍微提一下。</em>  </font>      </p>
<hr />
<p>1.虚拟机软件：安装虚拟机软件主要有VMware Station, VirtualBox等，后者免费，下载网址为：<a href="https://www.virtualbox.org/wiki/Downloads">https://www.virtualbox.org/wiki/Downloads</a>，本文以VMware Station为例。请自行下载安装，这里不多做赘述。        </p>
<hr />
<p>2.Ubuntu系统加载：到<a href="http://www.ubuntu.com/">Ubuntu官网</a>下载自身操作系统对应的最新版Ubuntu桌面镜像，通过VMware加载Ubuntu镜像。</p>
<hr />
<p>3.Mininet VM加载：到Mininet官网：<a href="http://mininet.org/vm-setup-notes/">http://mininet.org/vm-setup-notes/</a>下载镜像文件（打开网页后有相关指南，可以参照其进行加载安装，懒得看英文的话就只用先把Mininet镜像导入VMware，不用启动，后文会对这里接下来的操作进行详述）。</p>
<hr />
<p>4.最后Ubuntu部分的相关配置参数如下图，Mininet的导入不需要进行任何参数配置，至少在启动前不用。
<img alt="" src="http://img.blog.csdn.net/20151228070342639" /></p>
<hr />
<p><strong>二、Ubuntu系统下OpenDaylight安装</strong>
<font size=2><em>本部分操作比较多，因此针对每一步都另文给出详细步骤：</em></font></p>
<hr />
<p>1.Ubuntu系统中搭建Java开发环境：<a href="http://www.hao-jiang.com/pages/operating-systems/javaenvironment.html">《Linux Ubuntu系统下Java开发环境搭建》</a> <br />
<br>
2.Ubuntu系统中安装Apache Maven：<a href="http://www.hao-jiang.com/pages/operating-systems/mavenenvironment.html">《Linux Ubuntu系统下Apache Maven的安装和配置》</a> <br />
<br>
3.Ubuntu系统中安装OpenDaylight：<a href="http://www.hao-jiang.com/pages/software-defined-networks/   InstallOpenDaylight.html">《Build and Install OpenDaylight on Ubuntu(含中文版)》</a>   </p>
<hr />
<p><strong>三、OpenDaylight功能组件安装和调试</strong>    </p>
<p><font size=2>*本部分解决OpenDaylight控制器和Mininet的连接，并且通过OpenDaylight DLUX的Web GUI显示。</font>    </p>
<p><font size=2>*本部分基于上文步骤全部完成，已经搭建了一个初步装好OpenDaylight的Ubuntu虚拟机。</font>      </p>
<p><font size=2>*下文用ODL指代OpenDaylight。</font>    </p>
<hr />
<p>1.一键启动控制器：ODL每次启动controller需要cd目录十分麻烦。这里同样可以自己写一个启动脚本来管理ODL控制器的运行：    </p>
<div class="highlight"><pre><span></span><span class="k">vim</span> odl
<span class="p">&lt;</span>Insert<span class="p">&gt;</span>
#<span class="p">!</span><span class="sr">/bin/</span>bash
<span class="sr">/home/</span><span class="p">&lt;</span>usrname<span class="p">&gt;</span><span class="sr">/developApps/</span>openDayLight<span class="sr">/integration/</span>distributions<span class="sr">/karaf/</span>target<span class="sr">/assembly/</span><span class="nb">bin</span>/karaf
<span class="p">&lt;</span>Esc<span class="p">&gt;</span>
<span class="p">:</span><span class="k">wq</span><span class="p">!</span>
sudo mv odl <span class="sr">/usr/</span>local/<span class="nb">bin</span>
sudo chmod <span class="m">755</span> <span class="sr">/usr/</span>local<span class="sr">/bin/</span>odl
</pre></div>


<p>*这样在任何地方都只用输入odl就可以运行控制器了。    </p>
<hr />
<p>2.现在就可以输入odl命令来启动控制器了，先进入如下界面：    <br />
<img alt="" src="http://img.blog.csdn.net/20151228190159338?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" /></p>
<hr />
<p>3.然后开始安装OpenDaylight的Features：     </p>
<p>＊安装支持REST API的组件：   </p>
<div class="highlight"><pre><span></span><span class="n">feature</span><span class="o">:</span><span class="n">install</span> <span class="n">odl</span><span class="o">-</span><span class="n">restconf</span>
</pre></div>


<p>＊安装L2 switch和OpenFlow插件：   </p>
<div class="highlight"><pre><span></span><span class="n">feature</span><span class="o">:</span><span class="n">install</span> <span class="n">odl</span><span class="o">-</span><span class="n">l2switch</span><span class="o">-</span><span class="k">switch</span>

<span class="n">feature</span><span class="o">:</span><span class="n">install</span> <span class="n">odl</span><span class="o">-</span><span class="n">openflowplugin</span><span class="o">-</span><span class="n">all</span>
</pre></div>


<p>＊安装基于karaf控制台的md-sal控制器功能，包括nodes、yang UI、Topology：   </p>
<div class="highlight"><pre><span></span><span class="n">feature</span><span class="o">:</span><span class="n">install</span> <span class="n">odl</span><span class="o">-</span><span class="n">mdsal</span><span class="o">-</span><span class="n">apidocs</span>    
</pre></div>


<p>＊安装DLUX功能：   </p>
<div class="highlight"><pre><span></span><span class="n">feature</span><span class="o">:</span><span class="n">install</span> <span class="n">odl</span><span class="o">-</span><span class="n">dlux</span><span class="o">-</span><span class="n">all</span>
</pre></div>


<p>＊安装基于karaf控制台的ad-sal功能，包括Connection manager、Container、Network、Flows：</p>
<div class="highlight"><pre><span></span><span class="n">feature</span><span class="o">:</span><span class="n">install</span> <span class="n">odl</span><span class="o">-</span><span class="n">adsal</span><span class="o">-</span><span class="n">northbound</span>
</pre></div>


<ul>
<li>注意：请按照一定的顺序安装，安装顺序不合理的话，会导致后面Web界面无法访问！且记录遇到的一个问题：在没有按照顺序安装组件的情况下，无法登录进入ODL主界面。解决方法是通过logout退出karaf平台，进入上级目录，删除data目录：rm –r data，进入bin目录：cd bin，执行./karaf clean，再次重复上面的安装组件操作。    </li>
</ul>
<hr />
<p>＊Features 查看确认：可以通过<code>feature:list</code> 加上其它关键字来获取相关feature信息：    </p>
<div class="highlight"><pre><span></span><span class="n">feature</span><span class="o">:</span><span class="n">list</span>              <span class="err">#</span> <span class="n">show</span> <span class="n">the</span> <span class="n">list</span> <span class="n">of</span> <span class="n">all</span> <span class="n">available</span> <span class="n">features</span> <span class="n">of</span> <span class="n">controller</span>
<span class="n">feature</span><span class="o">:</span><span class="n">list</span> <span class="o">-</span><span class="n">i</span>           <span class="err">#</span> <span class="n">show</span> <span class="n">all</span> <span class="n">features</span> <span class="n">that</span> <span class="n">have</span> <span class="n">already</span> <span class="n">been</span> <span class="n">installed</span>
<span class="n">feature</span><span class="o">:</span><span class="n">list</span> <span class="o">|</span> <span class="n">grep</span> <span class="o">&lt;</span><span class="n">keyword</span><span class="o">&gt;</span>     <span class="err">#</span> <span class="n">show</span> <span class="n">features</span> <span class="n">that</span> <span class="n">contain</span> <span class="o">&lt;</span><span class="n">keyword</span><span class="o">&gt;</span>
</pre></div>


<hr />
<p>4.Web界面访问：此时可以登录ODL的Web UI界面进行访问。用浏览器访问网址：<a href="http://localhost:8181/dlux/index.html">http://ODL的IP:8181/dlux/index.html</a>，<code>&lt;ODL_IP&gt;</code>为安装ODL所在的主机IP地址，特别注意的是此版本的ODL访问端口为8181，因8080端口被karaf控制台进程所占用。某些情况下不需要进入/dlux目录而直接访问http://ODL的IP:8181/index.html。     </p>
<ul>
<li>By accessing "<a href="http://localhost:8181/apidoc/explorer/index.html">http://localhost:8181/apidoc/explorer/index.html</a>" you can have the list of all the available APIs exposed on the northbound.(获取北向接口文档)       </li>
</ul>
<hr />
<p>5.网页打开后，登陆用户名为admin，密码为admin，如下图：   <br />
<img alt="" src="http://img.blog.csdn.net/20151228192434519" /></p>
<ul>
<li>
<p>关于Features出问题，可以vim查看<code>/developApps/openDayLight/integration/distributions/karaf/target/assembly/etc</code>目录下的<code>org.apache.karaf.features.cfg</code>    </p>
</li>
<li>
<p>由于还没有连接数据面Mininet的交换机，因此登陆进去后还不会显示任何拓扑。   </p>
</li>
</ul>
<hr />
<p><strong>四、Mininet虚拟机的安装和登录调试</strong>
<font size=2>本部分接着第一部分下载好Mininet镜像后，解决Mininet导入虚拟机后的加载配置并重点阐述远程免密码自动登录的设置。</font></p>
<hr />
<p>1.在虚拟机成功导入.OVF后缀的mininet文件后，直接启动。    </p>
<hr />
<p>2.启动完成后，进入到登录界面，账号密码都是mininet（注意密码敲了不会有显示很正常，敲完再敲回车就行）。</p>
<div class="highlight"><pre><span></span><span class="n">mininet</span><span class="p">-</span><span class="n">vm</span> <span class="n">login</span><span class="p">:</span> <span class="n">mininet</span>                   
<span class="n">Password</span><span class="p">:</span> <span class="n">mininet</span>
</pre></div>


<hr />
<p>3.好，重点来了，接下来说明如何从Ubuntu的虚拟机"远程"SSH登录到Mininet，这样做的目的是可以避免在两个虚拟机之间切来切去的麻烦。（如果两者分别装在不同的主机上的话就省去了“跑来跑去”的麻烦～）    </p>
<ul>
<li>首先，需要找到Mininet虚拟机的IP地址，一般是192.168.x.y格式的地址。在Mininet的命令行界面输入：   <code>ifconfig eth0</code>    </li>
<li>如果你不希望每次从Ubuntu虚拟机SSH登录Mininet的时候都输一遍这个 IP地址，可以在Ubuntu虚拟机端修改一下/etc/hosts文件：<code>sudo gedit /etc/hosts</code>，然后在文档末尾添加以下内容后保存退出：<code>192.168.x.y minivm</code>。这样就可以在每次登陆的时候用“minivm”代替IP地址。    </li>
<li>接下来就可以从Ubuntu虚拟机端SSH到Mininet了。在Ubuntu端终端输入以下命令（没有修改hosts文件的话就用mininet的IP地址代替minivm）：<code>ssh -Y mininet@minivm</code>     </li>
<li>登陆后输入账号mininet密码mininet，就到了Mininet的命令行界面了。</li>
</ul>
<hr />
<p>4.（可选）写脚本一键SSH免密码自动登录Mininet。每次都要手动敲命令还要输入账号密码登陆Mininet稍显麻烦，我们还可以做出如下简化：  <br />
<br>
<strong>设置免密码登陆：</strong>
<em> 在Ubuntu端check一下是否已经有SSH密钥： <code>~/.ssh/id_rsa</code>  或者 <code>~/.ssh/id_dsa</code>  <br />
</em> 如果都不能找到任何文件的话，那么就需要通过命令生成SSH密钥，在Ubuntu端：<code>ssh-keygen -t rsa</code> <br />
<em> 为了加快以后SSH连接的速度，需要将你的公钥添加给Mininet端。同样在Ubuntu端：<code>scp ~/.ssh/id_rsa.pub mininet@minivm:~/</code>  <br />
</em>  最后，在Ubuntu端先通过SSH登陆进Mininet，再在Mininet命令行模式下输入：    </p>
<div class="highlight"><pre><span></span><span class="n">cd</span> <span class="p">~/</span> <span class="p">&amp;&amp;</span> <span class="n">mkdir</span> <span class="p">-</span><span class="n">p</span> <span class="p">.</span><span class="n">ssh</span> <span class="p">&amp;&amp;</span> <span class="n">chmod</span> <span class="m">700</span> <span class="p">.</span><span class="n">ssh</span> <span class="p">&amp;&amp;</span> <span class="n">cd</span> <span class="p">.</span><span class="n">ssh</span> <span class="p">&amp;&amp;</span> <span class="n">touch</span> <span class="n">authorized_keys2</span> <span class="p">&amp;&amp;</span> <span class="n">chmod</span> <span class="m">600</span> <span class="n">authorized_keys2</span> <span class="p">&amp;&amp;</span> <span class="n">cat</span> <span class="p">../</span><span class="n">id_rsa</span><span class="p">.</span><span class="n">pub</span> <span class="p">&gt;&gt;</span> <span class="n">authorized_keys2</span> <span class="p">&amp;&amp;</span> <span class="n">rm</span> <span class="p">../</span><span class="n">id_rsa</span><span class="p">.</span><span class="n">pub</span> <span class="p">&amp;&amp;</span> <span class="n">cd</span> <span class="p">..</span>
</pre></div>


<ul>
<li>操作完成后，以后每次登陆就不必输入账号密码了。    </li>
</ul>
<p><br>
<strong>写一键登陆脚本：</strong>
* 嫌输命令麻烦的童鞋还可以继续写一个脚本，输入：（其中&lt;&gt;表示按键）    </p>
  <div class="highlight"><pre><span></span><span class="k">vim</span> mininet
    <span class="p">&lt;</span>Insert<span class="p">&gt;</span>（在文档内添加以下内容）
    <span class="p">!</span>#<span class="sr">/bin/</span>bash
    ssh <span class="p">-</span>Y mininet@minivm
    <span class="p">&lt;</span>Esc<span class="p">&gt;</span>
    :<span class="k">wq</span><span class="p">!</span>
    sudo mv mininet <span class="sr">/usr/</span>local/<span class="nb">bin</span>
    sudo chmod <span class="m">755</span> <span class="sr">/usr/</span>local<span class="sr">/bin/</span>mininet
  </pre></div>


<ul>
<li>这样以后在Ubuntu端每次只用通过mininet命令来一键登陆Mininet。    </li>
</ul>
<hr />
<p><strong>五、OpenDaylight+Mininet联动</strong>
<font size=2>本部分测试ODL和Mininet的连接，初步搭建好一个SDN试验床。</font></p>
<hr />
<p>1.启动MIninet和ODL。调试好网络连接。首先通过一端Ping另一端测试网络连通性。</p>
<hr />
<p>2.通过"minivm"命令运行脚本登陆Mininet：创建简单实验拓扑并指定远程ODL作为控制器，简单的命令可以尝试：   </p>
<div class="highlight"><pre><span></span>sudo mn --controller=remote,ip=&lt;ODL的IP&gt;
</pre></div>


<ul>
<li>完成后将输出以下内容：    </li>
</ul>
<div class="highlight"><pre><span></span>mininet@mininet-vm:~$ sudo mn --controller=remote,ip=192.168.174.128
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 
*** Adding switches:
s1 
*** Adding links:
(h1, s1) (h2, s1) 
*** Configuring hosts
h1 h2 
*** Starting controller
c0 
*** Starting 1 switches
s1 ...
*** Starting CLI:
mininet&gt;
</pre></div>


<hr />
<p>3.打开网页登陆ODL的Web界面，看到如图拓扑，联动测试完成，一个基本的基于ODL+Mininet的SDN实验平台就搭建好了！ <br />
<img alt="" src="http://img.blog.csdn.net/20151228194854049" /></p>
<p>（完）</p></font></div>