
// 一个模块想要对外暴露变量（函数也是变量），可以用module.exports = variable;

// 变量module是Node在加载js文件前准备的一个变量，并将其传入加载函数，我们在hello.js中可以直接使用变量module原因就在于它实际上是函数的一个参数
// 通过把参数module传递给load()函数，hello.js就顺利地把一个变量传递给了Node执行环境，Node会把module变量保存到某个地方。
// 由于Node保存了所有导入的module，当我们用require()获取module时，Node找到对应的module，把这个module的exports变量返回，这样，另一个模块就顺利拿到了模块的输出

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

