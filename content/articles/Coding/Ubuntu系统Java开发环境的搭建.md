Title:Ubuntu系统Java开发环境的搭建
Date: 2017-10-23
Tags: Ubuntu, Java

<div><font face="Times New Roman">
<p><em><font face = "Times New Roman">操作系统：Linux x64 / Ubuntu 14.04</font></em>  <br />
<em><font face = "Times New Roman">Java JDK版本：jdk-8u65-linux-x64.tar.gz</font></em>    </p>
<hr />
<p><font face = "Times New Roman">1. 前往ORACLE官网下载最新版本的Java JDK：http://www.oracle.com/technetwork/java/javase/downloads/index.html，默认下载到Downloads文件夹。</font>   </p>
<p><font face = "Times New Roman">2. 在合适的路径下创建文件夹用来存储Java JDK，本例选择在/opt目录下新建JVM子文件夹。打开Terminal（后文成为T1），输入：</font>    </p>
<div class="highlight"><pre><span></span>cd /opt                     
sudo mkdir jvm              
ls                            
cd jvm
</pre></div>


<p><font face = "Times New Roman">3.将下载的JDK压缩包拷贝到jvm目录下。新建另一个Terminal窗口（T2）并输入：</font>    </p>
<div class="highlight"><pre><span></span>cd Downloads                       
ls                         
sudo cp jdk-8u65-linux-x64.tar.gz /opt/jvm   
sudo rm jdk-8u65-linux-x64.tar.gz
</pre></div>


<p><font face = "Times New Roman">4.解压安装Java JDK，配置环境变量。回到第一个Terminal（T1），输入：</font>     </p>
<div class="highlight"><pre><span></span>ls                              
sudo tar -zxvf jdk-8u65-linux-x64.tar.gz    
ls                                 
sudo rm jdk-8u65-linux-x64.tar.gz   
sudo gedit /etc/profile
</pre></div>


<p><font face = "Times New Roman">5.配置全局环境变量。在打开的profile文档末尾添加JDK安装路径（需仔细确认）：</font></p>
<div class="highlight"><pre><span></span>#set java environment
export JAVA_HOME=/opt/jvm/jdk1.8.0_65               
export JRE_HOME=<span class="cp">${</span><span class="n">JAVA_HOME</span><span class="cp">}</span>/jre
export CLASSPATH=.:<span class="nv">$JAVA_HOME</span>/lib:<span class="nv">$JRE_HOME</span>/lib:<span class="nv">$CLASSPATH</span>
export PATH=<span class="nv">$JAVA_HOME</span>/bin:<span class="nv">$JRE_HOME</span>/bin:<span class="nv">$PATH</span>
</pre></div>


<p><font face = "Times New Roman">6.保存并关闭文档。（注：也可以通过vim 命令编辑etc/profile，打开命令：sudo vim /etc/profile，按<Insert>键进入编辑模式，<Esc>键退出编辑模式，接着按":"再输入”wq!“保存并退出；输入"q!"不保存退出）</font>    </p>
<p><font face = "Times New Roman">7.启用配置并验证。在Terminal输入：</font>    </p>
<div class="highlight"><pre><span></span>java -version
</pre></div>


<p><font face = "Times New Roman">8.显示效果类似如下：</font>    </p>
<div class="highlight"><pre><span></span>java version &quot;1.8.0_65&quot;
Java(TM) SE Runtime Environment (build 1.8.0_65-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.65-b01, mixed mode)
</pre></div>


<p><font face = "Times New Roman">（完）</font></p></font></div>