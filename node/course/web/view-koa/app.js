

/* 这里我们定义了一个常量isProduction，它判断当前环境是否是production环境。如果是，就使用缓存，如果不是，就关闭缓存。在开发环境下，关闭缓存后，我们修改View，可以直接刷新浏览器看到效果，否则，每次修改都必须重启Node程序，会极大地降低开发效率。
Node.js在全局变量process中定义了一个环境变量env.NODE_ENV，为什么要使用该环境变量？因为我们在开发的时候，环境变量应该设置为'development'，而部署到服务器时，环境变量应该设置为'production'。在编写代码的时候，要根据当前环境作不同的判断。
注意：生产环境上必须配置环境变量NODE_ENV = 'production'，而开发环境不需要配置，实际上NODE_ENV可能是undefined，所以判断的时候，不要用NODE_ENV === 'development'。 */
const isProduction=process.env.NODE_ENV==='production';
const Koa=require('koa');
const app=new Koa();
const bodyParser=require('koa-bodyparser');

// 第一个middleware是记录URL以及页面执行时间：
app.use(async(ctx,next)=>{
    console.log('Process ${ctx.request.method} ${ctx.request.url}...');
    var
        start=new Date().getTime();
        execTime;
    await next();
    execTime=new Date().getTime()-start;
    ctx.response.set('X-Response-Time',`${execTime}ms`);
})

// 第二个middleware处理静态文件：
// 这是因为在生产环境下，静态文件是由部署在最前面的反向代理服务器（如Nginx）处理的，Node程序不需要处理静态文件。而在开发环境下，我们希望koa能顺带处理静态文件，否则，就必须手动配置一个反向代理服务器，这样会导致开发环境非常复杂。
if (!isProduction){
    // 注意：也可以去npm搜索能用于koa2的处理静态文件的包并直接使用。
    let staticFiles=require('./statics-files');
    app.use(staticFiles('/static',__dirname+'/static'));
}

// 第三个middleware解析POST请求：
app.use(bodyParser());

// 第四个middleware负责给ctx加上render()来使用Nunjucks：
let templating=require('./templating');
app.use(templating('views',{
    noCache:!isProduction,
    watch:!isProduction,
}))

// 最后一个middleware处理URL路由：


app.listen(3000);
console.log("app started at port 3000...");