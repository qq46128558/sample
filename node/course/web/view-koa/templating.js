// 集成Nunjucks实际上也是编写一个middleware，这个middleware的作用是给ctx对象绑定一个render(view, model)的方法，这样，后面的Controller就可以调用这个方法来渲染模板了。
const nunjucks=require('nunjucks');
function createEnv(path,opts){
    var
        autoescape=opts.autoescape===undefined?true:opts.autoescape,
        noCache=opts.noCache||false,
        watch=opts.watch||false,
        throwOnUndefined=opts.throwOnUndefined||false,
        env=new nunjucks.Environment(
            new nunjucks.FileSystemLoader(path||'views',{
                noCache:noCache,
                watch:watch,
            }),{
                autoescape:autoescape,
                throwOnUndefined:throwOnUndefined,
            }
        )
    if (opts.filters){
        for (var f in opts.filters){
            env.addFilter(f,opts.filters[f]);
        }
    }
    return env;
}

function templating(path,opts){
    // 创建Nunjucks的env对象:
    var env=createEnv(path,opts);
    return async(ctx,next)=>{
        console.log('entry templating...');
        // 给ctx绑定render函数:
        ctx.render=function (view, model){
            // 注意到ctx.render内部渲染模板时，Model对象并不是传入的model变量
            // 这个小技巧是为了扩展。
            // 首先，model || {}确保了即使传入undefined，model也会变为默认值{}。Object.assign()会把除第一个参数外的其他参数的所有属性复制到第一个参数中。第二个参数是ctx.state || {}，这个目的是为了能把一些公共的变量放入ctx.state并传给View。
            // 把render后的内容赋值给response.body:
            ctx.response.body=env.render(view,Object.assign({},ctx.state||{},model||{}));
            // 设置Content-Type:
            ctx.response.type="text/html";
        }
        console.log('templating await next...');
        // 继续处理请求
        await next();
    }
}

module.exports=templating;
// 注意到createEnv()函数和前面使用Nunjucks时编写的函数是一模一样的。我们主要关心tempating()函数，它会返回一个middleware，在这个middleware中，我们只给ctx“安装”了一个render()函数，其他什么事情也没干，就继续调用下一个middleware。


/* 例如，某个middleware负责检查用户权限，它可以把当前用户放入ctx.state中：
app.use(async (ctx, next) => {
    var user = tryGetUserFromCookie(ctx.request);
    if (user) {
        ctx.state.user = user;
        await next();
    } else {
        ctx.response.status = 403;
    }
});
这样就没有必要在每个Controller的async函数中都把user变量放入model中。 */