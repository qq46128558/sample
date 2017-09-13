// 在package.json中添加devDependencies，除了mocha外，我们还需要一个简单而强大的测试模块supertest：

const 
    request=require('supertest'),
    app=require('../app');

describe('#test koa pp',()=>{
    // 在测试中，我们首先导入supertest模块，然后导入app模块，注意我们已经在app.js中移除了app.listen(3000);语句，所以，这里我们用：
    let server=app.listen(9900);
    describe('#test server',()=>{
        it ('#test GET /',async()=>{
            // 可以构造一个GET请求，发送给koa的应用，然后获得响应
            let res=await request(server)
                .get('/')
                // 可以手动检查响应对象，例如，res.body，还可以利用supertest提供的expect()更方便地断言响应的HTTP代码、返回内容和HTTP头。断言HTTP头时可用使用正则表达式。
                .expect('Content-Type',/text\/html/)
                .expect(200,'<h1>Welcome back Peter.</h1>');
        });

        it ('#test GET /path?name=Bob',async()=>{
            let res=await request(server)
                .get('/path?name=Bob')
                .expect('Content-Type',/text\/html/)
                .expect(200,'<h1>Welcome back Bob.</h1>')
        })
    })
})
// 当所有测试运行结束后，app实例会自动关闭，无需清理。