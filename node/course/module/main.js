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



