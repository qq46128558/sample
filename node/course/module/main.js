// 在Node环境中，一个.js文件就称之为一个模块（module）
// node把一段JavaScript代码用一个函数包装起来，这段代码的所有“全局”变量就变成了函数内部的局部变量, 模块中定义的“全局”变量互不干扰
// 一个模块要引用其他模块暴露的变量，用var ref = require('module_name');就拿到了引用模块的变量
// 如果只写模块名：
// var greet = require('hello');
// 则Node会依次在内置模块、全局模块和当前模块下查找hello.js，你很可能会得到一个错误

'use strict';
var greet=require('./hello');
var s='Michael';

// 01原始示例
// greet(s);
// 02无返回
// greet(); //报错
// 03有返回
// greet();
// 04属性
greet.name('Peter');
// 04.1属性2
// greet.name('Peter');
// 05覆盖
// greet.name(); //报错
// console.log(greet);
// 06模块是一个类
// var r=new greet('Ozzy',62);
// r.about();
// 07模块是一个数组
// console.log('Rockin in heaven: '+greet[2]);



