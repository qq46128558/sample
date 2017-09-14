const Koa=require('koa');
const app=new Koa();
const controller=require('./controller');
const bodyParser=require('koa-bodyparser');

// 注意到app.use(bodyParser());这个语句，它给koa安装了一个解析HTTP请求body的处理函数。如果HTTP请求是JSON数据，我们就可以通过ctx.request.body直接访问解析后的JavaScript对象。
app.use(bodyParser());
app.use(controller());
app.listen(3000);
console.log('app started at port 3000...');

// 在koa中处理REST请求是非常简单的。bodyParser()这个middleware可以解析请求的JSON数据并绑定到ctx.request.body上，输出JSON时我们先指定ctx.response.type = 'application/json'，然后把JavaScript对象赋值给ctx.response.body就完成了REST请求的处理。

// 使用REST和使用MVC是类似的，不同的是，提供REST的Controller处理函数最后不调用render()去渲染模板，而是把结果直接用JSON序列化返回给客户端。
