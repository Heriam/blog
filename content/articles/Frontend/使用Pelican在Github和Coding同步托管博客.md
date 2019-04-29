title: 使用Pelican在Github(国外)和Coding(国内)同步托管博客
date: 2018-02-05
tags: Pelican, Git
template: article

**介绍：** Github Pages 禁用了百度爬虫，因此百度搜索引擎经常抓取不到在Github上托管的博客链接。本文介绍一种可行的解决方法：     
- 注册Coding用来托管一份和Github上一样的博客仓库专门服务国内的索引    
- 配置DNS解析，将国内的线路解析到Coding，国外的线路解析到Github    
- 配置Pelican，支持一键将同一份本地博客仓库同时发布到Github和Coding
  ​          
  <br>   
***
**一、**[《Pelican＋Github博客搭建详细教程》](<https://jiang-hao.com/articles/2018/blog-%E4%BD%BF%E7%94%A8Pelican%E5%9F%BA%E4%BA%8EGithubPages%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2%E6%95%99%E7%A8%8B.html>)      

***
按照标题链接给出的教程先搭建出一个基于Github托管的博客系统。接下来将说明如何将博客同步到Coding。    
<br>   

***
**二、在Coding创建一个新的项目**
***
1. 在[Coding首页](http://www.coding.net)进行注册并登陆，创建项目的方法与Github类似，不同之处在于coding新建的公开项目名和用户名相同，而不像Github那样是<用户名>.github.io。创建完成后，生成的新的项目链接应该类似于：`https://coding.net/<usrname>/<username>.git`。    
    <br>   
2. 将本地SSH公钥拷贝到coding。操作同样与Github类似。由于本地已经为Github生成了一个公钥，这里只用cd进入~/.ssh文件夹查看一个名为`id_rsa.pub`文件的内容，类似于如下。我们只拷贝**邮箱之前**的所有内容到coding的公钥管理页面。     
```
ssh-rsa AAAAfafjIJGOF+FDA。。(省略)。。Ksap Heriam@users.noreply.github.com
```
<br>   

***
**三、将仓库拷贝到Coding**
***
1. 进入Pelican的output目录下的本地博客仓库，打开.git/config，修改远程仓库，将 origin 改为 github，并添加 coding：   

```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
        ignorecase = true
        precomposeunicode = true
[remote "github"]
        url = git@github.com:Heriam/heriam.github.io.git
        fetch = +refs/heads/*:refs/remotes/github/*
[remote "coding"]
        url = git@git.coding.net:Heriam/heriam.git
        fetch = +refs/heads/*:refs/remotes/coding/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
```
<br>    
2. 然后将仓库 push 到 Coding上，在Coding新建一个 coding-pages 分支：    

```
git push -u coding master:coding-pages
```
<br>    
3. 这时登录Coding就可以看到博客内容已经被拷贝到coding-pages分支。
    <br>   

***
**四、配置域名**
***
1. 登录到网站的域名解析管理页面（我用的是DNSPOD，后来转向Cloudxns），然后添加两条域名解析记录：

```
@       CNAME  国内  coding.me
www     CNAME  国内  coding.me
```
<br>   

2. 在Coding 上“项目管理”中找到“自定义域名／Pages”，添加要绑定的域名，比如我是 [jiang-hao.com](https://jiang-hao.com)和[www.jiang-hao.com](https://jiang-hao.com)。注意这些域名也就是我们刚刚在dnspod中设置的解析域名。

<br>   

***
**五、配置Pelican实现同步提交**
***
设置一键上传：（如有疑问参见[《Pelican＋Github博客搭建详细教程》](<https://jiang-hao.com/articles/2018/blog-%E4%BD%BF%E7%94%A8Pelican%E5%9F%BA%E4%BA%8EGithubPages%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2%E6%95%99%E7%A8%8B.html>)第三部分第4点）打开根目录下的Makefile文件，修改以下三个地方：   
<br>    

- OUTPUTDIR        

```
OUTPUTDIR=$(BASEDIR)/output/<username>.github.io    #本地博客仓库路径
```
<br>   
-  publish    

```
publish:    
 $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)    
```
<br>   
- github: publish

```
github: publish
	cd $(OUTPUTDIR) ; git add . ; git commit -am '<添加自己的备注>' ; git push github master:master ; git push coding master:coding-pages 
```

<br>
这样 ，通过`make github`命令就能一键发布博客更新到Github和Coding了。