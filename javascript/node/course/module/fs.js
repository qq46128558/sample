'use strict';

// 同步读文件, 原异步调用的回调函数的data被函数直接返回，函数名需要改为readFileSync，其它参数不变。
// 如果同步读取文件发生错误，则需要用try...catch捕获该错误：

// 异步读文件
var fs=require('fs');
fs.readFile('hello.js','utf-8',function(err,data){
    if (err){
        console.log(err);
    }else{
        console.log('01.');
        console.log(data);
        // string->buffer
        console.log('02.');
        console.log(Buffer.from(data,'utf-8'))
    }
})

// 读取二进制文件
fs.readFile('d:/projects/www/sample/1353022505371.jpg',function(err,data){
    if (err){
        console.log(err);
    }else{
        console.log('03.');
        console.log(data);
        console.log(data.length+' Bytes');
        // buffer->string
        console.log('04.太大会卡一段时间,略.');
        // console.log(data.toString('utf-8'));
    }
})

// 写文件writeFile,追加用appendFile
var now=new Date();
/* fs.writeFile('output.txt','写资料入文件:'+now.getTime(),function(err){
    if (err){
        console.log(err);
    }else{
        console.log('05.write file done.');
    }
})
 */
fs.appendFile('output.txt','写资料入文件:'+now.getTime()+"\n",function(err){
    if (err){
        console.log(err);
    }else{
        console.log('05.write file done.');
    }
})
// 获取文件或目录的详细信息
// 如果我们要获取文件大小，创建时间等信息，可以使用fs.stat()，它返回一个Stat对象，能告诉我们文件或目录的详细信息：
fs.stat('hello.js',function(err,stats){
    if (err){
        console.log(err);
    }else{
        console.log('06.大小'+stats.size+ " Bytes");
        console.log('07.是否文件'+stats.isFile());
        console.log('08.是否目录'+stats.isDirectory());
        console.log('09.创建时间'+stats.birthtime);
        console.log('10.修改时间'+stats.mtime);
    }
})