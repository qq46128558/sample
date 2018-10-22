# code 代码修饰器

该模块就是对你的pre元素进行一个修饰，从而保证你展现的代码更具可读性

## 使用

~~~html
<pre class="layui-code">
//代码区域
var a = 'hello layui';
</pre>     
~~~

~~~javascript
layui.use('code', function(){ //加载code模块
  layui.code(); //引用code方法
});
~~~

## 基础参数

	layui.code(options)

~~~html
elem	string	指定元素的选择器
title	string	设定标题
height	string	设置最大高度 //请注意必须加px。如果该key不设定，则会自适应高度，且不会出现滚动条。
encode	boolean	是否转义html标签，默认false
skin	string	风格选择,内置了两种，分别为默认和notepad
about	boolean	是否剔除右上关于
~~~

> 特别提示：除了上述方式的设置，我们还允许你直接在pre标签上设置属性来替代，如：

~~~html
<pre class="layui-code" lay-title="" lay-height="" lay-skin="" lay-encode="">
这样有木有觉得更方便些
</pre>     
~~~

## 指定元素

code模块会去自动查找class为layui-code的类，如果你初始给的不是该类，仅仅只是一个pre标签，那么需要通过elem设置选择器来指向元素：

	layui.code({
	  elem: 'pre' //默认值为.layui-code
	});

## 转义html标签

事实上很多时候你都需要在pre标签中展现html标签，而不希望它被浏览器解析。那么code模块允许你这么做，只需要开启encode即可
	
	encode: true //是否转义html标签。默认不开启
