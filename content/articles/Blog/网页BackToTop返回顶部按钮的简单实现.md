Title: 网页 BacktoTop 返回顶部按钮的简单实现
Date:2017-06-30
Tags: HTML, JavaScript, CSS

在较长的网页页面中往往需要一个固定漂浮在显示屏右下侧位置的返回顶部按钮。

下面介绍一种简单实现：

**HTML 部分：**  

```html
<body>
  <a href="javascript:void(0);" id="scroll" title="Scroll to Top" style="display: none;">Top<span></span></a>
  ...
</body>
```

**CSS 部分：**

```css
#scroll {
    position:fixed;
    right:10px;
    bottom:10px;
    cursor:pointer;
    width:50px;
    height:50px;
    background-color:#2E435E;
    text-indent:-9999px;
    display:none;
    -webkit-border-radius:5px;
    -moz-border-radius:5px;
    border-radius:5px;
}
#scroll span {
    position:absolute;
    top:50%;
    left:50%;
    margin-left:-8px;
    margin-top:-12px;
    height:0;
    width:0;
    border:8px solid transparent;
    border-bottom-color:#ffffff
}
#scroll:hover {
    background-color:#3498db;
    opacity:1;
    filter:"alpha(opacity=100)";
    -ms-filter:"alpha(opacity=100)";
}
```

**JavaScript 部分：**

```javascript
$(document).ready(function(){
    $(window).scroll(function(){
        if($(this).scrollTop() > 100){
            $('#scroll').fadeIn();
        }else{
            $('#scroll').fadeOut();
        }
    });
    $('#scroll').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
});
```

最后的显示效果可以参照本博客：）

