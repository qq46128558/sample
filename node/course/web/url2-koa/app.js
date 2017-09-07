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
app.use(bodyParser());
// add router middleware:
app.use(router.routes());
app.listen(3000);
console.log('app started at port 3000...');
