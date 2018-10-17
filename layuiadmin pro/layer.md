# layer

## 使用layer

~~~javascript
layui.use('layer', function(){
  var layer = layui.layer;
  
  layer.msg('hello');
});    
~~~

## 基础参数

基础参数主要指调用方法时用到的配置项，如：layer.open({content: ''})layer.msg('', {time: 3})等，其中的content和time即是基础参数，以键值形式存在，基础参数可合理应用于任何层类型中，您不需要所有都去配置，大多数都是可选的。

### type - 基本层类型

类型：Number，默认：0

0（信息框，默认）1（页面层）2（iframe层）3（加载层）4（tips层）。

	layer.open({type:1});

### title - 标题

类型：String/Array/Boolean，默认：'信息'

	layer.open({title: '在线调试'});
	layer.open({title: ['文本', 'font-size:18px;']});
	layer.open({title: false});