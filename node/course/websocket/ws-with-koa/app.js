const url = require('url');
const ws = require('ws');
const Cookies = require('cookies');
const Koa = require('koa');
const bodyParser = require('koa-bodyparser');
const controller = require('./controller');
const templating = require('./templating');
const WebSocketServer = ws.Server;
const app = new Koa();

// log request URL:
app.use(async (ctx, next) => {
    console.log(`Process ${ctx.request.method} ${ctx.request.url}...`);
    await next();
});

// parse user from cookie:
app.use(async(ctx,next)=>{
    ctx.state.user=parseUser(ctx.cookies.get('name')||'');
    await next();
});

// static file support:
let staticFiles=require('./static-files');
app.use(staticFiles('/static/',__dirname+'/static'));

// parse request body:
app.use(bodyParser());

// add nunjucks as view:
app.use(templating('views',{
    noCache:true,
    watch:true
}));

// add controller middleware:
app.use(controller());

let server=app.listen(3000);

function parseUser(obj){
    if (!obj){return;}
    console.log(`Try parse: ${obj}`);
    let s='';
    if (typeof obj==='string'){
        s=obj;
    }else if (obj.headers){
        let cookies=new Cookies(obj,null);
        s=cookies.get('name');
    }
    
}

