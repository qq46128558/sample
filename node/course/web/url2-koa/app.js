// 导入controller middleware:
const controller=require('./controller');

// 使用middleware:
const Koa=require('koa');
const app=new Koa();

const bodyParser=require('koa-bodyparser');
app.use(async(ctx,next)=>{
    console.log(`Process ${ctx.request.method} ${ctx.request.url}...`);
    await next();
})

// parse request body:
app.use(bodyParser());

// add controllers:
app.use(controller());

app.listen(3000);
console.log("app started at port 3000...");


// 经过重新整理后的工程url2-koa目前具备非常好的模块化，所有处理URL的函数按功能组存放在controllers目录，今后我们也只需要不断往这个目录下加东西就可以了，app.js保持不变。