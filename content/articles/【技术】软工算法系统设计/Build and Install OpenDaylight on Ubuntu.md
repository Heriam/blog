Title: Build and Install OpenDaylight on Ubuntu
Date: 2018-01-01
Tags: OpenDaylight, Ubuntu, SDN

<div><font face="Times New Roman">
<p><em><font face = "Times New Roman">Operating System：Linux x64 / Ubuntu 14.04</font></em>   <br />
<em><font face = "Times New Roman">Prerequisites：Linux system with Java and Maven installed</font></em>   <br />
<em><font face = "Times New Roman" color="red">Chinese version is also available at <a href="http://www.cnblogs.com/cciejh/p/opendaylight1.html">Ubuntu系统下OpenDaylight源码编译安装</a></font></em>       </p>
<hr />
<p><font face = "Times New Roman"><strong>STEP 1, Environment Tuning</strong></font></p>
<hr />
<p><font face = "Times New Roman">1. Install Git tool by command line: </font>   </p>
<div class="highlight"><pre><span></span>sudo apt-get install git-core
</pre></div>


<p><font face = "Times New Roman">2. After the installation of Java and Maven, you need to edit a very important file for OpenDaylight which is named "settings.xml". It can customize the behavior of Maven at system level. But we often choose to make it in <em>~/.m2</em> folder under your <em>home</em> directory to limit it in user scope：  <br />
(under ~/ directory)</font>    </p>
<div class="highlight"><pre><span></span>mkdir .m2                     
cp -n ~/.m2/settings.xml{,.orig} ; \wget -q -O - https://raw.githubusercontent.com/opendaylight/odlparent/master/settings.xml &gt; ~/.m2/settings.xml
</pre></div>


<p><font face = "Times New Roman">You can also use this command instead: </font>   </p>
<div class="highlight"><pre><span></span>curl https://raw.githubusercontent.com/opendaylight/odlparent/master/settings.xml --create-dirs -o ~/.m2/settings.xml
</pre></div>


<p><font face = "Times New Roman">3. A new <em>settings.xml</em> file should now appear in the folder you just created, go and check the content, which should be something similar as below：</font>    </p>
<div class="highlight"><pre><span></span># gedit ~/.m2/settings.xml
<span class="nt">&lt;settings</span> <span class="na">xmlns=</span><span class="s">&quot;http://maven.apache.org/SETTINGS/1.0.0&quot;</span>
  <span class="na">xmlns:xsi=</span><span class="s">&quot;http://www.w3.org/2001/XMLSchema-instance&quot;</span>
  <span class="na">xsi:schemaLocation=</span><span class="s">&quot;http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd&quot;</span><span class="nt">&gt;</span>

  <span class="nt">&lt;profiles&gt;</span>
    <span class="nt">&lt;profile&gt;</span>
      <span class="nt">&lt;id&gt;</span>opendaylight-release<span class="nt">&lt;/id&gt;</span>
      <span class="nt">&lt;repositories&gt;</span>
        <span class="nt">&lt;repository&gt;</span>
          <span class="nt">&lt;id&gt;</span>opendaylight-mirror<span class="nt">&lt;/id&gt;</span>
          <span class="nt">&lt;name&gt;</span>opendaylight-mirror<span class="nt">&lt;/name&gt;</span>
          <span class="nt">&lt;url&gt;</span>http://nexus.opendaylight.org/content/repositories/public/<span class="nt">&lt;/url&gt;</span>
          <span class="nt">&lt;releases&gt;</span>
            <span class="nt">&lt;enabled&gt;</span>true<span class="nt">&lt;/enabled&gt;</span>
            <span class="nt">&lt;updatePolicy&gt;</span>never<span class="nt">&lt;/updatePolicy&gt;</span>
          <span class="nt">&lt;/releases&gt;</span>
          <span class="nt">&lt;snapshots&gt;</span>
            <span class="nt">&lt;enabled&gt;</span>false<span class="nt">&lt;/enabled&gt;</span>
          <span class="nt">&lt;/snapshots&gt;</span>
        <span class="nt">&lt;/repository&gt;</span>
      <span class="nt">&lt;/repositories&gt;</span>
      <span class="nt">&lt;pluginRepositories&gt;</span>
        <span class="nt">&lt;pluginRepository&gt;</span>
          <span class="nt">&lt;id&gt;</span>opendaylight-mirror<span class="nt">&lt;/id&gt;</span>
          <span class="nt">&lt;name&gt;</span>opendaylight-mirror<span class="nt">&lt;/name&gt;</span>
          <span class="nt">&lt;url&gt;</span>http://nexus.opendaylight.org/content/repositories/public/<span class="nt">&lt;/url&gt;</span>
          <span class="nt">&lt;releases&gt;</span>
            <span class="nt">&lt;enabled&gt;</span>true<span class="nt">&lt;/enabled&gt;</span>
            <span class="nt">&lt;updatePolicy&gt;</span>never<span class="nt">&lt;/updatePolicy&gt;</span>
          <span class="nt">&lt;/releases&gt;</span>
          <span class="nt">&lt;snapshots&gt;</span>
            <span class="nt">&lt;enabled&gt;</span>false<span class="nt">&lt;/enabled&gt;</span>
          <span class="nt">&lt;/snapshots&gt;</span>
        <span class="nt">&lt;/pluginRepository&gt;</span>
      <span class="nt">&lt;/pluginRepositories&gt;</span>
    <span class="nt">&lt;/profile&gt;</span>
    
    <span class="nt">&lt;profile&gt;</span>
      <span class="nt">&lt;id&gt;</span>opendaylight-snapshots<span class="nt">&lt;/id&gt;</span>
      <span class="nt">&lt;repositories&gt;</span>
        <span class="nt">&lt;repository&gt;</span>
          <span class="nt">&lt;id&gt;</span>opendaylight-snapshot<span class="nt">&lt;/id&gt;</span>
          <span class="nt">&lt;name&gt;</span>opendaylight-snapshot<span class="nt">&lt;/name&gt;</span>
          <span class="nt">&lt;url&gt;</span>http://nexus.opendaylight.org/content/repositories/opendaylight.snapshot/<span class="nt">&lt;/url&gt;</span>
          <span class="nt">&lt;releases&gt;</span>
            <span class="nt">&lt;enabled&gt;</span>false<span class="nt">&lt;/enabled&gt;</span>
          <span class="nt">&lt;/releases&gt;</span>
          <span class="nt">&lt;snapshots&gt;</span>
            <span class="nt">&lt;enabled&gt;</span>true<span class="nt">&lt;/enabled&gt;</span>
          <span class="nt">&lt;/snapshots&gt;</span>
        <span class="nt">&lt;/repository&gt;</span>
      <span class="nt">&lt;/repositories&gt;</span>
      <span class="nt">&lt;pluginRepositories&gt;</span>
        <span class="nt">&lt;pluginRepository&gt;</span>
          <span class="nt">&lt;id&gt;</span>opendaylight-snapshot<span class="nt">&lt;/id&gt;</span>
          <span class="nt">&lt;name&gt;</span>opendaylight-snapshot<span class="nt">&lt;/name&gt;</span>
          <span class="nt">&lt;url&gt;</span>http://nexus.opendaylight.org/content/repositories/opendaylight.snapshot/<span class="nt">&lt;/url&gt;</span>
          <span class="nt">&lt;releases&gt;</span>
            <span class="nt">&lt;enabled&gt;</span>false<span class="nt">&lt;/enabled&gt;</span>
          <span class="nt">&lt;/releases&gt;</span>
          <span class="nt">&lt;snapshots&gt;</span>
            <span class="nt">&lt;enabled&gt;</span>true<span class="nt">&lt;/enabled&gt;</span>
          <span class="nt">&lt;/snapshots&gt;</span>
        <span class="nt">&lt;/pluginRepository&gt;</span>
      <span class="nt">&lt;/pluginRepositories&gt;</span>
    <span class="nt">&lt;/profile&gt;</span>
  <span class="nt">&lt;/profiles&gt;</span>

  <span class="nt">&lt;activeProfiles&gt;</span>
    <span class="nt">&lt;activeProfile&gt;</span>opendaylight-release<span class="nt">&lt;/activeProfile&gt;</span>
    <span class="nt">&lt;activeProfile&gt;</span>opendaylight-snapshots<span class="nt">&lt;/activeProfile&gt;</span>
  <span class="nt">&lt;/activeProfiles&gt;</span>
<span class="nt">&lt;/settings&gt;</span>  
</pre></div>


<hr />
<p><font face = "Times New Roman"><strong>STEP 2, Build and Install OpenDaylight Controller Project</strong></font>    </p>
<p><font face = "Times New Roman" size=2>Please keep in mind that here controller really means core controller without many other additional features, such as WebUI(dlux). As for the development of other features in OpenDaylight and if you need dlux, please refer to next STEP.</font></p>
<hr />
<p><font face = "Times New Roman">1.Create a directory for your project and get the source code of OpenDaylight controller:</font>      </p>
<div class="highlight"><pre><span></span>mkdir openDayLight
cd openDayLight
git clone https://git.opendaylight.org/gerrit/p/controller.git
</pre></div>


<p><font face = "Times New Roman">2.Specify the version of OpenDaylight you want to build and check:</font>  </p>
<div class="highlight"><pre><span></span>cd controller
git checkout stable/lithium    //here I specify stable/lithium version
git branch
</pre></div>


<p><font face = "Times New Roman">3.Make sure your <em>settings.xml</em> file is right in place. Build the code with Internet connecdtion:</font>     </p>
<div class="highlight"><pre><span></span>mvn clean install -DskipTests
</pre></div>


<p><font face = "Times New Roman">4.Now run your controller:</font>        </p>
<div class="highlight"><pre><span></span>cd controller/karaf/opendaylight-karaf/target/assembly    
./bin/karaf
</pre></div>


<p><font face = "Times New Roman">5.And after a while you will enter the OpenDaylight command line mode as shown below:</font>    </p>
<div class="highlight"><pre><span></span>opendaylight-user@root&gt;
</pre></div>


<p><font face = "Times New Roman">6.Some useful command lines to check and install features:</font>    </p>
<div class="highlight"><pre><span></span><span class="n">feature</span><span class="o">:</span><span class="n">list</span> <span class="o">-</span><span class="n">i</span>   <span class="c1">//show the features which are already installed</span>
<span class="n">feature</span><span class="o">:</span><span class="n">list</span>      <span class="c1">//show all available features (installed ones are marked with &quot;x&quot;)</span>
<span class="n">feature</span><span class="o">:</span><span class="n">list</span> <span class="o">|</span> <span class="n">grep</span> <span class="o">&lt;</span><span class="n">keyword</span><span class="o">&gt;</span>   <span class="c1">//show features that contains &lt;keyword&gt;</span>
<span class="n">feature</span><span class="o">:</span><span class="n">install</span> <span class="o">&lt;</span><span class="n">feature</span><span class="o">&gt;</span>   <span class="c1">//install a &lt;feature&gt;</span>
</pre></div>


<hr />
<p><font face = "Times New Roman"><strong>STEP 3, Build and Install OpenDaylight Integration Project</strong></font></p>
<hr />
<p><font face = "Times New Roman">Integration Project is more like a framework project which is to integrate all other projects into OpenDaylight. With Integration project you can modify or put your own features under this project directory and test with the controller.</font>    </p>
<p><font face = "Times New Roman">1.Download the Integration source code:</font> </p>
<div class="highlight"><pre><span></span>git clone https://git.opendaylight.org/gerrit/p/integration.git
</pre></div>


<p><font face = "Times New Roman">2.Get into the integration directory and specify the version you want:</font>    </p>
<div class="highlight"><pre><span></span>cd integration
git checkout stable/lithium
mvn clean install -DskipTests
</pre></div>


<p><font face = "Times New Roman">3.After previous step is done, you may would like to run the controller:</font>    </p>
<div class="highlight"><pre><span></span>cd integration/distributions/karaf/target/assembly
./bin/karaf
</pre></div>


<p><font face = "Times New Roman">4.Finally you can now begin your development and replace original features with your own ones under this directory, after which you would be able to build and run the controller for testing:</font>    </p>
<div class="highlight"><pre><span></span>username@ubuntu:~/developApps/openDayLight/integration/distributions/karaf/target/assembly/system/org/opendaylight$ ls
aaa               integration      neutron         sdninterfaceapp  usc
bgpcep            iotdm            nic             sfc              vpnservice
capwap            l2switch         odlparent       snmp             vtn
controller        lacp             sxp             yangtools
coretutorials     lispflow         mapping         tcpmd5
didm              mdsal            ovsdb           topoprocessing
dlux              nemo             packetcable     tsdr
groupbasedpolicy  netconf          reservation     ttp
</pre></div>


<p><font face = "Times New Roman">（END）</font></p></font></div>