# slider 滑块

## 使用
	
	<div id="slideTest1"></div>
	<script>
	layui.use('slider', function(){
	  var slider = layui.slider;
	  
	  //渲染
	  slider.render({
	    elem: '#slideTest1'  //绑定元素
	  });
	});
	</script>

## 基础参数

~~~html
elem	指向容器选择器	string/object	-

type	滑块类型，可选值有：default（水平滑块）、vertical（垂直滑块）	string	default

min	滑动条最小值，正整数，默认为 0	number	0

max	滑动条最大值	number	100

range	是否开启滑块的范围拖拽，若设为 true，则滑块将出现两个可拖拽的环	boolean	false

value	滑块初始值，默认为数字，若开启了滑块为范围拖拽（即 range: true），则需赋值数组，异表示开始和结尾的区间，如：value: [30, 60]	number/Array	0

step	拖动的步长	number	1

showstep	是否显示间断点	boolean	false

tips	是否显示文字提示	boolean	true

input	是否显示输入框（注意：若 range 参数为 true 则强制无效） 
点击输入框的上下按钮，以及输入任意数字后回车或失去焦点，均可动态改变滑块	boolean	false

height	滑动条高度，需配合 type:"vertical" 参数使用	number	200

disabled	是否将滑块禁用拖拽	boolean	false

theme	主题颜色，以便用在不同的主题风格下	string	#009688
~~~

## 自定义提示文本

当鼠标放在圆点和滑块拖拽时均会触发提示层。其默认显示的文本是它的对应数值，你也可以自定义提示内容：

	slider.render({
	  elem: '#slideTest1'
	  ,setTips: function(value){ //自定义提示文本
	    return value + '%';
	  }
	});
      
## 数值改变的回调

~~~javascript
//当滑块为普通模式，回调返回的 value 是一个数值
slider.render({
  elem: '#slideTest1'
  ,change: function(value){
    console.log(value) //动态获取滑块数值
    //do something
  }
});
 
//当滑块为范围模式，回调返回的 value 是一个数组，包含开始和结尾
slider.render({
  elem: '#slideTest1'
  ,range: true
  ,change: function(value){
    console.log(value[0]) //得到开始值
    console.log(value[1]) //得到结尾值
    //do something
  }
});
~~~

## 实例方法

	var ins1 = slider.render(options); //获得实例对象
	ins1.config //获得当前实例的配置项
	ins1.setValue(nums); //动态给滑块赋值

### 动态改变滑块数值
	
	//改变指定滑块实例的数值
	ins1.setValue(20)

	//若滑块开启了范围（range: true）
	ins1.setValue(20, 0) //设置开始值
	ins1.setValue(60, 1) //设置结尾值

