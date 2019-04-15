Title: Ubuntu系统Apache Maven安装
Date: 2017-10-24
Tags: Ubuntu, Maven

<div><font face="Times New Roman">
<p><em><font face = "Times New Roman">操作系统：Linux x64 / Ubuntu 14.04</font></em>
<em><font face = "Times New Roman">Apache Maven版本：3.3.9</font></em>  <br />
<em><font face = "Times New Roman">建议预先搭建Java开发环境：详见<a href="https://jiang-hao.com/articles/2017/coding-Ubuntu%E7%B3%BB%E7%BB%9FJava%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E7%9A%84%E6%90%AD%E5%BB%BA.html">《Linux Ubuntu系统下Java开发环境搭建》</a></font></em></p>
<hr />
<p><font face = "Times New Roman">1. 前往Apache Maven官网下载最新版本：https://maven.apache.org/download.cgi，本文以apache-maven-3.3.9-bin.tar.gz为例。</font>    </p>
<p><font face = "Times New Roman">2. 在合适的路径下创建文件夹用来存储Maven，本例选择在/opt目录下新建MVN子文件夹。打开Terminal（后文成为T1），输入：</font>    </p>
<div class="highlight"><pre><span></span>cd /opt                       #进入到opt目录
sudo mkdir mvn                #新建一个mvn文件夹
ls                            #显示成功新建的mvn文件夹
cd mvn                        #进入mvn文件夹
</pre></div>


<p><font face = "Times New Roman">3.将下载的MVN压缩包拷贝到mvn目录下。新建另一个Terminal窗口（T2）并输入：</font></p>
<div class="highlight"><pre><span></span>cd Downloads                                               #进入Downloads文件夹
ls                                                         #显示刚刚下载的MVN文件，
sudo cp apache-maven-3.3.9-bin.tar.gz /opt/mvn             #将文件拷贝到刚刚新建的mvn文件夹中(这里将“&lt; &gt;”部分替代为自己对应的MVN文件名，后同)
sudo rm apache-maven-3.3.9-bin.tar.gz                      #删除本目录下的安装包（可选）  
</pre></div>


<p><font face = "Times New Roman">4.解压安装MVN，配置环境变量。回到第一个Terminal（T1），输入：</font>  </p>
<div class="highlight"><pre><span></span>ls                                                   #显示拷贝过来的MVN安装包
sudo tar -zxvf apache-maven-3.3.9-bin.tar.gz         #将安装包解压
ls                                                   #显示解压出的MVN文件夹，以及原安装包
sudo rm apache-maven-3.3.9-bin.tar.gz                #删除原安装包
sudo gedit /etc/profile                              #打开etc目录下的profile文件
</pre></div>


<p><font face = "Times New Roman">5.配置全局环境变量。在打开的profile文档末尾添加MVN安装路径（需仔细确认）：</font>  </p>
<div class="highlight"><pre><span></span>#set maven environment
export M2_HOME=/opt/mvn/apache-maven-3.3.9
export MAVEN_OPTS=&quot;-Xmx1024m&quot;                           #避免内存溢出错误（可选）
export PATH=<span class="cp">${</span><span class="n">M2_HOME</span><span class="cp">}</span>/bin:<span class="cp">${</span><span class="n">PATH</span><span class="cp">}</span>
</pre></div>


<p><font face = "Times New Roman">6.保存并关闭文档。（注：也可以通过vim 命令编辑etc/profile，打开命令：sudo vim /etc/profile，按<Insert>键进入编辑模式，<Esc>键退出编辑模式，接着按":"再输入”wq!“保存并退出；输入"q!"不保存退出）</font>     </p>
<p><font face = "Times New Roman">7.启用配置并验证。在Terminal输入：</font>    </p>
<div class="highlight"><pre><span></span>mvn -v
</pre></div>


<p><font face = "Times New Roman">8.显示效果类似如下：</font>    </p>
<div class="highlight"><pre><span></span>Apache Maven 3.3.9 (bb52d8502b132ec0a5a3f4c09453c07478323dc5; 2015-11-10T08:41:47-08:00)
Maven home: /opt/developTools/jvm/apache-maven-3.3.9
Java version: 1.8.0_65, vendor: Oracle Corporation
Java home: /opt/developTools/jvm/jdk1.8.0_65/jre
Default locale: en_US, platform encoding: UTF-8
OS name: &quot;linux&quot;, version: &quot;3.19.0-25-generic&quot;, arch: &quot;amd64&quot;, family: &quot;unix&quot;
</pre></div>


<p><font face = "Times New Roman">（完）</font></p></font></div>

