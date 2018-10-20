# laydate 日期和时间组件

## 快速使用

~~~html
<div class="layui-inline">
	<input type="text" class="layui-input" id="test1">
</div>
<script>
layui.use('laydate',function(){
	var laydate=layui.laydate;
	laydate.render({
		elem:'#test' // 指定元素
	});
});
</script>
~~~

## 基础参数选项
	
	laydate.render(options)
	laydate.set(options)

### elem 绑定元素

string/dom,无(默认值)

### type 控件选择类型

string,date
	
	year/month/date/time/datetime

### range 开启左右面板范围选择

boolean/string,false
	
	range:"~" // 自定义分割字符

### format 自定义格式

string,yyyy-MM-dd

	y年M月d日H小时m分钟s秒

### value 初始值

string,new Date()

	value:'2018-08-18' // 遵循format格式

### isInitValue 初始值填充

boolean,true

### min/max 最小/大范围内的日期时间值

string,min:'1900-1-1',max:'2099-12-31'

并非遵循format设定的格式

### trigger 自定义弹出控件的事件

string,focus(绑定元素非输入框,则为click)

### show 默认显示

boolean,false

	,show:true,closeStop:'#test1' //阻止关闭事件冒泡

### position 定位方式

string,absolute

	absolute:绝对定位
	fixed:固定位置(不随浏览器滚动)
	static:静态定位(嵌套在指定容器中) 配合change监听

### zIndex 层叠顺序

number,66666666

### showBottom 是否显示底部栏

boolean,true

### btns 工具按钮

array,['clear','now','confirm']

### lang 语言

string,cn

	,lang:'en'

### theme 主题

string,default

	default 默认简约
	molv 墨绿背景
	#颜色值
	grid 格子主题

### calendar 是否显示公/历节日

boolean,false

### mark 标注重要日子

object,无

	,mark:{'0-0-20':'工资'} // 每个月20号

## 控件初始打开的回调

	,ready:funciton(date){}

## 日期时间被切换后的回调

	,change:function(value,date,endDate){} //值,日期对象,range为true时返回

## 控件选择完毕后的回调

	,done:function(value,date,endDate){}

## 弹出控件提示
	
	var ins1=laydate.render({
		elem:'#test1'
		,change:function(value,date,endDate){
			ins1.hint(value); //在控件上弹出value值
		}
		})

## 其他方法
	
	laydate.getEndDate(month,year) // 获取指定年月的最后一天