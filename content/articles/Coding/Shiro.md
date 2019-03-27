Title: Apache Shiro Multi-tenancy with JDBC MySQL
Date: 2016-02-21
Tags: MySQL, Java, Shiro, AAA

<p><b>0. GOALS</b><hr>
- Provide user authentication and authorization for <strong>multi-tenant</strong> scenarios     <br> <br />
- Provide easy-to-maintain data storage with only <strong>one database</strong>    <br> <br />
- Provide <strong>domain-differentiated, credential-based</strong> authentication    <br> <br />
- Provide <strong>domain-differentiated, role-based, service-specific</strong> authorization;    <br>   </p>
  <p><br><br><br><b>1. QuickStart with Apache Shiro</b><hr>
- <a href="http://shiro.apache.org/reference.html">English Documentation</a>    <br> <br />
- <a href="http://jinnianshilongnian.iteye.com/blog/2018398">Chinese Documentation</a>    <br> <br />
- <a href="https://github.com/zhangkaitao/shiro-example">Example Applications</a>    <br><br />
- <a href="http://shiro.apache.org/architecture.html">Architecture:</a>    <br><br>  <br />
  <img alt="Shiro Architecture" src="http://shiro.apache.org/assets/images/ShiroArchitecture.png" />  <br />
  <br><br>    </p>
  <p><br><b>2. Environment Prerequisites</b><hr></p>

<div class="highlight"><pre><span></span>Apache Maven 3.3.9 (bb52d8502b132ec0a5a3f4c09453c07478323dc5; 2015-11-10T17:41:47+01:00)
Maven home: /Library/Maven
Java version: 1.7.0_79, vendor: Oracle Corporation
Java home: /Library/Java/JavaVirtualMachines/jdk1.7.0_79.jdk/Contents/Home/jre
Default locale: en_US, platform encoding: UTF-8
OS name: &quot;mac os x&quot;, version: &quot;10.11.2&quot;, arch: &quot;x86_64&quot;, family: &quot;mac&quot;
</pre></div>


<p><br><br><br><b>3. Apache Shiro Maven Dependency</b><hr></p>
<div class="highlight"><pre><span></span>        <span class="nt">&lt;dependency&gt;</span>
            <span class="nt">&lt;groupId&gt;</span>org.apache.shiro<span class="nt">&lt;/groupId&gt;</span>
            <span class="nt">&lt;artifactId&gt;</span>shiro-core<span class="nt">&lt;/artifactId&gt;</span>
            <span class="nt">&lt;version&gt;</span>1.1.0<span class="nt">&lt;/version&gt;</span>
        <span class="nt">&lt;/dependency&gt;</span>
        <span class="nt">&lt;dependency&gt;</span>
            <span class="nt">&lt;groupId&gt;</span>org.slf4j<span class="nt">&lt;/groupId&gt;</span>
            <span class="nt">&lt;artifactId&gt;</span>slf4j-simple<span class="nt">&lt;/artifactId&gt;</span>
            <span class="nt">&lt;version&gt;</span>1.6.1<span class="nt">&lt;/version&gt;</span>
            <span class="nt">&lt;scope&gt;</span>test<span class="nt">&lt;/scope&gt;</span>
        <span class="nt">&lt;/dependency&gt;</span>
</pre></div>


<p><br><br><br><b>4. MySQL QuickStart</b><hr>
1. <a href="http://www.cnblogs.com/macro-cheng/archive/2011/10/25/mysql-001.html">Install MySQL on Mac</a>     <br> <br />
2. <a href="http://jingyan.baidu.com/article/90bc8fc87b04e3f653640c1c.html">修改Root密码</a>    <br>       <br />
3. <a href="http://www.w3schools.com/sql/default.asp">W3Schools SQL Tutorial</a>   <br> <br />
4. <a href="http://www.w3school.com.cn/sql/index.asp">W3School中文SQL教程</a>    <br> <br />
5. <a href="http://www.runoob.com/mysql/mysql-tutorial.html">RUNOOB MySQL教程</a>    <br>   </p>
  <p><br><br><br><b>5. Create Tables</b>  <hr>  </p>
  <p>1.User Table:  <br />
  <img alt="user table" src="http://7xq8q3.com1.z0.glb.clouddn.com/user" />  <br />
   <br>  <br />
  2.Domain_User Table:  <br />
  <img alt="domain user table" src="http://7xq8q3.com1.z0.glb.clouddn.com/domain_user" />
    <br>  <br />
  3.User_Role Table:  <br />
  <img alt="user role table" src="http://7xq8q3.com1.z0.glb.clouddn.com/user_role" />
     <br>  <br />
  4.Permission_Domain_Role Table:  <br />
  <img alt="permission domain role table" src="http://7xq8q3.com1.z0.glb.clouddn.com/perms_dom_role" />
  <br><br><br><b>6. JDBC Setup and Code Customization</b>  <hr>  </p>
  <p>1.Maven Dependency:</p>

<div class="highlight"><pre><span></span><span class="nt">&lt;dependency&gt;</span>  
    <span class="nt">&lt;groupId&gt;</span>mysql<span class="nt">&lt;/groupId&gt;</span>  
    <span class="nt">&lt;artifactId&gt;</span>mysql-connector-java<span class="nt">&lt;/artifactId&gt;</span>  
    <span class="nt">&lt;version&gt;</span>5.1.25<span class="nt">&lt;/version&gt;</span>  
<span class="nt">&lt;/dependency&gt;</span>  
<span class="nt">&lt;dependency&gt;</span>  
    <span class="nt">&lt;groupId&gt;</span>com.alibaba<span class="nt">&lt;/groupId&gt;</span>  
    <span class="nt">&lt;artifactId&gt;</span>druid<span class="nt">&lt;/artifactId&gt;</span>  
    <span class="nt">&lt;version&gt;</span>0.2.23<span class="nt">&lt;/version&gt;</span>  
<span class="nt">&lt;/dependency&gt;</span> 
</pre></div>


<p><br>  <br />
2.Rewrite getPermissions method in jdbcRealm</p>
<div class="highlight"><pre><span></span><span class="kd">protected</span> <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="nf">getPermissions</span><span class="o">(</span><span class="n">Connection</span> <span class="n">conn</span><span class="o">,</span> <span class="n">String</span> <span class="n">username</span><span class="o">)</span> <span class="kd">throws</span> <span class="n">SQLException</span> <span class="o">{</span>
    <span class="n">PreparedStatement</span> <span class="n">ps</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
    <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">permissions</span> <span class="o">=</span> <span class="k">new</span> <span class="n">LinkedHashSet</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;();</span>
    <span class="k">try</span> <span class="o">{</span>
        <span class="n">ps</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="na">prepareStatement</span><span class="o">(</span><span class="n">permissionsQuery</span><span class="o">);</span>
    
        <span class="n">ps</span><span class="o">.</span><span class="na">setString</span><span class="o">(</span><span class="mi">1</span><span class="o">,</span> <span class="n">username</span><span class="o">);</span>
    
        <span class="n">ResultSet</span> <span class="n">rs</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
    
        <span class="k">try</span> <span class="o">{</span>
            <span class="c1">// Execute query</span>
            <span class="n">rs</span> <span class="o">=</span> <span class="n">ps</span><span class="o">.</span><span class="na">executeQuery</span><span class="o">();</span>
    
            <span class="c1">// Loop over results and add each returned role to a set</span>
            <span class="k">while</span> <span class="o">(</span><span class="n">rs</span><span class="o">.</span><span class="na">next</span><span class="o">())</span> <span class="o">{</span>
    
                <span class="n">String</span> <span class="n">permissionString</span> <span class="o">=</span> <span class="n">rs</span><span class="o">.</span><span class="na">getString</span><span class="o">(</span><span class="mi">1</span><span class="o">);</span>
    
                <span class="c1">// Add the permission to the set of permissions</span>
                <span class="n">permissions</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">permissionString</span><span class="o">);</span>
            <span class="o">}</span>
        <span class="o">}</span> <span class="k">finally</span> <span class="o">{</span>
            <span class="n">JdbcUtils</span><span class="o">.</span><span class="na">closeResultSet</span><span class="o">(</span><span class="n">rs</span><span class="o">);</span>
        <span class="o">}</span>
    <span class="o">}</span> <span class="k">finally</span> <span class="o">{</span>
        <span class="n">JdbcUtils</span><span class="o">.</span><span class="na">closeStatement</span><span class="o">(</span><span class="n">ps</span><span class="o">);</span>
    <span class="o">}</span>
    
    <span class="k">return</span> <span class="n">permissions</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><br>
3.Add getUserDomain method in jdbcRealm</p>
<div class="highlight"><pre><span></span>    <span class="kd">public</span> <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="nf">getUserDomain</span><span class="o">(</span><span class="n">Connection</span> <span class="n">conn</span><span class="o">,</span> <span class="n">String</span> <span class="n">username</span><span class="o">){</span>

        <span class="n">PreparedStatement</span> <span class="n">ps</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
        <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">domains</span> <span class="o">=</span> <span class="k">new</span> <span class="n">LinkedHashSet</span><span class="o">&lt;&gt;();</span>
        <span class="k">try</span> <span class="o">{</span>
            <span class="n">ps</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="na">prepareStatement</span><span class="o">(</span><span class="n">userDomainQuery</span><span class="o">);</span>
            <span class="n">ps</span><span class="o">.</span><span class="na">setString</span><span class="o">(</span><span class="mi">1</span><span class="o">,</span> <span class="n">username</span><span class="o">);</span>
            <span class="n">ResultSet</span> <span class="n">rs</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
    
            <span class="k">try</span> <span class="o">{</span>
                <span class="n">rs</span> <span class="o">=</span> <span class="n">ps</span><span class="o">.</span><span class="na">executeQuery</span><span class="o">();</span>
                <span class="k">while</span> <span class="o">(</span><span class="n">rs</span><span class="o">.</span><span class="na">next</span><span class="o">())</span> <span class="o">{</span>
                    <span class="n">String</span> <span class="n">domainID</span> <span class="o">=</span> <span class="n">rs</span><span class="o">.</span><span class="na">getString</span><span class="o">(</span><span class="mi">1</span><span class="o">);</span>
                    <span class="n">domains</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">domainID</span><span class="o">);</span>
                <span class="o">}</span>
            <span class="o">}</span> <span class="k">catch</span> <span class="o">(</span><span class="n">SQLException</span> <span class="n">e</span><span class="o">)</span> <span class="o">{</span>
                <span class="n">e</span><span class="o">.</span><span class="na">printStackTrace</span><span class="o">();</span>
            <span class="o">}</span> <span class="k">finally</span> <span class="o">{</span>
                <span class="n">JdbcUtils</span><span class="o">.</span><span class="na">closeResultSet</span><span class="o">(</span><span class="n">rs</span><span class="o">);</span>
            <span class="o">}</span>
        <span class="o">}</span> <span class="k">catch</span> <span class="o">(</span><span class="n">SQLException</span> <span class="n">e</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">e</span><span class="o">.</span><span class="na">printStackTrace</span><span class="o">();</span>
        <span class="o">}</span> <span class="k">finally</span> <span class="o">{</span>
            <span class="n">JdbcUtils</span><span class="o">.</span><span class="na">closeStatement</span><span class="o">(</span><span class="n">ps</span><span class="o">);</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">domains</span><span class="o">;</span>
    
    <span class="o">}</span>
</pre></div>


<p><br>4.Rewrite doGetAuthenticationInfo method in jdbcRealm</p>
<div class="highlight"><pre><span></span><span class="kd">protected</span> <span class="n">AuthenticationInfo</span> <span class="nf">doGetAuthenticationInfo</span><span class="o">(</span><span class="n">AuthenticationToken</span> <span class="n">token</span><span class="o">)</span> <span class="kd">throws</span> <span class="n">AuthenticationException</span> <span class="o">{</span>

        <span class="n">VTNAuthNToken</span> <span class="n">upToken</span> <span class="o">=</span> <span class="o">(</span><span class="n">VTNAuthNToken</span><span class="o">)</span> <span class="n">token</span><span class="o">;</span>
        <span class="n">String</span> <span class="n">username</span> <span class="o">=</span> <span class="n">upToken</span><span class="o">.</span><span class="na">getUsername</span><span class="o">();</span>
        <span class="n">String</span> <span class="n">domainID</span> <span class="o">=</span> <span class="n">Integer</span><span class="o">.</span><span class="na">toString</span><span class="o">(</span><span class="n">upToken</span><span class="o">.</span><span class="na">getDomainId</span><span class="o">());</span>
        <span class="c1">// Null username is invalid</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">username</span> <span class="o">==</span> <span class="kc">null</span><span class="o">)</span> <span class="o">{</span>
            <span class="k">throw</span> <span class="k">new</span> <span class="n">AccountException</span><span class="o">(</span><span class="s">&quot;Null usernames are not allowed by this realm.&quot;</span><span class="o">);</span>
        <span class="o">}</span>
    
        <span class="n">Connection</span> <span class="n">conn</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
        <span class="n">SimpleAuthenticationInfo</span> <span class="n">info</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
        <span class="k">try</span> <span class="o">{</span>
            <span class="n">conn</span> <span class="o">=</span> <span class="n">dataSource</span><span class="o">.</span><span class="na">getConnection</span><span class="o">();</span>
            <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">domains</span> <span class="o">=</span> <span class="n">getUserDomain</span><span class="o">(</span><span class="n">conn</span><span class="o">,</span> <span class="n">username</span><span class="o">);</span>
            <span class="k">if</span><span class="o">(!(</span><span class="n">domains</span><span class="o">.</span><span class="na">contains</span><span class="o">(</span><span class="n">domainID</span><span class="o">))){</span>
                <span class="k">throw</span> <span class="k">new</span> <span class="n">AuthenticationException</span><span class="o">(</span><span class="s">&quot;Domain not found&quot;</span><span class="o">);</span>
            <span class="o">}</span>
    
            <span class="n">String</span> <span class="n">password</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
            <span class="n">String</span> <span class="n">salt</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
            <span class="k">switch</span> <span class="o">(</span><span class="n">saltStyle</span><span class="o">)</span> <span class="o">{</span>
                <span class="k">case</span> <span class="n">NO_SALT</span><span class="o">:</span>
                    <span class="n">password</span> <span class="o">=</span> <span class="n">getPasswordForUser</span><span class="o">(</span><span class="n">conn</span><span class="o">,</span> <span class="n">username</span><span class="o">)[</span><span class="mi">0</span><span class="o">];</span>
                    <span class="k">break</span><span class="o">;</span>
                <span class="k">case</span> <span class="n">CRYPT</span><span class="o">:</span>
                    <span class="c1">// TODO: separate password and hash from getPasswordForUser[0]</span>
                    <span class="k">throw</span> <span class="k">new</span> <span class="n">ConfigurationException</span><span class="o">(</span><span class="s">&quot;Not implemented yet&quot;</span><span class="o">);</span>
                    <span class="c1">//break;</span>
                <span class="k">case</span> <span class="n">COLUMN</span><span class="o">:</span>
                    <span class="n">String</span><span class="o">[]</span> <span class="n">queryResults</span> <span class="o">=</span> <span class="n">getPasswordForUser</span><span class="o">(</span><span class="n">conn</span><span class="o">,</span> <span class="n">username</span><span class="o">);</span>
                    <span class="n">password</span> <span class="o">=</span> <span class="n">queryResults</span><span class="o">[</span><span class="mi">0</span><span class="o">];</span>
                    <span class="n">salt</span> <span class="o">=</span> <span class="n">queryResults</span><span class="o">[</span><span class="mi">1</span><span class="o">];</span>
                    <span class="k">break</span><span class="o">;</span>
                <span class="k">case</span> <span class="n">EXTERNAL</span><span class="o">:</span>
                    <span class="n">password</span> <span class="o">=</span> <span class="n">getPasswordForUser</span><span class="o">(</span><span class="n">conn</span><span class="o">,</span> <span class="n">username</span><span class="o">)[</span><span class="mi">0</span><span class="o">];</span>
                    <span class="n">salt</span> <span class="o">=</span> <span class="n">getSaltForUser</span><span class="o">(</span><span class="n">username</span><span class="o">);</span>
            <span class="o">}</span>
    
            <span class="k">if</span> <span class="o">(</span><span class="n">password</span> <span class="o">==</span> <span class="kc">null</span><span class="o">)</span> <span class="o">{</span>
                <span class="k">throw</span> <span class="k">new</span> <span class="n">UnknownAccountException</span><span class="o">(</span><span class="s">&quot;No account found for user [&quot;</span> <span class="o">+</span> <span class="n">username</span> <span class="o">+</span> <span class="s">&quot;]&quot;</span><span class="o">);</span>
            <span class="o">}</span>
    
            <span class="n">info</span> <span class="o">=</span> <span class="k">new</span> <span class="n">SimpleAuthenticationInfo</span><span class="o">(</span><span class="n">username</span><span class="o">,</span> <span class="n">password</span><span class="o">.</span><span class="na">toCharArray</span><span class="o">(),</span> <span class="n">getName</span><span class="o">());</span>
    
            <span class="k">if</span> <span class="o">(</span><span class="n">salt</span> <span class="o">!=</span> <span class="kc">null</span><span class="o">)</span> <span class="o">{</span>
                <span class="n">info</span><span class="o">.</span><span class="na">setCredentialsSalt</span><span class="o">(</span><span class="n">ByteSource</span><span class="o">.</span><span class="na">Util</span><span class="o">.</span><span class="na">bytes</span><span class="o">(</span><span class="n">salt</span><span class="o">));</span>
            <span class="o">}</span>
    
        <span class="o">}</span> <span class="k">catch</span> <span class="o">(</span><span class="n">SQLException</span> <span class="n">e</span><span class="o">)</span> <span class="o">{</span>
            <span class="kd">final</span> <span class="n">String</span> <span class="n">message</span> <span class="o">=</span> <span class="s">&quot;There was a SQL error while authenticating user [&quot;</span> <span class="o">+</span> <span class="n">username</span> <span class="o">+</span> <span class="s">&quot;]&quot;</span><span class="o">;</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">log</span><span class="o">.</span><span class="na">isErrorEnabled</span><span class="o">())</span> <span class="o">{</span>
                <span class="n">log</span><span class="o">.</span><span class="na">error</span><span class="o">(</span><span class="n">message</span><span class="o">,</span> <span class="n">e</span><span class="o">);</span>
            <span class="o">}</span>
    
            <span class="c1">// Rethrow any SQL errors as an authentication exception</span>
            <span class="k">throw</span> <span class="k">new</span> <span class="n">AuthenticationException</span><span class="o">(</span><span class="n">message</span><span class="o">,</span> <span class="n">e</span><span class="o">);</span>
        <span class="o">}</span> <span class="k">finally</span> <span class="o">{</span>
            <span class="n">JdbcUtils</span><span class="o">.</span><span class="na">closeConnection</span><span class="o">(</span><span class="n">conn</span><span class="o">);</span>
        <span class="o">}</span>
    
        <span class="k">return</span> <span class="n">info</span><span class="o">;</span>
    <span class="o">}</span>
</pre></div>


<p><br><br><br><b>7. Setup Shiro.ini Configuration File</b>  <hr>  </p>
<div class="highlight"><pre><span></span><span class="k">[main]</span>
<span class="c1">#authenticator</span>
<span class="na">authenticator</span><span class="o">=</span><span class="s">aaa.authn.VTNAuthenticator   #(Customized)</span>
<span class="na">authenticationStrategy</span><span class="o">=</span><span class="s">org.apache.shiro.authc.pam.AtLeastOneSuccessfulStrategy</span>
<span class="na">authenticator.authenticationStrategy</span><span class="o">=</span><span class="s">$authenticationStrategy</span>
<span class="na">securityManager.authenticator</span><span class="o">=</span><span class="s">$authenticator</span>

<span class="c1">#authorizer</span>
<span class="na">authorizer</span><span class="o">=</span><span class="s">aaa.authz.VTNAuthorizer         #(Customized)</span>
<span class="na">permissionResolver</span><span class="o">=</span><span class="s">org.apache.shiro.authz.permission.WildcardPermissionResolver</span>
<span class="na">authorizer.permissionResolver</span><span class="o">=</span><span class="s">$permissionResolver</span>
<span class="na">securityManager.authorizer</span><span class="o">=</span><span class="s">$authorizer</span>

<span class="c1">#Realm</span>
<span class="na">jdbcRealm</span><span class="o">=</span> <span class="s">aaa.realms.MySQLRealm           #(Customized)</span>
<span class="na">dataSource</span><span class="o">=</span><span class="s">com.alibaba.druid.pool.DruidDataSource</span>
<span class="na">dataSource.driverClassName</span><span class="o">=</span><span class="s">com.mysql.jdbc.Driver</span>
<span class="na">dataSource.url</span><span class="o">=</span><span class="s">jdbc:mysql://localhost:3306/vtn</span>
<span class="na">dataSource.username</span><span class="o">=</span><span class="s">root</span>
<span class="na">jdbcRealm.dataSource</span><span class="o">=</span><span class="s">$dataSource</span>
<span class="na">securityManager.realms</span><span class="o">=</span><span class="s">$jdbcRealm</span>
<span class="na">jdbcRealm.permissionsLookupEnabled</span> <span class="o">=</span> <span class="s">true</span>

<span class="c1">#SQL Queries</span>
<span class="na">jdbcRealm.authenticationQuery</span> <span class="o">=</span> <span class="s">SELECT password FROM user WHERE user_name = ?</span>

<span class="na">jdbcRealm.userRolesQuery</span> <span class="o">=</span> <span class="s">SELECT role_id FROM user_role left join user using(user_id) WHERE user_name = ?</span>

<span class="na">jdbcRealm.permissionsQuery</span> <span class="o">=</span> <span class="s">SELECT distinct permission_id FROM perm_domain_role left join domain_user using(domain_id) left join user using(user_id) WHERE (domain_id, role_id) IN ( SELECT domain_id, role_id From user left join user_role using(user_id) left join domain_user using(user_id) WHERE user_name = ?)</span>
</pre></div>


<p><br><b>8. Tips about SQL permissionsQuery in INI file:</b><hr><br></p>
<p>1. Query with same parameter at two places:    </p>
<div class="highlight"><pre><span></span><span class="k">SELECT</span> <span class="n">T</span><span class="p">.</span><span class="n">P</span> 

<span class="k">FROM</span> <span class="p">(</span><span class="k">SELECT</span> <span class="k">distinct</span> <span class="n">permission_id</span> <span class="k">as</span> <span class="n">P</span><span class="p">,</span> <span class="n">role_id</span> <span class="k">AS</span> <span class="n">R</span> 
      <span class="k">FROM</span> <span class="n">perm_domain_role</span> 
           <span class="k">left</span> <span class="k">join</span> <span class="n">domain_user</span> <span class="k">using</span><span class="p">(</span><span class="n">domain_id</span><span class="p">)</span> 
           <span class="k">left</span> <span class="k">join</span> <span class="k">user</span> <span class="k">using</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span> 
      <span class="k">WHERE</span> <span class="n">user_name</span><span class="o">=</span> <span class="o">?</span><span class="p">)</span> <span class="k">AS</span> <span class="n">T</span> 

<span class="k">WHERE</span> <span class="n">T</span><span class="p">.</span><span class="n">R</span> 
  <span class="k">IN</span> <span class="p">(</span><span class="k">SELECT</span> <span class="n">role_id</span> 
      <span class="k">FROM</span> <span class="n">user_role</span> 
           <span class="k">left</span> <span class="k">join</span> <span class="k">user</span> <span class="k">using</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span> 
      <span class="k">WHERE</span> <span class="n">user_name</span> <span class="o">=</span> <span class="o">?</span><span class="p">)</span>
</pre></div>


<p><br>
2.Optimization with only one parameter:     </p>
<div class="highlight"><pre><span></span><span class="k">SELECT</span> <span class="k">DISTINCT</span> <span class="n">permission_id</span> 

<span class="k">FROM</span> <span class="n">perm_domain_role</span> 
     <span class="k">left</span> <span class="k">join</span> <span class="n">domain_user</span> <span class="k">using</span><span class="p">(</span><span class="n">domain_id</span><span class="p">)</span> 
     <span class="k">left</span> <span class="k">join</span> <span class="k">user</span> <span class="k">using</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span> 

<span class="k">WHERE</span> <span class="p">(</span><span class="n">domain_id</span><span class="p">,</span> <span class="n">role_id</span><span class="p">)</span>
 <span class="k">IN</span> <span class="p">(</span><span class="k">SELECT</span> <span class="n">domain_id</span><span class="p">,</span> <span class="n">role_id</span> 
     <span class="k">FROM</span> <span class="k">user</span> 
          <span class="k">left</span> <span class="k">join</span> <span class="n">user_role</span> <span class="k">using</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span> 
          <span class="k">left</span> <span class="k">join</span> <span class="n">domain_user</span> <span class="k">using</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span> 
     <span class="k">WHERE</span> <span class="n">user_name</span> <span class="o">=</span> <span class="o">?</span><span class="p">)</span>
</pre></div>

<p><br><br>
<strong>9. Result:</strong></p><hr>
<p>Finally,  you can easily test that each user has different services  authorized by Shiro according to its tenant domain and its role.</p>
<div class="highlight"><pre><span></span><span class="k">for</span> <span class="o">(</span><span class="n">VTNAuthNToken</span> <span class="n">token</span><span class="o">:</span> <span class="n">userTokenList</span><span class="o">)</span> <span class="o">{</span>
      <span class="n">Mappable</span> <span class="n">userRequest</span> <span class="o">=</span> <span class="k">new</span> <span class="n">MappableMsg</span><span class="o">(</span><span class="kc">null</span><span class="o">,</span><span class="kc">null</span><span class="o">,</span><span class="n">token</span><span class="o">);</span>
      <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">service</span><span class="o">:</span> <span class="n">servList</span><span class="o">){</span>
            <span class="n">userRequest</span><span class="o">.</span><span class="na">setServID</span><span class="o">(</span><span class="n">service</span><span class="o">);</span>
            <span class="k">if</span><span class="o">(</span><span class="n">IShiro</span><span class="o">.</span><span class="na">getInstance</span><span class="o">().</span><span class="na">isAuthorized</span><span class="o">(</span><span class="n">userRequest</span><span class="o">)){</span>
                  <span class="n">String</span> <span class="n">entry</span> <span class="o">=</span> <span class="s">&quot;Domain &quot;</span><span class="o">+</span><span class="n">token</span><span class="o">.</span><span class="na">getDomainId</span><span class="o">()+</span><span class="s">&quot;: &quot;</span><span class="o">+</span><span class="n">token</span><span class="o">.</span><span class="na">getUsername</span><span class="o">()+</span><span class="s">&quot;: &quot;</span><span class="o">+</span><span class="n">service</span><span class="o">;</span>
                  <span class="n">authZResult</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">entry</span><span class="o">);</span>
            <span class="o">}</span>
      <span class="o">}</span>
<span class="o">}</span>
<span class="k">for</span><span class="o">(</span><span class="n">String</span> <span class="n">i</span><span class="o">:</span> <span class="n">authZResult</span><span class="o">){</span>
      <span class="n">System</span><span class="o">.</span><span class="na">out</span><span class="o">.</span><span class="na">println</span><span class="o">(</span><span class="n">i</span><span class="o">);</span>
<span class="o">}</span>
</pre></div>
<p><br>Output:</p>
<div class="highlight"><pre>
Domain 1: admin: vtn:topo:create
Domain 1: admin: vtn:topo:read
Domain 1: admin: vtn:topo:update
Domain 1: admin: vtn:topo:delete
Domain 1: admin: system:vtn:create
Domain 1: admin: system:vtn:update
Domain 1: admin: system:vtn:delete
Domain 1: admin: serv:firewall:create
Domain 1: admin: serv:firewall:read
Domain 1: admin: serv:firewall:update
Domain 1: admin: serv:firewall:delete
Domain 1: boss: system:vtn:read
Domain 2: tenant1: vtn:topo:create
Domain 2: tenant1: vtn:topo:read
Domain 2: tenant1: vtn:topo:update
Domain 2: tenant1: vtn:topo:delete
Domain 2: tenant1: serv:firewall:create
Domain 2: tenant1: serv:firewall:read
Domain 2: tenant1: serv:firewall:update
Domain 2: tenant1: serv:firewall:delete
Domain 2: guest1: vtn:topo:read
Domain 2: guest1: serv:firewall:read
Domain 3: tenant2: vtn:topo:create
Domain 3: tenant2: vtn:topo:read
Domain 3: tenant2: vtn:topo:update
Domain 3: tenant2: vtn:topo:delete
Domain 3: guest2: vtn:topo:read
</pre></div>