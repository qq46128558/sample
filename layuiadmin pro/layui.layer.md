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

### content - 内容

类型：String/DOM/Array，默认：''

	layer.open({content:'传入任意的文本或html'})

### skin - 样式类名

类型：String，默认：'' (借助skin完成不同的风格定制)

	layer.open({skin: 'demo-class'});

### area - 宽高

类型：String/Array，默认：'auto'

	area: ['500px', '300px']

### offset - 坐标

类型：String/Array，默认：垂直水平居中

	offset: ['100px', '50px']

### icon - 图标。信息框和加载层的私有参数

类型：Number，默认：-1（信息框）/0（加载层）

信息框默认不显示图标。当你想显示图标时，默认皮肤可以传入0-6如果是加载层，可以传入0-2

	layer.msg('不开心。。', {icon: 5});

### btn - 按钮

类型：String/Array，默认：'确认'

	btn: ['按钮1', '按钮2', '按钮3', …]
	// 按钮1的回调是yes，而从按钮2开始，则回调为btn2: function(){}，以此类推
	,yes: function(index, layero){}
	,btn2: function(index, layero){}
	,btn3: function(index, layero){}
	,cancel: function(){} //右上角关闭回调 
	// return false 开启该代码可禁止点击该按钮关闭

### yes - 确定按钮回调方法

类型：Function，默认：null
	
	// //如果设定了yes回调，需进行手工关闭
	yes: function(index, layero){layer.close(index);}

### cancel - 右上角关闭按钮触发的回调

类型：Function，默认：null

	cancel: function(index, layero){ }

### btnAlign - 按钮排列

类型：String，默认：r

	btnAlign: 'c' // 按钮居中对齐

### closeBtn - 关闭按钮

类型：String/Boolean，默认：1

	closeBtn: 0 // 不显示

### shade - 遮罩

类型：String/Array/Boolean，默认：0.3 (弹层外区域)

	shade: [0.8, '#393D49'] // 定义别的颜色
	shade: 0 // 不想显示遮罩

### shadeClose - 是否点击遮罩关闭

类型：Boolean，默认：false (设定shadeClose来控制点击弹层外区域关闭。)

### time - 自动关闭所需毫秒

类型：Number，默认：0

	time: 5000，// 即代表5秒后自动关闭

### id - 用于控制弹层唯一标识

类型：String，默认：空字符

### anim - 弹出动画

类型：Number，默认：0 (平滑放大)

	anim: -1  // 不想显示动画
	anim: 5	// 渐显
	anim: 6	// 抖动

### isOutAnim - 关闭动画 （layer 3.0.3新增）

类型：Boolean，默认：true (关闭层时会有一个过度动画)

### maxmin - 最大最小化

类型：Boolean，默认：false

	maxmin: true // 该参数值对type:1和type:2有效

### fixed - 固定

类型：Boolean，默认：true

	fixed: false // 层是否固定在可视区域

### resize - 是否允许拉伸

类型：Boolean，默认：true (该参数对loading、tips层无效)

### resizing - 监听窗口拉伸动作

类型：Function，默认：null

	resizing: function(layero){console.log(layero);}  // 回调返回一个参数：当前层的DOM对象

### scrollbar - 是否允许浏览器出现滚动条

类型：Boolean，默认：true

### maxWidth - 最大宽度

类型：Number，默认：360 (只有当area: 'auto'时，maxWidth的设定才有效。)

### maxHeight - 最大高度

类型：Number，默认：无 (只有当高度自适应时，maxHeight的设定才有效。)

### zIndex - 层叠顺序

类型：，默认：19891014

### move - 触发拖动的元素

类型：String/DOM/Boolean，默认：'.layui-layer-title'

	move: '.mine-move' // 指向元素的选择器或者DOM
	move: false // 禁止拖拽

### moveOut - 是否允许拖拽到窗口外

类型：Boolean，默认：false

### moveEnd - 拖动完毕后的回调方法

类型：Function，默认：null

	moveEnd: function(layero){}

### tips - tips方向和颜色

类型：Number/Array，默认：2 (支持上右下左四个方向，通过1-4进行方向设定)
	
	tips: 3 // 则表示在元素的下面出现
	tips: [1, '#c00'] // 定义一些颜色

### tipsMore - 是否允许多个tips

类型：Boolean，默认：false

### success - 层弹出后的成功回调方法

类型：Function，默认：null

	success: function(layero, index){console.log(layero, index);}

### end - 层销毁后触发的回调

类型：Function，默认：null

### full/min/restore -分别代表最大化、最小化、还原 后触发的回调

类型：Function，默认：null (携带一个参数，即当前层DOM)

## layer.config(options) - 初始化全局配置

可以配置一些诸如路径、加载的模块，甚至还可以决定整个弹层的默认参数

如果采用 layui 加载 layer，无需设置 path。所以前置工作都是自动完成

	layer.config({
	  anim: 1, //默认动画风格
	  skin: 'layui-layer-molv' //默认皮肤
	  …
	});

## layer.ready(callback) - 初始化就绪

当你在页面一打开就要执行弹层时，你最好是将弹层放入ready方法中

	layer.ready(function(){
	  layer.msg('很高兴一开场就见到你');
	});     

## layer.open(options) - 原始核心方法

不管是使用哪种方式创建层，都是走layer.open()，创建任何类型的弹层都会返回一个当前层索引，上述的options即是基础参数

	var index = layer.open({
	  content: 'test'
	});

## layer.alert(content, options, yes) - 普通信息框
	
一般用于对用户造成比较强烈的关注，类似系统alert

	layer.alert('只想简单的提示');   

## layer.confirm(content, options, yes, cancel) - 询问框

不是和系统的confirm一样阻塞,你需要把交互的语句放在回调体中
	
	layer.confirm('is not?', {icon: 3, title:'提示'}, function(index){
	  //do something
	  layer.close(index);
	});

## layer.msg(content, options, end) - 提示框

露脸率最高的提示框

	layer.msg('只想弱弱提示');

## layer.load(icon, options) - 加载层

type:3的深度定制 (load默认是不会自动关闭的，因为你一般会在ajax回调体中关闭它)

	var index = layer.load(2, {time: 10*1000}); //又换了种风格，并且设定最长等待10秒 
	//关闭
	layer.close(index);    

## layer.tips(content, follow, options) - tips层

type:4的深度定制(默认是在元素右边弹出)

	layer.tips('只想提示地精准些', '#id');

## layer.close(index) - 关闭特定层

	layer.close(layer.index); //它获取的始终是最新弹出的某个层，值是由layer内部动态递增计算的
	var index = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
	parent.layer.close(index); //再执行关闭   

## layer.closeAll(type) - 关闭所有层
	
	layer.closeAll('dialog'); //关闭信息框
	layer.closeAll('page'); //关闭所有页面层
	layer.closeAll('iframe'); //关闭所有的iframe层
	layer.closeAll('loading'); //关闭加载层
	layer.closeAll('tips'); //关闭所有的tips层  

## layer.style(index, cssStyle) - 重新定义层的样式

该方法对loading层和tips层无效。参数index为层的索引，cssStyle允许你传入任意的css属性

	//重新给指定层设定width、top等
	layer.style(index, {
	  width: '1000px',
	  top: '10px'
	});    

## layer.title(title, index) - 改变层的标题

	layer.title('标题变了', index)

## layer.getChildFrame(selector, index) - 获取iframe页的DOM

当你试图在当前页获取iframe页的DOM元素时，你可以用此方法。selector即iframe页的选择器

## layer.getFrameIndex(windowName) - 获取特定iframe层的索引

此方法一般用于在iframe页关闭自身时用到。

## layer.iframeAuto(index) - 指定iframe层自适应

## layer.iframeSrc(index, url) - //重置特定iframe url

## layer.setTop(layero) -置顶当前窗口

## layer.full()、layer.min()、layer.restore() - 手工执行最大小化

## layer.prompt(options, yes) - 输入层

yes携带value 表单值index 索引elem 表单元素

## layer.tab(options) - tab层

tab层只单独定制了一个成员，即tab: []

## layer.photos(options) - 相册层

相册层，也可以称之为图片查看器 (photos还有个tab回调，切换图片时触发)

	layer.photos({
	  photos: json/选择器,
	  tab: function(pic, layero){
	    console.log(pic) //当前图片的一些信息
	  }
	});