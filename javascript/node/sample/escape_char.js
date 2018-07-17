// 转义字符
'use strict'

// 换行符
console.info('first line\nsecond line');
// first line
// second line

// 退格符
console.info('first line\bsecond line');
// first linsecond line

// 换页符\f 垂直制表符\v
console.info('first line\fsecond line');
// first line
//           second line

// 水平制表符
console.info('first line\tsecond line');
// first line      second line

// 回车符\r
console.info('first line\rsecond line');
// second line

// Nul字符
console.info('first line\0second line');
// first linesecond line
console.info('\0'=='\u0000');
// true