Title: Install Wireshark on Ubuntu
Date: 2016-07-08
Tags: Wireshark, Ubuntu

<div><font face="Times New Roman"><p><br>
1. Download WIreshark source code on website: <a href="https://www.wireshark.org/download.html">https://www.wireshark.org/download.html</a>  <br />
2. Extract files into targeted folder:     <br></p>
<div class="highlight"><pre><span></span>tar -xvf wireshark-1.10.7.tar.bz2
</pre></div>


<p><br>  <br />
3. Install compiling tools and dependencies:    <br></p>
<div class="highlight"><pre><span></span>sudo apt-get install build-essential
sudo apt-get install libgtk2.0-dev libglib2.0-dev
sudo apt-get install checkinstall
sudo apt-get install flex bison
sudo apt-get build-dep wireshark
sudo apt-get install qt5-default
sudo apt-get install libssl-dev
sudo apt-get install libgtk-3-dev
</pre></div>


<p><br>  <br />
4. Go to <a href="http://www.tcpdump.org">www.tcpdump.org</a> and find newest version of libpcap(e.g., libpcap-1.5.3.tar.gz):     <br></p>
<div class="highlight"><pre><span></span>#tar -xvf libpcap-1.5.3.tar.gz  
#cd libpcap-1.5.3.tar.gz  
#./configure  
#make  
#make install 
</pre></div>


<p><br>  <br />
5. Go to wireshark folder:    <br></p>
<div class="highlight"><pre><span></span>./autogen.sh
./configure --with-ssl --enable-setcap-install
make
make install
</pre></div></font></div>