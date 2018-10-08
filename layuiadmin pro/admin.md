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