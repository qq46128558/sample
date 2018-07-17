// 字符串的使用
'use strict';

var c=function(msg){
	console.info(msg);
}

var s='hello, world';
c(s.charAt(0));
// h
c(s.substring(1,4));
c(s.slice(1,4));
// ell
c(s.slice(-3));
// rld
c(s.indexOf("l"));
// 2
c(s.lastIndexOf("l"));
// 10
c(s.indexOf("l",3));
// 3
c(s.split(", "));
// [ 'hello', 'world' ]
c(s.replace("h","H"));
// Hello, world
c(s.toUpperCase());
// HELLO, WORLD