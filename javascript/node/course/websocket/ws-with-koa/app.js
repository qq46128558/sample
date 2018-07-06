// 基于WebSocket创建一个在线聊天室。

const url = require('url');
const ws = require('ws');
const Cookies = require('cookies');
const Koa = require('koa');
const bodyParser = require('koa-bodyparser');
const controller = require('./controller');
const templating = require('./templating');
const WebSocketServer = ws.Server;
// 首先得到了一个标准的基于MVC的koa2应用。该应用的核心是一个代表koa应用的app变量
const app = new Koa();

// log request URL:
app.use(async (ctx, next) => {
    console.log(`Process ${ctx.request.method} ${ctx.request.url}...`);
    await next();
});

// 在koa的middleware中，我们很容易识别用户：
// parse user from cookie:
app.use(async (ctx, next) => {
    ctx.state.user = parseUser(ctx.cookies.get('name') || '');
    await next();
});

// static file support:
let staticFiles = require('./static-files');
app.use(staticFiles('/static/', __dirname + '/static'));

// parse request body:
app.use(bodyParser());

// add nunjucks as view:
app.use(templating('views', {
    noCache: true,
    watch: true
}));

// add controller middleware:
app.use(controller());

// 实际应用中，HTTP和WebSocket都使用标准的80和443端口，不需要暴露新的端口，也不需要修改防火墙规则。
// 实际上，3000端口并非由koa监听，而是koa调用Node标准的http模块创建的http.Server监听的。koa只是把响应函数注册到该http.Server中了。类似的，WebSocketServer也可以把自己的响应函数注册到http.Server中，这样，同一个端口，根据协议，可以分别由koa和ws处理：

// koa app的listen()方法返回http.Server:
let server = app.listen(3000);

/* 在koa应用中，可以很容易地认证用户，例如，通过session或者cookie，但是，在响应WebSocket请求时，如何识别用户身份？
一个简单可行的方案是把用户登录后的身份写入Cookie，在koa中，可以使用middleware解析Cookie，把用户绑定到ctx.state.user上。
WS请求也是标准的HTTP请求，所以，服务器也会把Cookie发送过来，这样，我们在用WebSocketServer处理WS请求时，就可以根据Cookie识别用户身份。
先把识别用户身份的逻辑提取为一个单独的函数： */
function parseUser(obj) {
    if (!obj) { return; }
    console.log(`Try parse: ${obj}`);
    let s = '';
    if (typeof obj === 'string') {
        s = obj;
    } else if (obj.headers) {
        let cookies = new Cookies(obj, null);
        s = cookies.get('name');
    }
    if (s) {
        try {
            let user = JSON.parse(Buffer.from(s, 'base64').toString());
            console.log(`User: ${user.name}, ID:${user.id}`);
            return user;
        } catch (e) {
            // ignore
        }
    }
}
// 注意：出于演示目的，该Cookie并没有作Hash处理，实际上它就是一个JSON字符串。

function createWebSocketServer(server, onConnection, onMessage, onClose, onError) {
    // 创建WebSocketServer:
    // WebSocketServer会首先判断请求是不是WS请求，如果是，它将处理该请求，如果不是，该请求仍由koa处理。
    // 所以，WS请求会直接由WebSocketServer处理，它根本不会经过koa，koa的任何middleware都没有机会处理该请求。
    let wss = new WebSocketServer({
        server: server
    });
    // 对于聊天应用来说，每收到一条消息，就需要把该消息广播到所有WebSocket连接上。
    wss.broadcast = function broadcast(data) {
        wss.clients.forEach(function each(client) {
            client.send(data);
        });
    }
    onConnection = onConnection || function () {
        console.log('[WebSocket] connected.');
    };
    onMessage = onMessage || function (msg) {
        console.log('[WebSocket] message received: ' + msg);
    }
    onClose = onClose || function (code, message) {
        console.log(`[WebSocket] closed: ${code} - ${message}`);
    }
    onError = onError || function (err) {
        console.log('[WebSocket] error' + err);
    }
    // 在WebSocketServer中，就需要响应connection事件，然后识别用户：
    wss.on('connection', function (ws) {
        let location = url.parse(ws.upgradeReq.url, true);
        console.log('[WebSocketServer] connection: ' + location.href);
        // 我们要对每个创建成功的WebSocket绑定message、close、error等事件处理函数。
        ws.on('message', onMessage);
        ws.on('close', onClose);
        ws.on('error', onError);
        if (location.pathname !== '/ws/chat') {
            // close ws
            ws.close(4000, 'Invalid URL');
        }
        // ws.upgradeReq是一个request对象:
        // check user
        let user = parseUser(ws.upgradeReq);
        if (!user) {
            // Cookie不存在或无效，直接关闭WebSocket:
            ws.close(4001, 'Invalid user');
        }
        // 识别成功，把user绑定到该WebSocket对象
        ws.user = user;
        // 绑定WebSocketServer对象:
        ws.wss = wss;
        onConnection.apply(ws);
    })
}
var messageIndex = 0;

// 消息有很多类型，不一定是聊天的消息，还可以有获取用户列表、用户加入、用户退出等多种消息。所以我们用createMessage()创建一个JSON格式的字符串，发送给浏览器，浏览器端的JavaScript就可以直接使用：
function createMessage(type, user, data) {
    messageIndex++;
    return JSON.stringify({
        id: messageIndex,
        type: type,
        user: user,
        data: data
    });
}

function onConnect() {
    let user = this.user;
    let msg = createMessage('join', user, `${user.name} joined.`);
    this.wss.broadcast(msg);
    // build user list
    let users = this.wss.clients.map(function (client) {
        return client.user;
    });
    this.send(createMessage('list', user, users));
}

function onMessage(message) {
    console.log(message);
    // 在某个WebSocket收到消息后，就可以调用wss.broadcast()进行广播了：
    if (message && message.trim()) {
        let msg = createMessage('chat', this.user, message.trim());
        this.wss.broadcast(msg);
    }
}

function onClose() {
    let user = this.user;
    let msg = createMessage('left', user, `${user.name} is left.`);
    this.wss.broadcast(msg);
}

app.wss = createWebSocketServer(server, onConnect, onMessage, onClose);

console.log('app started at port 3000...');
// 测试的时候，如果在本机测试，需要同时用几个不同的浏览器，这样Cookie互不干扰。