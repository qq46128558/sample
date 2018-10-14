# layui css

## CSS内置公共基础类

~~~html
layui-main	用于设置一个宽度为 1140px 的水平居中块（无响应式）
layui-inline	用于将标签设为内联块状元素
layui-box	用于排除一些UI框架（如Bootstrap）强制将全部元素设为box-sizing: border-box所引发的尺寸偏差
layui-clear	用于消除浮动（一般不怎么常用，因为layui几乎没用到浮动）
layui-btn-container	用于定义按钮的父容器。（layui 2.2.5 新增）
layui-btn-fluid	用于定义流体按钮。即宽度最大化适应。（layui 2.2.5 新增）

layui-icon	用于图标
layui-elip	用于单行文本溢出省略
layui-unselect	用于屏蔽选中
layui-disabled	用于设置元素不可点击状态
layui-circle	用于设置元素为圆形
layui-show	用于显示块状元素
layui-hide	用于隐藏元素

layui-text	定义一段文本区域（如文章），该区域内的特殊标签（如a、li、em等）将会进行相应处理
layui-word-aux	灰色标注性文字，左右会有间隔

layui-bg-red	用于设置元素赤色背景
layui-bg-orange	用于设置元素橙色背景
layui-bg-green	用于设置元素墨绿色背景（主色调）
layui-bg-cyan	用于设置元素藏青色背景
layui-bg-blue	用于设置元素蓝色背景
layui-bg-black	用于设置元素经典黑色背景
layui-bg-gray	用于设置元素经典灰色背景
~~~

## 常用公共属性

~~~html
lay-skin=" "	定义相同元素的不同风格，如checkbox的开关风格
lay-filter=" "	事件过滤器。你可能会在很多地方看到他，他一般是用于监听特定的自定义事件。你可以把它看作是一个ID选择器
lay-submit	定义一个触发表单提交的button，不用填写值
~~~

## 布局
	
	采用 layui-row 来定义行，如：<div class="layui-row"></div>
	采用类似 layui-col-md* 这样的预设类来定义一组列（column），且放在行（row）内
	可对列追加类似 layui-col-space5、 layui-col-md-offset3 这样的预设类来定义列的间距和偏移。
	最后，在列（column）元素中放入你自己的任意元素填充内容，完成布局！

## 内置背景色
	
	class="layui-bg-black"

## 图标
	
	<i class="layui-icon layui-icon-face-smile"></i>   
	<i class="layui-icon layui-icon-face-smile" style="font-size: 30px; color: #1E9FFF;"></i>  

## 动画

	<div class="layui-anim layui-anim-up layui-anim-loop"></div>

## 按钮
	<button class="layui-btn">一个标准的按钮</button>
	<a href="http://www.layui.com" class="layui-btn">一个可跳转的按钮</a>
