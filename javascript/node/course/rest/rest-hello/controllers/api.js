// 存储Product列表，相当于模拟数据库:
var products=[{
    name:'iPhone',
    price:6999
},{
    name:'Kindle',
    price:999
}];

module.exports={
    'GET /api/products':async(ctx,next)=>{
        // 设置Content-Type:
        ctx.response.type='application/json';
        // 设置Response Body:
        // 在koa中，我们只需要给ctx.response.body赋值一个JavaScript对象，koa会自动把该对象序列化为JSON并输出到客户端。
        ctx.response.body={
            products:products
        }
    },
    // 这个POST请求无法在浏览器中直接测试。但是我们可以通过curl命令在命令提示符窗口测试这个API。我们输入如下命令
    // curl -H 'Content-Type: application/json' -X POST -d '{"name":"XBox","price":3999}' http://localhost:3000/api/products
    'POST /api/products':async(ctx,next)=>{
        var p={
            name:ctx.request.body.name,
            price:ctx.request.body.price
        }
        products.push(p);
        ctx.response.type="application/json";
        ctx.response.body=p;

    }
}