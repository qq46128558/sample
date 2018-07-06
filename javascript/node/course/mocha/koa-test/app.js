// 这个koa应用和前面的koa应用稍有不同的是，app.js只负责创建app实例，并不监听端口
const Koa=require('koa');
const app=new Koa();
app.use(async(ctx,next)=>{
    const start=new Date().getTime();
    await next();
    const ms=new Date().getTime()-start;
    console.log(`${ctx.request.method} ${ctx.request.url}: ${ms}ms`);
    ctx.response.set('X-Response-Time',`${ms}ms`);
});
app.use(async(ctx,next)=>{
    var name=ctx.request.query.name||'Peter';
    ctx.response.type="text/html";
    ctx.response.body=`<h1>Welcome back ${name}.</h1>`;
});
module.exports=app;
