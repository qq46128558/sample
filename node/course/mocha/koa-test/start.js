// start.js负责真正启动应用：
// 这样做的目的是便于后面的测试。
const app=require('./app');
app.listen(3000);
console.log("app started at port 3000...")