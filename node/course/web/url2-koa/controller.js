// 我们把扫描controllers目录和创建router的代码从app.js中提取出来，作为一个简单的middleware使用，命名为controller.js
// 先导入fs模块，然后用readdirSync列出文件
const fs=require('fs');

function addControllers(router,dir){
    // 自动扫描controllers目录，找到所有js文件，导入，然后注册每个URL：
    // 这里可以用sync是因为启动时只运行一次，不存在性能问题:
    var files=fs.readdirSync(__dirname+`/${dir}`);
    // 过滤出.js文件:
    var js_files=files.filter((f)=>{
        return f.endsWith('.js');
    })
    // 这里用of
    for (var f of js_files){
        console.log(`Process controller: ${f}...`);
        let mapping=require(__dirname+'/'+dir+'/'+f);
        addMapping(router,mapping);
    }

}

function addMapping(router,mapping){
    // 这里用in
    for (var url in mapping){
        if (url.startsWith('GET ')){
            var path=url.substring(4);
            router.get(path,mapping[url]);
            console.log(`Register URL mapping: GET ${path}`);
        }else if (url.startsWith('POST')){
            var path=url.substring(5);
            router.post(path,mapping[url]);
            console.log(`Register URL mapping: POST ${path}`);
        }else{
            console.log(`Invalid URL: ${url}`);
        }
    }
}

module.exports=function(dir){
    let
        // 如果不传参数，扫描目录默认为'controllers'
        controllers_dir=dir||'controllers',router=require('koa-router')();
        addControllers(router,controllers_dir);
        return router.routes();

}

