'use strict'

// 浮点数二进制表示法的问题

var x=0.3-0.2;
var y=0.2-0.1;

console.info(x);
// 0.09999999999999998
console.info(y);
// 0.1
console.info(x==y);
// false

// 所以银行一般用整数分进行运算