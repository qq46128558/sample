# carousel 通用轮播组件

## 快速使用

~~~html
<div class="layui-carousel" id="test1">
  <div carousel-item>
    <div>条目1</div>
    <div>条目2</div>
    <div>条目3</div>
    <div>条目4</div>
    <div>条目5</div>
  </div>
</div>
<!-- 条目中可以是任意内容，如：<img src=""> -->
~~~

~~~javascript
<script>
layui.use('carousel', function(){
  var carousel = layui.carousel;
  //建造实例
  carousel.render({
    elem: '#test1'
    ,width: '100%' //设置容器宽度
    ,arrow: 'always' //始终显示箭头
    //,anim: 'updown' //切换动画方式
  });
});
</script>
~~~

## 基础参数

通过核心方法：carousel.render(options) 来对轮播设置基础参数，也可以通过方法：carousel.set(options) 来设定全局基础参数

~~~html
elem	指向容器选择器，如：elem: '#id'。也可以是DOM对象	string/object	无

width	设定轮播容器宽度，支持像素和百分比	string	'600px'

height	设定轮播容器高度，支持像素和百分比	string	'280px'

full	是否全屏轮播	boolean	false

anim	轮播切换动画方式，可选值为：
default（左右切换）
updown（上下切换）
fade（渐隐渐显切换）
string	'default'

autoplay	是否自动切换	boolean	true

interval	自动切换的时间间隔，单位：ms（毫秒），不能低于800	number	3000

index	初始开始的条目索引	number	0

arrow	切换箭头默认显示状态，可选值为：
hover（悬停显示）
always（始终显示）
none（始终不显示）
string	'hover'

indicator	指示器位置，可选值为：
inside（容器内部）
outside（容器外部）
none（不显示）
注意：如果设定了 anim:'updown'，该参数将无效	string	'inside'

trigger	指示器的触发事件	string	'click'
~~~

## 切换事件

轮播的每一次切换时触发

~~~javascript
var carousel = layui.carousel;
 
//监听轮播切换事件
carousel.on('change(test1)', function(obj){ //test1来源于对应HTML容器的 lay-filter="test1" 属性值
  console.log(obj.index); //当前条目的索引
  console.log(obj.prevIndex); //上一个条目的索引
  console.log(obj.item); //当前条目的元素对象
});     
~~~

## 重置轮播
	
	var ins = carousel.render(options);
	//重置轮播
	ins.reload(options);