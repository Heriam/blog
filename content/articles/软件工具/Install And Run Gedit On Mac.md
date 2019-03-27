Title: Install & Run Gedit from Terminal on Mac
Date: 2017-08-15
Tags: Gedit, MacOS

<div><font face="Times New Roman"><p><em>App description: gedit (App: gedit.app)</em>   <br />
<em>App website: <a href="https://wiki.gnome.org/Apps/Gedit">https://wiki.gnome.org/Apps/Gedit</a></em>     </p>
<hr />
<p><strong>Install from Terminal</strong></p>
<hr />
<p><br>  <br />
1.Run:    </p>
<div class="highlight"><pre><span></span><span class="nt">ruby</span> <span class="nt">-e</span> <span class="s2">&quot;$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)&quot;</span> <span class="o">&lt;</span> <span class="o">/</span><span class="nt">dev</span><span class="o">/</span><span class="nt">null</span> <span class="nt">2</span><span class="o">&gt;</span> <span class="o">/</span><span class="nt">dev</span><span class="o">/</span><span class="nt">null</span> <span class="o">;</span> <span class="nt">brew</span> <span class="nt">install</span> <span class="nt">caskroom</span><span class="o">/</span><span class="nt">cask</span><span class="o">/</span><span class="nt">brew-cask</span> <span class="nt">2</span><span class="o">&gt;</span> <span class="o">/</span><span class="nt">dev</span><span class="o">/</span><span class="nt">null</span>
</pre></div>


<p><br>  <br />
2.After the command finishes, run:    </p>
<div class="highlight"><pre><span></span>brew cask install gedit
</pre></div>


<p><br>  <br />
Now Gedit is installed.   <br />
<br>    </p>
<hr />
<p><strong>Run Gedit from Terminal</strong></p>
<hr />
<p><br>
<strong>Solution 1.</strong> Add the following line to ~/.profile or ~/.bash_profile:    </p>
<div class="highlight"><pre><span></span><span class="x">export PATH=/Users/&lt;Username&gt;/Applications/gedit.app/Contents/MacOS/gedit:</span><span class="p">$</span><span class="nv">PATH</span><span class="x"></span>
</pre></div>


<p><br>  <br />
<strong>Solution 2.</strong> Create a script named <code>gedit</code> in <code>/usr/local/bin</code> and make it executable:  <br />
<br> <br />
a. Create a new file:     </p>
<div class="highlight"><pre><span></span>sudo vim /usr/local/bin/gedit
</pre></div>


<p><br>  <br />
b. Add content as below, save and quit:    </p>
<table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="ch">#!/bin/bash    </span>
/Users/&lt;Username&gt;/Applications/gedit.app/Contents/MacOS/gedit    
</pre></div>
</td></tr></table>

<p><br>  <br />
c. Make it executable:    </p>
<div class="highlight"><pre><span></span>sudo chmod 755 /usr/local/bin/gedit
</pre></div>


<p><br>
<br>
(END)</p></font></div>