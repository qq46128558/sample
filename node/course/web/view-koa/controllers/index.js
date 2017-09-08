// 处理首页 GET /
// 我们定义一个async函数处理首页URL/：
async(ctx,next)=>{
    ctx.render('index.html',{
        title:"Welcome"
    })
}
// 注意到koa并没有在ctx对象上提供render方法，这里我们假设应该这么使用，这样，我们在编写Controller的时候，最后一步调用ctx.render(view, model)就完成了页面输出。
