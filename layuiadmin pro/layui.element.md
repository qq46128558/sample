# element 常用元素操作

## 使用

元素功能的开启只需要加载element模块即会自动完成，所以不用跟其它模块一样为某一个功能而调用一个方法。她只需要找到她支持的元素，如你的页面存在一个 Tab元素块，那么element模块会自动赋予她该有的功能。

	layui.use('element', function(){
	  var element = layui.element;
	  
	  //一些事件监听
	  element.on('tab(demo)', function(data){
	    console.log(data);
	  });
	});

## 预设元素属性

|属性名|值|说明
|-|-|-
|lay-filter|任意字符|事件过滤器（公用属性），主要用于事件的精确匹配，跟选择器是比较类似的。
|lay-allowClose|true|针对于Tab容器，是否允许选项卡关闭。默认不允许，即不用设置该属性
|lay-separator|任意分隔符|针对于面包屑容器

## 基础方法

基础方法允许你在外部主动对元素发起一起操作，目前element模块提供的方法如下：

- var element = layui.element; 		element模块的实例 
- element.on(event(filter), callback); 	用于元素的一些事件监听
- element.tabAdd(filter, options);	用于新增一个Tab选项,options:title/content/id
- element.tabDelete(filter, layid);	用于删除指定的Tab选项 
- element.tabChange(filter, layid);	用于外部切换到指定的Tab项上
- element.tab(options);				用于绑定自定义 Tab 元素
- element.progress(filter, percent); 用于动态改变进度条百分比： 

## 更新渲染

跟表单元素一样，很多时候你的页面元素可能是动态生成的，这时element的相关功能将不会对其有效，你必须手工执行 element.init(type, filter) 方法即可。注意：2.1.6 开始，可以用 element.render(type, filter); 方法替代

第一个参数：type，为表单的type类型，可选。默认对全部类型的表单进行一次更新。可局部刷新的type如下表：

- tab	重新对tab选项卡进行初始化渲染
- nav	重新对导航进行渲染
- breadcrumb	重新对面包屑进行渲染
- progress	重新对进度条进行渲染
- collapse	重新对折叠面板进行渲染

## 事件监听

	element.on('event(filter)', callback);

### 监听选项卡切换
	
	element.on('tab(filter)', function(data){
	  console.log(this); //当前Tab标题所在的原始DOM元素
	  console.log(data.index); //得到当前Tab的所在下标
	  console.log(data.elem); //得到当前的Tab大容器
	});

### 监听选项卡删除

	element.on('tabDelete(filter)', function(data){
	  console.log(this); //当前Tab标题所在的原始DOM元素
	  console.log(data.index); //得到当前Tab的所在下标
	  console.log(data.elem); //得到当前的Tab大容器
	});
     
### 监听导航菜单的点击

	element.on('nav(filter)', function(elem){
	  console.log(elem); //得到当前点击的DOM对象
	});

### 监听折叠面板

	element.on('collapse(filter)', function(data){
	  console.log(data.show); //得到当前面板的展开状态，true或者false
	  console.log(data.title); //得到当前点击面板的标题区域DOM对象
	  console.log(data.content); //得到当前点击面板的内容区域DOM对象
	});

