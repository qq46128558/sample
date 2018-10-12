# 学习记录

## 入口页面

1. 宿主页面：start/index.html，
2. 宿主页面引用layui css: <link rel="stylesheet" href="layui/css/layui.css" media="all">
3. 校验是否浏览器打开

    ~~~javascript
    /^http(s*):\/\//.test(location.href) || alert('请先部署到 localhost 下再访问');
    ~~~

4. body中有div id="LAY_app"，应改是嵌入各种页面用
5. layui的js脚本: src="layui/layui.js"
6. 模块化的用法:layui.use() 方式来加载该入口文件, base是存放新模块的目录

    ~~~javascript
    layui.config({
    base: '../dist/' //指定 layuiAdmin 项目路径，本地开发用 src，线上用 dist
        ,version: '1.0.0' //每次发布项目时，跟着改动下该属性值即可更新静态资源的缓存（参考开发者文档的缓存问题）
    }).use('index');
    ~~~

## layuiadmin pro模块的加载

1. 主入口：src/index.js 或 dist/index.js