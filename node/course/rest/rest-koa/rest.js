// 这个错误处理的好处在于，不但简化了Controller的错误处理（只需要throw，其他不管），并且，在遇到非APIError的错误时，自动转换错误码为internal:unknown_error。
module.exports = {
    APIError: function (code, message) {
        this.code = code || 'internal:unknow_error';
        this.message = message || '';
    },
    restify: (pathPrefix) => {
        // REST API前缀，默认为/api/:
        pathPrefix = pathPrefix || '/api/';
        return async (ctx, next) => {
            // 是否是REST API前缀?
            if (ctx.request.path.startsWith(pathPrefix)) {
                // 绑定rest()方法:
                ctx.rest = (data) => {
                    ctx.response.type = 'application/json';
                    ctx.response.body = data;
                }
                // 受益于async/await语法，我们在middleware中可以直接用try...catch捕获异常。如果是callback模式，就无法用try...catch捕获，代码结构将混乱得多。
                try {
                    await next();
                } catch (e) {
                    // 返回错误:
                    ctx.response.status = 400;
                    ctx.response.type = "application/json";
                    ctx.response.body = {
                        code: e.code || 'internal:unknow_error',
                        message: e.message || ''
                    }
                }
            } else {
                await next();
            }
        }
    }
}

// 这样，任何支持REST的异步函数只需要简单地调用：
/* ctx.rest({
    data: 123
}); */
// 就完成了REST请求的处理。
