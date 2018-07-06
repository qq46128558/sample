'use strict';
var fs=require('fs');
// 打开一个流
var rs=fs.createReadStream('./hello.js','utf-8');
var i=1;
rs.on('data',function(chunk){
    console.log('DATA'+i++);
    console.log(chunk);
})
rs.on('error',function(err){
    console.log('ERROR:');
    console.log(err);
})
rs.on('end',function(){
    console.log("END.");
})

// write是异步操作
var ws1=fs.createWriteStream('output.txt','utf-8');
ws1.write('使用Stream写入文本数据...\n');
ws1.write('写入结束.');
ws1.end();
// 连续写会出现同时写的混乱情况
setTimeout(function()
{
var ws2=fs.createWriteStream('output.txt');
ws2.write(new Buffer('使用Stream写入二进制数据...\n'),'utf-8');
ws2.write(new Buffer('写入结束.'),'utf-8');
ws2.end();
},1000);

// pipe
// 就像可以把两个水管串成一个更长的水管一样，两个流也可以串起来。一个Readable流和一个Writable流串起来后，所有的数据自动从Readable流进入Writable流，这种操作叫pipe。
// ws关闭后(end)则不能写入,也存在异步写入问题
// 默认情况下，当Readable流的数据读取完毕，end事件触发后，将自动关闭Writable流。如果我们不希望自动关闭Writable流，需要传入参数：
// readable.pipe(writable, { end: false });
setTimeout(function(){
    var rs=fs.createReadStream('hello.js','utf-8');
    var ws=fs.createWriteStream('output.txt','utf-8');
    rs.pipe(ws);
},500);