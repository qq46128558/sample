# 最基础的小程序开发入门

## [微信开发者工具](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html "https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html")

搭建开发环境

## 如何创建第一个小程序

可以先不用注册小程序ID

使用微信开发者工具创建小程序项目

点击确定，第一个小程序"Hello World"已经可以运行了

## 项目结构

一个页面构成主要有三大部分构成 index.wxml 、index.wxss 、index.js

如同一个网页主要 HTML + CSS + JS 这样的组合

项目的根目录还有一个 app.json 和 project.config.json 

app.json 是对当前小程序的全局配置，包括了小程序的所有页面路径、界面表现、网络超时时间、底部 tab 等。

project.config.json 可以针对各自喜好做一些个性化配置，例如界面颜色、编译配置等 。

[官方文档](https://mp.weixin.qq.com/debug/wxadoc/dev/framework/config.html "https://mp.weixin.qq.com/debug/wxadoc/dev/framework/config.html")

## 如何创建个新页面

小程序的页面创建，只需要在 app.json 文件下找到一个 pages 的属性值 

pages 属性：接受一个数组，每一项都是字符串，来指定小程序由哪些页面组成。

每一项代表对应页面的【路径+文件名】信息，数组的第一项代表小程序的初始页面。小程序中新增/减少页面，都需要对 pages 数组进行修改。

## 页面如何加载数据

首先你要先学习一下小程序开发组件 。一个组件通常包括开始标签和结束标签，属性用来修饰这个组件，内容在两个标签之内 。

[官方文档](https://mp.weixin.qq.com/debug/wxadoc/dev/component/ "https://mp.weixin.qq.com/debug/wxadoc/dev/component/")

[小程序提供的原生API](https://mp.weixin.qq.com/debug/wxadoc/dev/api/ "https://mp.weixin.qq.com/debug/wxadoc/dev/api/")