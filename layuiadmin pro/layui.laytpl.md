# laytpl 模板引擎

## 快速使用

~~~javascript
// 1:编写模板,使用script标签
<script id="demo" type="text/html">
	<h3>{{d.title}}</h3>
	...
</script>
// 2:建立视图,用于呈现渲染结果
<div id="view"></div>
//3:渲染模板
<script>
var data={
	"title":"XXXX"
}
var getTpl=demo.innerHTML,view=document.getElementById('view');
laytpl(getTpl).render(data,function(html){
	view.innerHTML=html;
})
</script>
~~~

## 模板语法

|语法|说明
|-|-
|{{d.field}}|输出一个普通字段,不转义html
|{{=d.field}}|同上,转义html
|{{# javascript表达式}}|js语句,一般用于逻辑处理(输出函数写{{ fn() }} 未理解)
|{{! template !}}|不解析该区域,即原樣呈現出來,暫未知應用場景

## 分隔符

可以重新定义默认分隔符{{ }}

~~~javascript
laytpl.config({
	open:'<%',
	close:'%>'
});
~~~

