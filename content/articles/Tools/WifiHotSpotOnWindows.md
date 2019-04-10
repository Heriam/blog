Title: Windows系统配置WiFi无线热点
Date: 2017-11-21
Tags: WiFi, Windows

 <div><font face="Times New Roman"><p><font face="Times New Roman" size=3>
Windows 版本： Windows 7/8/10  <br />
前提：电脑装配无线网卡  <br />
方法：通过Dos命令行创建WiFi热点，然后启用共享  <br />
</font></p>
<hr />
<p>1.首先确定无线网卡是否支持承载网络（Hosted Network）。在管理员模式的CMD窗口输入命令：    </p>
<div class="highlight"><pre><span></span>netsh wlan show drivers
</pre></div>


<p>在输出信息中找到 “支持承载网络：是” 则继续。
<hr>2.确定电脑是否已经配置承载网络。同样在CMD窗口分别输入命令：    </p>
<div class="highlight"><pre><span></span>netsh wlan show hostednetwork
netsh wlan show hostednetwork setting=security
</pre></div>


<p>如果看到第一条命令输出已经配置好的WiFi热点的SSID，第二条输出WiFi热点的密码，直接跳到第四步。<hr></p>
<p>3.创建WiFi热点。命令行输入：    </p>
<div class="highlight"><pre><span></span>netsh wlan set hostednetwork mode=allow ssid=WiFi名称 key=WiFi密码
</pre></div>


<p>完成后提示承载网络设置成功。
<hr>4.启用WiFi热点。在命令行输入：</p>
<div class="highlight"><pre><span></span>netsh wlan start hostednetwork
</pre></div>


<p>完成后提示已启动承载网络。<hr></p>
<p>5.启用WiFi热点共享。打开 “网络和共享中心”，在窗口左边栏找到 “更改适配器设置”，再在窗口右侧找到刚刚创建的WiFi网络，一般显示为 “本地连接”，记住。如下所示  <br />
<img alt="windows wifi 热点 hotspot" src="http://7xq8q3.com1.z0.glb.clouddn.com/hostednetwork.jpg" />  <br />
<br>在以太网的网络连接图标上点击右键选择属性，在弹出的窗口上方标签栏点击 “共享”。然后在下方确认框中启用 “允许其它网络用户通过此计算机的 Internet连接来连接(N)”。如下所示，下拉框中选择刚刚创建的WiFi热点，确定，完成。  <br />
<img alt="windows wifi 热点 hotspot" src="http://7xq8q3.com1.z0.glb.clouddn.com/enablesharing.jpg" />  <br />
<br>  <br />
（完）</p></font></div>