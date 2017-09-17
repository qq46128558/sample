const Koa = require("koa");
const app = new Koa();
const staticFiles = require('./static-files');

const bodyParser = require('koa-bodyparser');
const controller = require('./controller');
const rest = require('./rest');
const isProduction = process.env.NODE_ENV === 'production';


app.use(async (ctx, next) => {
    console.log(`Process ${ctx.request.method} ${ctx.request.url}...`);
    var
        start = new Date().getTime(),
        execTime;
    await next();
    execTime = new Date().getTime() - start;
    ctx.response.set('X-Response-Time', `${execTime}ms`);
})
app.use(staticFiles('/static', __dirname + '/static/'));

// parse request body:
app.use(bodyParser());

// bind .rest() for ctx:
app.use(rest.restify());

// add controllers:
app.use(controller());

app.listen(3000);
console.log('app started at port 3000...');
