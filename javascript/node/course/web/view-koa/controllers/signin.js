// 处理登录请求 POST /signin
// 我们再定义一个async函数处理登录请求/signin
module.exports={
    "POST /signin":async(ctx,next)=>{
        var
            email=ctx.request.body.email||'',
            password=ctx.request.body.password||'';
        if (email==='dgw@yn-ce.com' && password==='123456'){
            // 登录成功
            ctx.render('signin-ok.html',{
                title:"Sign in ok.",
                name:"Mr Node."
            })
        }else{
            // 登录失败
            ctx.render('signin-failed.html',{
                title:"Sign in failed."
            })
        }
    }
}
// 由于登录请求是一个POST，我们就用ctx.request.body.<name>拿到POST请求的数据，并给一个默认值。
