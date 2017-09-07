'use strict';
// 我们可以设定一个目录，然后让Web程序变成一个文件服务器。要实现这一点，我们只需要解析request.url中的路径，然后在本地找到对应的文件，把文件内容发送出去就可以了。

var 
fs=require('fs'),
url=require('url'),
path=require('path'),
http=require('http');

// 从命令行参数获取root目录，默认是当前目录:
var root=path.resolve(process.argv[2]||'.');
console.log('Static root dir:'+root);
// 创建服务器:
var server=http.createServer(function(request,response){
    // 获得URL的path，类似 '/css/bootstrap.css':
    var pathname=url.parse(request.url).pathname;
    // 获得对应的本地文件路径，类似 '/srv/www/css/bootstrap.css':
    var filepath=path.join(root,pathname);
    // 获取文件状态:
    fs.stat(filepath,checkstat);

   /*  练习
    在浏览器输入http://localhost:8080/时，会返回404，原因是程序识别出HTTP请求的不是文件，而是目录。请修改file_server.js，如果遇到请求的路径是目录，则自动在目录下依次搜索index.html、default.html，如果找到了，就返回HTML文件的内容。 */
    function checkstat(err,stats){
        if (!err && stats.isFile()){
            show200();
        }else if (!err && stats.isDirectory()){
           filepath=path.join(filepath,'unicode.html');
           fs.stat(filepath,checkstat);
        }else{
            show404();
        }
    }
    var show200=function(){
        // 没有出错并且文件存在:
        console.log('200'+request.url);
        // 发送200响应:
        response.writeHead(200);
        // 将文件流导向response: 没有必要手动读取文件内容。由于response对象本身是一个Writable Stream，直接用pipe()方法就实现了自动读取文件内容并输出到HTTP响应。
        fs.createReadStream(filepath).pipe(response);
    }
    var show404=function(){
        // 出错了或者文件不存在
        console.log('404'+request.url);
        // 发送404响应:
        response.writeHead(404);
        response.end('404 Not Found.');
    }
})



server.listen(8080);
console.log('Server is running at http://127.0.0.1:8080/');

// 在命令行运行node file_server.js /path/to/dir，把/path/to/dir改成你本地的一个有效的目录，然后在浏览器中输入http://localhost:8080/index.html：