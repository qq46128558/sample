// 入WebSocket模块:
const WebSocket=require('ws');
// 引用Server类:
const WebSocketServer=WebSocket.Server;
// 实例化:
const wss=new WebSocketServer({
    port:3000
})

// 这样，我们就在3000端口上打开了一个WebSocket Server，该实例由变量wss引用。
// 接下来，如果有WebSocket请求接入，wss对象可以响应connection事件来处理这个WebSocket：