Title: Apache Maven的简单介绍
Date: 2017-01-21
Tags: Maven

<div><font face="Times New Roman"><p><strong>What is Maven?</strong>    </p>
<hr />
<p>Maven is a very useful tool for project management. It helps developers conveniently build a complete life cycle framework. Especially in the case that there are several teams cooperating in the same project, Maven can do the building and configuration work in a very short time according to the predefined settings. As for most projects the settings are quite simple and reusable, it makes the development work much easier. To be more specific, Maven simplifies project management in terms of below aspects :  <br />
。Builds   <br />
。Documentation   <br />
。Reporting  <br />
。Dependencies  <br />
。SCMs  <br />
。Releases  <br />
。Distribution  <br />
。mailing list    </p>
<p>*The installation and path configuration for Maven can be found <a href="http://www.hao-jiang.com/pages/operating-systems/mavenenvironment.html">here</a>.    </p>
<hr />
<p><strong>Maven Repository</strong></p>
<hr />
<p><strong>Maven Local Repository</strong> is a place for storing dependencies(plugin jar and other files) of the project. By default it is in /.m2 directory. Sometimes you need to change it to another path.  <br />
* Default path in different operating systems:  <br />
Unix/Mac OS X： ~/.m2  <br />
Windows：C:\Documents and Settings{your-username}.m2    </p>
<p>Normally, you can change the location of local repository to a folder with an easy--to-understand name, e.g., maven-repo. But remember also to modify the maven path you specified in your file for environment variables.  <br />
<br>
<strong>Maven Central Repository</strong> is a place for maven to download the dependencies for your project when it cannot find them in your local repository.   <br />
<br>
<img alt="Maven Central Repository" src="http://7xq8q3.com1.z0.glb.clouddn.com/maven-center-repository.png" />  <br />
<br>
The address of it is <a href="http://repo1.maven.org/maven/">http://repo1.maven.org/maven/</a>. Browsing for this directory has been disabled, but you can view this directory's contents on <a href="http://search.maven.org">http://search.maven.org</a> instead.     </p>
<hr />
<p><strong>Add a Remote Repository</strong></p>
<hr />
<p>When the library you specified in <code>pom.xml</code> is not in the central repository and local repository, it will stop compiling and report an error. In such case you will need to download the dependency from other place. For example, org.jvnet.localizer is only for Java.net:  <br />
<code>pom.xml:</code>     </p>
<div class="highlight"><pre><span></span><span class="nt">&lt;dependency&gt;</span>
        <span class="nt">&lt;groupId&gt;</span>org.jvnet.localizer<span class="nt">&lt;/groupId&gt;</span>
        <span class="nt">&lt;artifactId&gt;</span>localizer<span class="nt">&lt;/artifactId&gt;</span>
        <span class="nt">&lt;version&gt;</span>1.8<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>


<p>When you try to build this maven project, it will report an error because it cannot find this dependency in its central repository. In such case you need to specify the url in pom.xml:    </p>
<div class="highlight"><pre><span></span> <span class="nt">&lt;repositories&gt;</span>
    <span class="nt">&lt;repository&gt;</span>
        <span class="nt">&lt;id&gt;</span>java.net<span class="nt">&lt;/id&gt;</span>
        <span class="nt">&lt;url&gt;</span>https://maven.java.net/content/repositories/public/<span class="nt">&lt;/url&gt;</span>
    <span class="nt">&lt;/repository&gt;</span>
    <span class="nt">&lt;/repositories&gt;</span>
</pre></div>


<hr />
<p><strong>And a JAR Library Manually</strong></p>
<hr />
<p>In case there is a jar not supporting maven and you need it, you can manually include the jar into local repository by commands. For example, kaptcha is a popular third-party java library which is used to generate pictures of verification code, but it is not supported in the central repository of maven. In such case we can download and install kaptcha jar, then include it in your local repository:    <br />
<br>
<strong>Installation:</strong>  <br />
Download kaptcha, extract it and copy <code>kaptcha-&lt;version&gt;.jar</code>into another place(C:\ for example). execute commands as below:    </p>
<div class="highlight"><pre><span></span>mvn install:install-file -Dfile=c:\kaptcha-{version}.jar -DgroupId=com.google.code -DartifactId=kaptcha -Dversion={version} -Dpackaging=jar
</pre></div>


<p>Example output:</p>
<div class="highlight"><pre><span></span>D:\&gt;mvn install:install-file -Dfile=c:\kaptcha-2.3.jar -DgroupId=com.google.code 
-DartifactId=kaptcha -Dversion=2.3 -Dpackaging=jar
[INFO] Scanning for projects...
[INFO] Searching repository for plugin with prefix: &#39;install&#39;.
[INFO] ------------------------------------------------------------------------
[INFO] Building Maven Default Project
[INFO]    task-segment: [install:install-file] (aggregator-style)
[INFO] ------------------------------------------------------------------------
[INFO] [install:install-file]
[INFO] Installing c:\kaptcha-2.3.jar to 
D:\maven_repo\com\google\code\kaptcha\2.3\kaptcha-2.3.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] ------------------------------------------------------------------------
[INFO] Total time: &lt; 1 second
[INFO] Finished at: Tue May 12 13:41:42 SGT 2014
[INFO] Final Memory: 3M/6M
[INFO] ------------------------------------------------------------------------
</pre></div>


<p>Now kaptcha jar was copied to maven local repository. <br />
<br>
<strong>Add in POM.XML:</strong>  <br />
After installation, declare the location of kaptcha in pom.xml:     </p>
<div class="highlight"><pre><span></span><span class="nt">&lt;dependency&gt;</span>
      <span class="nt">&lt;groupId&gt;</span>com.google.code<span class="nt">&lt;/groupId&gt;</span>
      <span class="nt">&lt;artifactId&gt;</span>kaptcha<span class="nt">&lt;/artifactId&gt;</span>
      <span class="nt">&lt;version&gt;</span>2.3<span class="nt">&lt;/version&gt;</span>
 <span class="nt">&lt;/dependency&gt;</span>
</pre></div>


<p>Now, kaptcha jar can be searched in your maven local repository.</p></font></div>