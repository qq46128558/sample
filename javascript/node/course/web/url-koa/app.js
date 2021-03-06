// 导入koa，和koa 1.x不同，在koa2中，我们导入的是一个class，因此用大写的Koa表示:
const Koa=require('koa');
// 注意require('koa-router')返回的是函数:
const router=require('koa-router')();
// 处理post的body
const bodyParser=require('koa-bodyparser');

// 创建一个Koa对象表示web app本身:
const app=new Koa();

// log request URL:
app.use(async(ctx,next)=>{
    console.log(`Process ${ctx.request.method} ${ctx.request.url}...`);
    await next();
})

// add url-route:
router.get('/hello/:name',async(ctx,next)=>{
    var name=ctx.params.name;
    ctx.response.body=`<h1>Welcome back,${name}!</h1>`;
})

// 写一个简单的登录表单
router.get('/',async(ctx,next)=>{
    ctx.response.body=`<h1>Index</h1>
        <form action="/signin" method="post">
        <p>Name:<input name="name" value="koa"></p>
        <p>Password:<input name="password" type="password"></p>
        <p><input type="submit" value="Submit"></p>
        </form>
        `;
})

// 处理post请求
router.post('/signin',async(ctx,next)=>{
    // 注意到我们用var name = ctx.request.body.name || ''拿到表单的name字段，如果该字段不存在，默认值设置为''。
    var name=ctx.request.body.name||'', password=ctx.request.body.password||'';
    console.log(`Signin with name:${name}, password:${password}`);
    if (name==='koa' && password==='123456'){
        ctx.response.body=`<h1>Welcome back.</h1>`;
    }else{
        ctx.response.body=`<h1>Login failed.</h1>
        <p><a href="/">Try again.</a></p>`;
    }
    // await next();
})


// 由于middleware的顺序很重要，这个koa-bodyparser必须在router之前被注册到app对象上。
// 此外，如果一个middleware没有调用await next()，会怎么办？答案是后续的middleware将不再执行了。这种情况也很常见，例如，一个检测用户权限的middleware可以决定是否继续处理请求，还是直接返回403错误：
// 用post请求处理URL时，我们会遇到一个问题：post请求通常会发送一个表单，或者JSON，它作为request的body发送，但无论是Node.js提供的原始request对象，还是koa提供的request对象，都不提供解析request的body的功能！
// 所以，我们又需要引入另一个middleware来解析原始request请求，然后，把解析后的参数，绑定到ctx.request.body中。
// koa-bodyparser就是用来干这个活的。
app.use(bodyParser());
// add router middleware:
app.use(router.routes());
app.listen(3000);
console.log('app started at port 3000...');
// 最后注意ctx对象有一些简写的方法，例如ctx.url相当于ctx.request.url，ctx.type相当于ctx.response.type。