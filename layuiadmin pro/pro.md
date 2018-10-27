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