Title: JQCloud: 一个前端生成美化标签云的简单JQuery插件
Date: 2018-02-25
Tags: JQCloud, JQuery, TagCloud

因为博客需要，发现了一个生成美化简约风格的标签云的JQuery插件。
官网地址：[http://mistic100.github.io/jQCloud/index.html](http://mistic100.github.io/jQCloud/index.html)

使用方法很简单，可以把JS和CSS文件下载到本地，也可以直接通过Script标签src=“”的方法在线引用。

具体的使用方法官网都能查到。

贴出自己微博使用JQCloud的前端代码：

```HTML
<script src="{{ SITEURL }}/theme/jqcloud.js"></script>
<link href="{{ SITEURL }}/theme/jqcloud.css" rel="stylesheet">
<script>
    var words = [];
    {% for tag, articles in tags|sort %}
    	words.push({text: "{{tag}}", weight: Math.random(), link: '{{ SITEURL }}/{{ tag.url }}'});
	{% endfor %}
    {% for category, articles in categories %}
    	words.push({text: "{{category}}", weight: Math.random(), link: '{{ SITEURL }}/{{ category.url }}'});
	{% endfor %}
    $(function() {
        $("#tagcloud").jQCloud(words, {
	  		autoResize: true
		});	
    });
</script>
<div id="tagcloud" style="width: 80%; height: 450px; align-self: center;"></div>
```

需要注意的是要包含标签云的div模块需要显示指定width和height，否则需要在JavaScript中进行相关设置。