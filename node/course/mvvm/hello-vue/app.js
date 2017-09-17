const Koa=require("koa");
const app=new Koa();
const staticFiles=require('./static-files');

app.use(async(ctx,next)=>{
    console.log(`Process ${ctx.request.method} ${ctx.request.url}...`);
    await next();
})
app.use(staticFiles('/static',__dirname+'/static/'));

app.listen(3000);
console.log('app started at port 3000...');
