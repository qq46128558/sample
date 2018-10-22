# form 表单模块

## 使用

页面元素的表单

	layui.use('form', function(){
	  var form = layui.form;
	  //各种基于事件的操作，下面会有进一步介绍
	});

## 更新渲染
	
	// type可选,默认全部刷新,可局部刷新:select/checkbox/radio
	form.render(type, filter);

## 预设元素属性

lay-verify、lay-skin、lay-filter、lay-submit 等, 他们可以使得一些交互操作交由form模块内部、或者你来借助form提供的JS接口精确控制

|属性名|值|说明
|-|-|-
|title|任意字符|设定元素名称
|lay-skin|switch/primary|定义元素的风格，目前只对 checkbox 元素有效
|lay-ignore|任意字符或不设值|是否忽略元素美化处理
|lay-filter|任意字符|事件过滤器，主要用于事件的精确匹配，跟选择器是比较类似的
|lay-verify|required/phone/email/url/number/date/identity/自定义值|同时支持多条规则的验证用丨分隔,自定义需要借助form.verify()方法,详见表单验证
|lay-verType|tips/alert/msg|用于定义异常提示层模式
|lay-submit|无需填写值|绑定触发提交的元素，如button

## 事件监听

	form.on('event(filter)', callback);

|event|描述
|-|-
|select|监听select下拉选择事件
|checkbox|监听checkbox复选框勾选事件
|switch|监听checkbox复选框开关事件
|radio|监听radio单选框事件
|submit|监听表单提交事件

### 监听select选择
	
	form.on('select(filter)', function(data){
	  console.log(data.elem); //得到select原始DOM对象
	  console.log(data.value); //得到被选中的值
	  console.log(data.othis); //得到美化后的DOM对象
	});     

### 监听checkbox复选

	form.on('checkbox(filter)', function(data){
	  console.log(data.elem); //得到checkbox原始DOM对象
	  console.log(data.elem.checked); //是否被选中，true或者false
	  console.log(data.value); //复选框value值，也可以通过data.elem.value得到
	  console.log(data.othis); //得到美化后的DOM对象
	});     

### 监听switch开关

	form.on('switch(filter)', function(data){
	  console.log(data.elem); //得到checkbox原始DOM对象
	  console.log(data.elem.checked); //开关是否开启，true或者false
	  console.log(data.value); //开关value值，也可以通过data.elem.value得到
	  console.log(data.othis); //得到美化后的DOM对象
	});  

### 监听radio单选

	form.on('radio(filter)', function(data){
	  console.log(data.elem); //得到radio原始DOM对象
	  console.log(data.value); //被点击的radio的value值
	});  

### 监听submit提交

	回调函数只有在验证全部通过后才会进入

	form.on('submit(filter)', function(data){
	  console.log(data.elem) //被执行事件的元素DOM对象，一般为button对象
	  console.log(data.form) //被执行提交的form对象，一般在存在form标签时才会返回
	  console.log(data.field) //当前容器的全部表单字段，名值对形式：{name: value}
	  return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
	});

## 表单初始赋值
	
	form.val('filter', object); //object键值对

## 表单验证
	
	<input type="text" lay-verify="required|phone|number">

### 自定义验证规则

~~~javascript
form.verify({
  username: function(value, item){ //value：表单的值、item：表单的DOM对象
    if(!new RegExp("^[a-zA-Z0-9_\u4e00-\u9fa5\\s·]+$").test(value)){
      return '用户名不能有特殊字符';
    }
    if(/(^\_)|(\__)|(\_+$)/.test(value)){
      return '用户名首尾不能出现下划线\'_\'';
    }
    if(/^\d+\d+\d$/.test(value)){
      return '用户名不能全为数字';
    }
  }
  
  //我们既支持上述函数式的方式，也支持下述数组的形式
  //数组的两个值分别代表：[正则匹配、匹配不符时的提示文字]
  ,pass: [
    /^[\S]{6,12}$/
    ,'密码必须6到12位，且不能出现空格'
  ] 
});    
~~~

~~~html
<input type="text" lay-verify="username" placeholder="请输入用户名">
<input type="password" lay-verify="pass" placeholder="请输入密码">
~~~
