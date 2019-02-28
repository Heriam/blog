title: 使用Pelican基于Github Pages搭建博客教程
date: 2018-02-05
tags: Pelican, Blog, Github
template: article

**操作系统：**Mac OS / Linux      
**工具集：**    
1.Pelican——基于Python的静态网页生成器   
2.马克飞象——Evernote出的Markdown文本编辑器   
3.GoDaddy——域名供应商   
4.DNSPod——提供免费域名解析注册服务   
5.Github Pages——Github为每个注册用户提供300M的站点空间   
6.Python——Pelican工具需要Python运行环境   
7.Google Analytics——谷歌站点数据监测分析工具   
8.Google Custom Search——谷歌自定义搜索引擎可用作站内搜索工具   
9.Google Webmasters——谷歌站长工具    
10.Disqus——用来提供博客评论功能    
11.Sitemap——站点地图，供谷歌，百度等搜索引擎收录  
12.七牛云存储——静态资源管理，上传自动生成网盘直链      
**最终效果展示：**[欢迎访问我的博客](http://www.hao-jiang.com)：http://www.hao-jiang.com
***
**一、使用Github Pages创建个人博客页面**  
***
Git是一个开源的分布式版本控制系统，用以有效、高速的处理从很小到非常大的项目版本管理。GitHub可以托管各种git库的站点。通过GitHub Pages生成的静态站点，可以免费托管、自定义主题、并且自制网页界面。   
​     
1.首先到Github进行账号注册：[https://github.com/](https://github.com/)。       
2.注册后登录Github，右上角点击“Creat a new repo”，跳转到新页面后填写相关内容，注意版本库名使用'username.github.io'的格式，这里将username替换成自己的用户名即可。    
3.设置和选择好页面模板后就可以生成然后发布新网页了。    
4.创建SSH密钥并上传到Github。   
​    
​    
*以上内容都很简单，有问题可以参照：     
关于Github注册登录：[通过GitHub创建个人技术博客图文详解1](http://www.linuxidc.com/Linux/2015-02/114121.htm)   
关于Github页面生成：[通过GitHub创建个人技术博客图文详解2](http://www.linuxidc.com/Linux/2015-02/114121p2.htm)    
关于SSH认证：[Windows/Mac下使用SSH密钥连接Github](http://www.xuanfengge.com/using-ssh-key-link-github-photo-tour.html)     
官方文档：[Github官方文档在这里](https://help.github.com/articles/generating-ssh-keys/)       
***
**二、安装Python、Pelican和Markdown**
***
Pelican是一套开源的使用Python编写的博客静态生成, 可以添加文章和和创建页面, 可以使用MarkDown reStructuredText 和 AsiiDoc 的格式来抒写, 同时使用 Disqus评论系统, 支持 RSS和Atom输出, 插件, 主题, 代码高亮等功能, 采用Jajin2模板引擎, 可以很容易的更改模板。    
​    
1.安装Python。最新的Mac OS 一般都自带Python环境。在终端输入"python"即可确认Python版本。如有需要可以到官网安装：http://www.python.org/。      
​    
2.安装Pelican。可以从github克隆最新的代码安装, 并且建议在virtualenv下使用。首先建立 virtualenv（Python虚拟环境）:         

```
virtualenv pelican      # 创建
cd pelican
sh bin/activate            # 激活虚拟环境
```
从github克隆最新代码安装Pelican：      

```
git clone git://github.com/getpelican/pelican.git          # 下载代码
cd pelican
python setup.py install
```

3.安装Markdown:        

```
pip install markdown
```
***
**三、创建博客骨架**     
***
接下来将通过初始化Pelican设置来生成一个基本的博客框架。     
​     
1.搭建博客目录：     

```
mkdir blog
cd blog
pelican-quickstart
```
2.根据提示一步步输入相应的配置项，不知道如何设置的接受默认即可，后续可以通过编辑pelicanconf.py文件更改配置。完成后将会在根目录生成以下文件：     

```
.
|-- content                # 所有文章放于此目录
│   └── (pages)            # 存放手工创建的静态页面
|-- develop_server.sh      # 用于开启测试服务器
|-- Makefile               # 方便管理博客的Makefile
|-- output                 # 静态生成文件
|-- pelicanconf.py         # 配置文件
|-- publishconf.py         # 配置文件
```
3.进入output文件夹，把自己刚刚建好的username.github.io版本库clone下来，注意这里以及后文中的username要替换成自己的Github用户名：      

```
cd output
git clone https://github.com/username/username.github.io.git
```
4.设置一键上传部署到Github。打开根目录下的Makefile文件，修改以下三个地方：     

```
 OUTPUTDIR=$(BASEDIR)/output/username.github.io    
 publish:    
 $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)    
 github: publish    
 cd OUTPUTDIR ; git add . ;  git commit -am 'your comments' ; git push    
```

5.设置完后，以后写完文章就可以通过在blog根目录下执行“make github”进行一键部署了。     

***
**四、通过Markdown试写博文并上传Github发布**    
***
Markdown是当下非常流行的一种文本编辑语法，支持HTML转换，书写博文排版也方便快捷。    
​      

1.写一篇文章：用[马克飞象](http://pan.baidu.com/s/16soGY#path=%252F%25E9%25A9%25AC%25E5%2585%258B%25E9%25A3%259E%25E8%25B1%25A1%25E5%25AE%25A2%25E6%2588%25B7%25E7%25AB%25AF)编辑器用Markdown语法来写一篇文章保存为.md格式放在content目录下。写完后，执行以下命令，即可在本机http://127.0.0.1:8000看到效果。    

```
make publish
make serve
```

2.创建一个页面：这里以创建 About页面为例。在content目录创建pages子目录：    

```
mkdir content/pages
```

*然后创建About.md并填入下面内容：     

```
title: About Me        
date: 2013-04-18       

About me content
```
*注意上面title和date是.md文件的重要参数，需要写在文档开头。比如：    

```
Title: Pelican+Github
Date: 2014-10-07 22:20
Modified: 2014-10-07 23:04
Tags: python, pelican
Slug: build-blog-system-by-pelican
Authors: Joey Huang
Summary: blablablablablablablabla...
Status: draft
```


相关介绍请参见官方文档：http://pelican-zh.readthedocs.org/en/latest/zh-cn/ 。完成后同样可以在本机http://127.0.0.1:8000看效果。    
​      
3.创建导航目录项：Menu Item设置。在你的博客中，可设置相应的菜单项，菜单项是通过pelicanconf.py设置的，具体如下所示：      

```
MENUITEMS = (("ITEM1","http://github.com"),
             ("ITEM2",URL),
            ......)
```

***
**五、安装主题**    
***
这里以主题bootstrap2为例，同样还在blog目录下：     

```
git clone https://github.com/getpelican/pelican-themes.git
cd pelican-themes
pelican-themes -i bootstrap2
```
对应在在pelicanconf.py中添加主题选择条目：    

```
THEME = 'bootstrap2'
```
***
**六、安装第三方评论系统Disqus**    
***
在Disqus上申请一个站点，记住shortname。 在pelicanconf.py添加：     

```
DISQUS_SITENAME = Shortname
```
***
**七、添加Google Analytics**    
***
去Google Analytics申请账号并通过验证，记下跟踪ID（Track ID）， 在pelicanconf.py添加：    

```
GOOGLE_ANALYTICS = '跟踪ID'
```
***
**八、添加Google Webmasters和百度站长收录**    
***
为了让博客被Google更好的收录，比如手动让Googlebot抓取、提交Robots、更新Sitemap等等。        
​    
1.在Google Webmasters上注册并通过验证。    
​    
2.添加sitemap插件。还是到/blog目录下执行：    

```
cd ~/blog
git clone git://github.com/getpelican/pelican-plugins.git
```
*然后在pelicanconf.py里配置如下：    

```
PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap"]
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}
```

3.将make github命令后在output目录下生成的sitemap文件上传到Google Webmasters。      
​    
4.对于百度。它是宣称支持sitemap的，但是网上相关问题一大堆，要么格式不对要么就是抓取失败，要么突然不开放支持。在几次尝试失败以后，我是通过添加JavaScript代码来自动推送网站链接的。具体是在主题模板（base.html）面最后添加代码：    

```
<script>
(function(){
    var bp = document.createElement('script');
    bp.src = '//push.zhanzhang.baidu.com/push.js';
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
```

*我还是比较推崇这种方法的，因为比sitemap方法被抓取收录的时间短很多。谷歌的sitemap是xml格式。  
***
**九、添加谷歌／百度站内搜索**    
***
**谷歌站内搜索**    
1.修改主题。找到这个主题的templates文件夹中的base.html，在`<div class="nav-collapse">`的最后，添加以下内容：    

```
<form class="navbar-search pull-right" action="/search.html">
    <input type="text" class="search-query" placeholder="Search" name="q" id="s">
</form>
```
2.创建search.html。之后，在output目录下，新建一个名为search.html的文件，写入下面的内容，其中需要你自己修改的是google站内搜索的ID号，需要自己在[google站内搜索](https://cse.google.com)的网站上自己申请。     

```
<html lang="zh_CN">
<head>
<meta charset="utf-8">
<title>站内搜索</title>
</head>
  <body>
<style>
#search-box {
    position: relative;
    width: 50%;
    margin: 0;
    padding: 1em;
}

#search-form {
    height: 30px;
    border: 1px solid #999;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    background-color: #fff;
    overflow: hidden;
}

#search-text {
    font-size: 14px;
    color: #ddd;
    border-width: 0;
    background: transparent;
}

#search-box input[type="text"] {
    width: 90%;
    padding: 4px 0 12px 1em;
    color: #333;
    outline: none;
}
</style>
<div id='search-box'>
  <form action='/search.html' id='search-form' method='get' target='_top'>
    <input id='search-text' name='q' placeholder='Search' type='text'/>
  </form>
</div>
<div id="cse" style="width: 100%;">Loading</div>
<script src="http://www.google.com/jsapi" type="text/javascript"></script>
<script type="text/javascript"> 
  google.load('search', '1', {language : 'zh-CN', style : google.loader.themes.V2_DEFAULT});
  google.setOnLoadCallback(function() {
    var customSearchOptions = {};  var customSearchControl = new google.search.CustomSearchControl(
      '012191777864628038963:**********<!写入你申请的google站内搜索的ID号>）', customSearchOptions);
    customSearchControl.setResultSetSize(google.search.Search.FILTERED_CSE_RESULTSET);
    var options = new google.search.DrawOptions();
    options.enableSearchResultsOnly(); 
    customSearchControl.draw('cse', options);
    function parseParamsFromUrl() {
      var params = {};
      var parts = window.location.search.substr(1).split('\x26');
      for (var i = 0; i < parts.length; i++) {
        var keyValuePair = parts[i].split('=');
        var key = decodeURIComponent(keyValuePair[0]);
        params[key] = keyValuePair[1] ?
            decodeURIComponent(keyValuePair[1].replace(/\+/g, ' ')) :
            keyValuePair[1];
      }
      return params;
    }

    var urlParams = parseParamsFromUrl();
    var queryParamName = "q";
    if (urlParams[queryParamName]) {
      customSearchControl.execute(urlParams[queryParamName]);
    }
  }, true);
</script>
</body>
</html>
```
3.将GOOGLE_CUSTOM_SEARCH_SIDEBAR = "001578481551708017171:axpo6yvtdyg" 添加到pelicanconf.py文件。注意, 引号里的那一串字符是之前申请的自定义搜索引擎的id。    
4.最后发布后就可以看到搜索框了。      
***


​    
**百度站内搜索**    
1.在百度站长平台中注册一个账号，之后添加网站，按照提示验证网站。之后左侧`其他工具`中找到`站内搜索`，按照提示填写基本信息，选择搜索框样式，之后点击`查看代码`，复制其中内容，留用。    
2.同样在base.html的这个`<div class="nav-collapse">`的最后，新建一个`div`，刚才注册最后复制的代码粘贴到这个`div`中：    

```
<div class="navbar-search pull-right">
    <script>  
        <!略>
    </script>
</div>
```
3.发布验证。    
***
**十、添加Tags侧边栏**    
***
在其他一些pelican主题中，看到有标签云，想到Tags的链接可能比Categories的链接更有用，通过更改主题，添加了侧栏中红框内的Tags链接框。    
​    
1.还是找到base.html，找到categories部分：    

```
{% if categories %}
<div class="well" style="padding: 8px 0; background-color: #FBFBFB;">
<ul class="nav nav-list">
    <li class="nav-header"> 
    Categories
    </li>

    {% for cat, null in categories %}
    <li><a href="{{ SITEURL }}/{{ cat.url }}">{{ cat }}</a></li>
    {% endfor %}                   
</ul>
</div>
{% endif %}
```
2.在这段后面添加：    

```
{% if tags %}
<div class="well" style="padding: 8px 0; background-color: #FBFBFB;">
<ul class="nav nav-list">
    <li class="nav-header"> 
    Tags
    </li>

{% for name, tag in tags %}
    <li><a href="{{ SITEURL }}/{{ name.url }}">{{ name }}</a></li>
{% endfor %}
</ul>
</div>
{% endif %}
```

3.保存，重新发布网页验证。    

***
**十一、插入视频**    
***
其实很简单, 只需要把html代码放进markdown源文件就行了! 而视频的html代码在视频网站上一般都会提供。复制下来放进源文件即可。    
***
**十二、拷贝静态文件**    
***
如果我们定义静态的文件，该如何将它在每次生成的时候拷贝到 output 目录呢，我们以网站logo图片sitelogo.ico为例，在我们的 content/extra 下放置网站的静态资源文件：sitelogo.ico，在pelicanconf.py更改或添加 FILES_TO_COPY项：    

```
FILES_TO_COPY = (
    ("extra/sitelogo.ico", "sitelogo.ico"),
)
```
这样在每次生成html的时候都会把 content/extra下的 sitelogo.ico 拷贝到 output目录下。    

***
**十三、资源目录管理**    
***
使用目录名作为文章的分类名    

```
USE_FOLDER_AS_CATEGORY = True
```

使用文件名作为文章或页面的`slug（url）`    

```
FILENAME_METADATA = '(?P<slug>.*)'
```

页面的显示路径和保存路径，推荐下面的方式     

```
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'
```
***
**十四、指定文章或页面URL**    
***
在需要指定URL的文章或者页面中包括两个元数据url与save_as，例如：    

```
url: pages/url/
save_as: pages/url/index.html
```

*这个代码指定了本篇文章的url为pages/url/index.html       
​     
​      
根据上面很容易推断如何将一篇文章设置为网站的主页，如下代码即可实现将 `content/pages/home.md`设为主页：     

```
Title: [www.yanyulin.info](http://www.yanyulin.info)
Date: 2014-01-08
URL:
save_as: index.html
```
*另外还可以通过template:关键字来指定要使用的模板。    
***
**十五、独立域名设置**    
详见：http://www.jianshu.com/p/252b542b1abf 
***
Godaddy上购买专属域名，用dnspod进行动态域名解析，步骤如下:    

步骤1：修改Godaddy中的NameServers的两个地址为dnspod的DNS地址：    

```
f1g1ns1.dnspod.net
f1g1ns2.dnspod.net
```

步骤2：在Dnspod中添加一条A记录，指向Github URL      

```
username.github.io
```

步骤3：在Pelican主目录，即上面创建的blog/output/username.github.io目录，添加CNAME文件，在文件中添加你的独立域名。      
​    
​    
*注意这里的CNAME建议放在第十二步提到的content目录下的静态子目录`content/extra`下，并在配置文件中添加相关条目。     

***
**十六、相关文章、上下文导航**    
***
1.打开pelicanconf.py，定义插件目录和启用插件：     

```
#加载plugins
PLUGIN_PATH = "plugins"
PLUGINS = ["sitemap","neighbors","related_posts"]
#sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.8,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
#相关文章
RELATED_POSTS_MAX = 10
```
2.邻居导航，在主题模版中调用如下代码，可根据自己的情况修改：     

```
   <div class="pagination">
      <ul>
      {% if article.prev_article %}
        <li class="prev"><a href="{{ SITEURL }}/{{ article.prev_article.url}}">← Previous</a></li>
        {% else %}
        <li class="prev"><a href="/">← Previous</a></li>
        {% endif %}
        <li><a href="/archives.html">Archive</a></li>
        {% if article.next_article %}
        <li class="next"><a href="{{ SITEURL }}/{{ article.next_article.url}}">Next →</a></li>
        {% else %}
        <li class="next"><a href="/">Next →</a></li>
        {% endif %}
      </ul>
    </div>
```

3.相关文章：    

```
{% if article.related_posts %}
    <h4>Related Articles</h4>
    <ul>
    {% for related_post in article.related_posts %}
        <li><a href="{{ SITEURL }}/{{ related_post.url }}">{{ related_post.title }}</a></li>
    {% endfor %}
    </ul>
{% endif %} 
```
<br>
<br>
**十七、最后，一些比较占空间的资源文件（图片、媒体等）可以用七牛来进行存储管理**
<br>
<br>
<br>