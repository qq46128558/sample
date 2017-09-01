'use strict';
var s="Hello";
function greet(name){
    console.log(s+", "+name+"!");
}

// 01原始示例
// module.exports=greet;
// 02无返回
// exports=function(){
//     console.log('exports value.');
// }
// 03有返回
// module.exports=function(){
//     console.log('module.exports value.');
// }
// 04属性
exports.name=function(name){
    console.log("My name is "+ name);
}
// 04.1属性2
// module.exports.name=function(name){
//     console.log("My name is "+name);
// }
// 05覆盖
// module.exports='ROCK IT!';
// exports.name=function(){
//     console.log('My name is Lemmy Kilmister.');
// }
// 06模块是一个类
// module.exports=function(name,age){
//     this.name=name;
//     this.age=age;
//     this.about=function(){console.log(this.name+ ' is '+this.age+' years old.');};
// }
// 07模块是一个数组
// module.exports=['Lemmy Kilmister', 'Ozzy Osbourne', 'Ronnie James Dio', 'Steven Tyler', 'Mick Jagger'];

// module.exports是真正的接口，exports只不过是它的辅助工具。推荐使用exports导出，除非你打算从原来的“实例化对象”改变成一个类型。

