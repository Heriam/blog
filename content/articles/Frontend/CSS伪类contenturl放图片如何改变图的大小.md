Title: CSS伪类content: url放图片如何改变图的大小
Date: 2017-02-21
Tags: CSS

遇到过一个问题：用before after 之类的伪类的content里放一个图的链接，如何去改图的大小？比如：

```CSS
.nav ul li:after{
  content: url(../img/nav_fg.png);
}
```

事实上，如果想要设置前端页面通过content：url显示出来的图片大小，那只能修改图片的大小。因为它是直接读取的图片，并不是代入到html中再显示出来。但可以采用background的方式调整图片的大小，比如本博客中学术社交网站ResearchGate的Logo的CSS显示代码如下：

```CSS
.social a[href*='researchgate.net']:before {
  background-image: url('./images/icons/researchgate.png'); 
  background-size: 100%; 
  display: inline-block; 
  margin-right: 2px; 
  vertical-align: -3px; 
  height: 16px; 
  width: 16px; 
  content: "";
}
```

其中 content="", height, width, background-size, display, background-image 都必须显示指定。这样，就可以通过 height, width 来分别设置图片的长和宽了。