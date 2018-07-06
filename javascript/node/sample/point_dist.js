'use strict';
// 计算两点之间的距离



// 定义一个构造函数以初始化一个新的point对象
function Point(x,y){
    this.x=x;
    this.y=y;
}

var p=new Point(1,1);

// 通过给构造函数的prototype对象赋值来给point对象定义方法
Point.prototype.r=function(){
    return Math.sqrt(this.x*this.x+this.y+this.y);
};

console.info(p.r());



var points=[new Point(5,5),new Point(10,10)];
// 定义一个方法计算两点之间的距离
points.dist=function(){
    // this关键字是对定义方法的对象的引用
    var p1=this[0];
    var p2=this[1];
    var a=p2.x-p1.x,b=p2.y-p1.y;
    return Math.sqrt(a*a+b*b); // 勾股定理
}

console.log(points.dist());