'use strict'

// 'javascript正则用法'

var c=function(msg){
	console.info(msg);
}

var text="testing: 1, 2, 3";
// 匹配所有包含一个或多个数字的实例
var pattern=/\d+/g;

c(pattern.test(text));
// true 匹配成功

c(text.search(pattern));
// 9 首次匹配成功位置

c(text.match(pattern));
// [ '1', '2', '3' ] 所有匹配组成的数组

c(text.replace(pattern,'#'));
// testing: #, #, #

c(text.split(/\D+/));
// [ '', '1', '2', '3' ] 用非数字字符截取字符串

