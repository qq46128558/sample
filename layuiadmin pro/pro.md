# 开发者资料

## 全局配置文件位置
    src/config.js：layuiAdmin 的全局配置文件，可随意修改

## 清除本地储存
    F12/Ctrl+Shift+i>Application页签>Storage>Local Storage>找到地址>选中key(layuiAdmin)[在config.js的tableName配置此名]>点上面的按钮Delete Selected

## js接口文件在start/json/内,返回json格式

## layui.router()
	// 获得当前路由对象
	var router = layui.router();

	path：存储的是路由的目录结构
	search：存储的是路由的参数部分
	href：存储的是 layuiAdmin 的完整路由地址
	hash：存储的是 layuiAdmin 自身的锚记，跟系统自带的 location.hash 有点类似

	// 操作对象
	router.search.uid

## 在动态模板中获取路由参数
	<script type="text/html" template lay-url="./xxx/?uid={{ layui.router().search.uid }}">

## 路由跳转
	通过对任意元素设定 lay-href="/user/set/uid=123/type=1"
	直接对 a 标签设定 href，如： <a href="#/user/set">text</a>
	在 JS 代码中，还可通过 location.hash = '/user/set';
	(input的lay-action,li的data-jump也是路由跳转?

## 路由结尾
	user/set: 读取的视图文件是：.views/user/set.html
	user/set/: 读取的视图文件是：./views/user/set/index.html

## 视图与路由的关系

|视图路径|对应的路由地址
|-|-
|./views/user/index.html|/user/
|./views/user.html|/user
|./views/user/set/index.html|/user/set/
|./views/user/set.html|/user/set
|./views/user/set/base.html|/user/set/base

## 视图中加载 JS 模块

在视图文件中，除了写 HTML，也可以写 JavaScript 代码。如：

~~~html
<div id=“LAY-demo-hello”>Hello layuiAdmin</div>
<script>
layui.use('admin', function(){
  var $ = layui.jquery;
  admin.popup({
    content: $('#LAY-demo-hello').html()
  });
});
</script>
~~~

如果该视图对应的 JS 代码量太大，我们更推荐你在 controller 目录下新增一个业务模块，并在视图中直接 layui.use 去加载该模块。可以以控制台主页 index.html 为例：

~~~html
<div>html区域<div>
<script>
layui.use('console', layui.factory('console'));
</script>
~~~


## 动态模板定义模板

~~~html
<script type="text/html" template>
  <!-- 动态模板碎片 -->
</script>
~~~

## 动态模板读取数据

在不对动态模板设定数据接口地址的情况下，它能读取到全局对象。但更多时候，一个动态模板应该是对应一个接口地址

~~~javascript
<script type="text/html" template lay-url="接口地址">
<a href="javascript:;">
	<cite>{{ d.data.username }}</cite>
</a>
~~~

## 模板基础属性

- lay-url: 用于绑定模板的数据接口地址，支持动态模板解析
- lay-type: 用于设定模板的接口请求类型（默认：get）
- lay-data: 用于定义接口请求的参数，其值是一个 JavaScript object 对象，同样支持动态模板解析
- lay-headers: 用户定义接口请求的 Request Headers 参数，用法与 lay-data 的完全类似，支持动态模板解析
- lay-done: 接口请求完毕并完成视图渲染的回调脚本，里面支持写任意的 JavaScript 语句。事实上它是一个封闭的函数作用域，通过给 Function 实例返回的函数传递一个参数 d，用于得到接口返回的数据

很多时候，你在动态模板中可能会放入一些类似于 layui 的 form 元素，而有些控件需要执行 form.render() 才会显示，这时，你可以对 lay-done 赋值一个全局函数，如：

~~~html
<script type="text/html" template lay-url="接口地址" lay-done="layui.data.done(d);">
   <div class="layui-form" lay-filter="LAY-filter-demo-form">
     <input type="checkbox" title="复选框">
  </div>
</script>

<!--  注意：别看眼花了，下面可不是动态模板，而是 JS 脚本区域 -->
<script>
layui.data.done = function(d){
  layui.use(['form'], function(){
    var form = layui.form;
     form.render(null, 'LAY-filter-demo-form'); //渲染该模板下的动态表单
  });
};
</script>
~~~

## 登录拦截器

进入登入页面登入成功后，会在 localStorage 的本地表中写入一个字段。如： access_token （名称可以在 config.js 自定义）。拦截器判断没有 access_token 时，则会跳转到登入页。尽管可以通过伪造一个假的 access_token 绕过视图层的拦截，但在请求接口时，会自动带上 access_token，服务端应再次做一层校验。

## 登录流程

* 打开 config.js ，将 interceptor 参数设置为 true（该参数为 1.0.0-beta6 开始新增）。那么，当其未检查到 access_token 值时，会强制跳转到登录页面，以获取 access_token。
* 打开登录对应的视图文件 views/user/login.html，在代码最下面，你将看到一段已经写好的代码，你需要的是将接口地址改为服务端的真实接口，并返回 access_token 值。
* layuiAdmin 会将服务端返回的 access_token 值进行本地存储，这时你会发现 layuiAdmin 不再强制跳转到登录页面。并在后面每次请求服务端接口时，都会自动在参数和 Request Headers 中带上 access_token，以便服务端进行鉴权。
* 若鉴权成功，顺利返回数据；若鉴权失败，服务端的 code 应返回 1001（可在 config.js 自定义） ， layuiAdmin 将会自动清空本地无效 token 并跳转到登入页。
* 退出登录：重新打开 controller/common.js，搜索 logout，配上注销接口即可。

> 如果是在其它场景请求的接口（如：table.render()），那么你需要获取本地存储的 token 复制给接口参数，如：

~~~javascript
table.render({
  elem: '#xxxx'
  ,url: 'url'
  ,where: {
    access_token: layui.data('layuiAdmin').access_token
  }
})
~~~

~~~javascript
// table.render登录权限拦截, 需要手动捕获Code:1001
,done: function (res, curr, count) {
        if (res.code != 0) {
          if (res.code === 1001) {
            admin.exit();
          }
          else
          {
            layer.msg(res.msg);
          }
        }
      }
~~~

> 事实上，layuiAdmin 的所有 Ajax 请求都是采用 admin.req(options)，它会自动传递 access_token，因此推荐你在 JS 执行 Ajax 请求时直接使用它。

## 接口鉴权

我们推荐服务端遵循 JWT（JSON Web Token） 标准进行鉴权。

## 基础方法

### config 模块

你可以在任何地方通过 layui.setter 得到 config.js 中的配置信息

### admin 模块

var admin = layui.admin;
	
* admin.req(options)
	* Ajax 请求，用法同 $.ajax(options)，只是该方法会进行错误处理和 token 的自动传递
* admin.screen()
	* 获取屏幕类型，根据当前屏幕大小，返回 0 - 3 的值(小于768px~大于1200px)
* admin.exit()
	* 清除本地 token，并跳转到登入页
* admin.sideFlexible(status)
	* 侧边伸缩。status 为 null：收缩；status为 “spread”：展开
* admin.on(eventName, callback)
	* 事件监听
	* hash: 监听路由地址改变

	~~~javascript
	// 下述中的 xxx 可随意定义，不可与已经定义的 hash 事件同名，否则会覆盖上一事件
	admin.on('hash(xxx)', function(router){
	  console.log(router); //得到路由信息
	});
	~~~

	* side: 监听侧边伸缩

	~~~javascript
	// 下述中的 xxx 可随意定义，不可与已经定义的 side 事件同名，否则会覆盖上一事件
	admin.on('side(xxx)', function(obj){
	  console.log(obj.status); //得到伸缩状态：spread 为展开状态，其它值为收缩状态
	});
	~~~

* admin.popup(options)
	* 弹出一个 layuiAdmin 主题风格的 layer 层，参数 options 跟 layer.open(options) 完全相同
* admin.popupRight(options)
	* 在屏幕右侧呼出一个面板层。options 同上。
* admin.resize(callback)
	* 窗口 resize 事件处理，我们推荐你使用该方法取代 jQuery 的 resize 事件，以避免多页面标签下可能存在的冲突。
* admin.fullScreen()
	* 全屏
* admin.exitScreen()
	* 退出全屏
* admin.events.refresh()
	* 刷新当前右侧区域
* admin.events.closeThisTabs()
	* 关闭当前标签页
* admin.events.closeOtherTabs()
	* 关闭其它标签页
* admin.events.closeAllTabs()
	* 关闭全部标签页

### view 模块

var view = layui.view;

* view(id)
	* 获取指定容器，并返回一些视图渲染的方法

	~~~javascript
	//渲染视图，viewPath 即为视图路径
	view('id').render(viewPath).then(function(){
	    //视图文件请求完毕，视图内容渲染前的回调
	}).done(function(){
	   //视图文件请求完毕和内容渲染完毕的回调
	}); 

	//直接向容器插入 html，tpl 为 模板字符；data 是传入的数据。该方法会自动完成动态模板解析
	view('id').send(tpl, data); 
	~~~

	* 另外，render 方法支持动态传参，以用于视图内容接受

	~~~javascript
	admin.popup({
	  id: 'LAY-popup-test1'
	  ,success: function(){
	    view(this.id).render('视图文件所在路径', {
	       id: 123 //这里的 id 值你可以在一些事件中动态获取（如 table 模块的编辑）
	    });
	  }
	});
	~~~

	* 那么，在视图文件中，你可以在动态模板中通过 {{ d.params.xxx }} 得到传入的参数，如：

	~~~javascript
	<script type="text/html" template lay-url="http://api.com?id={{ d.params.id }}">
	  配置了接口的动态模板，且接口动态获取了 render 传入的参数：{{ d.params.id }}
	</script>

	<script type="text/html" template>
	  也可以直接获取：<input type="hidden" name="id" value="{{ d.params.id }}">
	</script>
	~~~

	* 而如果是在 JS 语句中去获取模板传递过来的变量，可以借助动态模板的 lay-done 属性去实现，如：

	~~html
	<script type="text/html" template lay-done="layui.data.sendParams(d.params)">
	  
	</script>
	~~~

	* 然后在 JS 语句中通过执行动态模板 lay-done 中对应的方法得到对应的参数值：

	~~~javascript
	<script>
	//定义一个 lay-done 对应的全局方法，以供动态模板执行
	layui.data.sendParams = function(params){
	  console.log(params.id) //得到传递过来的 id 参数（或其他参数）值
	  
	  //通过得到的参数值，做一些你想做的事
	  //…

	  //若需用到 layui 组件，layui.use 需写在该全局方法里面，如：
	  layui.use(['table'], function(){
	    var table = layui.table;
	    table.render({
	      elem: ''
	      ,url: 'url?id='+ params.id
	    });
	  });
	};
	</script>
	~~~

* 总之，驾驭好 view().render().done(callback) 对您的项目开发至关重要。

## ID唯一性

如果你开启了标签页功能，请务必注意 ID 的冲突，尤其是在你自己绑定事件的情况。ID 的命令可以遵循以下规则来规避冲突：

> LAY-路由-任意名

## Hover 提示层

通过对元素设置 lay-tips="提示内容" 来开启一个 hover 提示，如：

	<i class="layui-icon layui-icon-tips" lay-tips="要支持的噢" lay-offset="5"></i>

其中 lay-offset 用于定于水平偏移距离（单位px），以调整箭头让其对准元素

## 兼容性

layuiAdmin 使用到了 layui 的栅格系统，而栅格则是基于浏览器的媒体查询。ie8、9不支持。
所以要在宿主页面（如 start/index.html ）加上下面这段保证兼容：

~~~html
<!-- 让IE8/9支持媒体查询，从而兼容栅格 -->
<!--[if lt IE 9]>
  <script src="https://cdn.staticfile.org/html5shiv/r29/html5.min.js"></script>
  <script src="https://cdn.staticfile.org/respond.js/1.4.2/respond.min.js"></script>
<![endif]-->  
~~~

## 缓存问题

由于单页面版本的视图文件和静态资源模块都是动态加载的，所以可能存在浏览器的本地缓存问题，事实上我们也考虑到这个，因此，为了避免改动后的文件未及时生效，你只需在入口页面（默认为start/index.html）中，找到 layui.config ，修改其 version 的值即可。

~~~html
我们推荐你分场景来更新缓存：

场景一：如果项目是在本地开发。你可以设置 version 为动态毫秒数，如：
version: new Date().getTime() //这样你每次刷新页面，都会更新一次缓存
场景二：如果项目是在线上运行。建议你手工更新 version，如：
version: '1.0.0' //每次发布项目时，跟着改动下该属性值即可更新静态资源的缓存
~~~

## 源码构建

> 当你在 src 目录完成开发后，你可通过 gulp 对 src 源码进行自动化构建，以生成用于线上环境的 dist 目录。并在入口页面中的 layui.config 的 base 参数指向 dist。

在资源包中根目录下看到的 gulpfile.js 是 layuiAdmin 写好的任务脚本，package.json 是任务配置文件，你只需按照以下步骤：

step1：确保你的电脑已经安装好了 Node.js，如果未安装，可去官网下载安装

step2: 命令行安装 gulp：npm install gulp -g

step3：切换到 layuiAdmin 项目根目录（即 gulpfile.js 所在目录），命令行安装任务所依赖的包：npm install

安装完成后，后续只需直接执行命令：gulp 即可完成 src 到 dist 目录的构建