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

## 表单

依赖加载模块：form

~~~html
<form class="layui-form layui-form-pane" action="">
	<div class="layui-form-item">
    	<label class="layui-form-label">输入框</label>
    	<div class="layui-input-block">
      		<input type="text" name="title" required  lay-verify="required" placeholder="请输入标题" autocomplete="off" class="layui-input">
    	</div>
    </div>
    <div class="layui-form-item">
	    <div class="layui-input-block">
	      <button class="layui-btn" lay-submit lay-filter="formDemo">立即提交</button>
	      <button type="reset" class="layui-btn layui-btn-primary">重置</button>
	    </div>
  	</div>
</form>
~~~

## 导航

依赖加载模块：element

~~~html
<ul class="layui-nav layui-nav-tree layui-nav-side">
  <li class="layui-nav-item layui-nav-itemed">
    <a href="javascript:;">默认展开</a>
    <dl class="layui-nav-child">
      <dd><a href="javascript:;">选项1</a></dd>
      <dd><a href="javascript:;">选项2</a></dd>
      <dd><a href="">跳转</a></dd>
    </dl>
  </li>
</ul>
~~~

面包屑

~~~html
<span class="layui-breadcrumb">
  <a href="">首页</a>
  <a href="">国际新闻</a>
  <a href="">亚太地区</a>
  <a><cite>正文</cite></a>
</span>
~~~

## 选项卡

依赖加载组件：element

~~~html
<div class="layui-tab">
  <ul class="layui-tab-title">
    <li class="layui-this">网站设置</li>
    <li>用户管理</li>
    <li>权限分配</li>
    <li>商品管理</li>
    <li>订单管理</li>
  </ul>
  <div class="layui-tab-content">
    <div class="layui-tab-item layui-show">内容1</div>
    <div class="layui-tab-item">内容2</div>
    <div class="layui-tab-item">内容3</div>
    <div class="layui-tab-item">内容4</div>
    <div class="layui-tab-item">内容5</div>
  </div>
</div>
~~~

## 进度条

依赖加载组件：element

~~~html
<div class="layui-progress">
  <div class="layui-progress-bar" lay-percent="10%"></div>
</div>
~~~

## 面板

依赖加载组件：element

~~~html
<div class="layui-card">
  <div class="layui-card-header">卡片面板</div>
  <div class="layui-card-body">
    卡片式面板面板通常用于非白色背景色的主体内<br>
    从而映衬出边框投影
  </div>
</div>
~~~

折叠面板

~~~html
<div class="layui-collapse">
  <div class="layui-colla-item">
    <h2 class="layui-colla-title">杜甫</h2>
    <div class="layui-colla-content layui-show">内容区域</div>
  </div>
  <div class="layui-colla-item">
    <h2 class="layui-colla-title">李清照</h2>
    <div class="layui-colla-content layui-show">内容区域</div>
  </div>
  <div class="layui-colla-item">
    <h2 class="layui-colla-title">鲁迅</h2>
    <div class="layui-colla-content layui-show">内容区域</div>
  </div>
</div>
~~~

## 表格

	<table class="layui-table">
	<table lay-even lay-skin="line" lay-size="lg">

## 徽章

	<span class="layui-badge-dot"></span>
	<span class="layui-badge">6</span>
	<span class="layui-badge-rim">6</span>

## 时间线

~~~html
<ul class="layui-timeline">
  <li class="layui-timeline-item">
    <i class="layui-icon layui-timeline-axis">&#xe63f;</i>
    <div class="layui-timeline-content layui-text">
      <h3 class="layui-timeline-title">8月18日</h3>
      <p>
        layui 2.0 的一切准备工作似乎都已到位。发布之弦，一触即发。
        <br>不枉近百个日日夜夜与之为伴。因小而大，因弱而强。
        <br>无论它能走多远，抑或如何支撑？至少我曾倾注全心，无怨无悔 <i class="layui-icon"></i>
      </p>
    </div>
  </li>
</ul>
~~~

## 辅助

	<blockquote class="layui-elem-quote">引用区域的文字</blockquote>
	<blockquote class="layui-elem-quote layui-quote-nm">引用区域的文字</blockquote>
	<hr class="layui-bg-red">
	
字段集区块

~~~html
<fieldset class="layui-elem-field">
  <legend>字段集区块 - 默认风格</legend>
  <div class="layui-field-box">
    内容区域
  </div>
</fieldset>
~~~