// 要得知某些代码的执行时间，特别是调试缓慢循环时，非常有用。 甚至可以通过给方法传入不同参数，来设置多个定时器。来看看它是怎么运行的：
console.time("timer1");
var items=[];
for (var i=0;i<10000;i++){
    items.push({index:i});
}
console.timeEnd("timer1");
