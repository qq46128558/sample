var car;
var func1 = function() {
  func2();
}

var func2 = function() {
  func4();
}
var func3 = function() {
}

var func4 = function() {
  car = new Car();
  car.funcX();
}
var Car = function() {
  this.brand = 'volvo';
  this.color = 'red';
  this.funcX = function() {
    this.funcY();
  }

  this.funcY = function() {
    this.funcZ();
  }

  this.funcZ = function() {
    console.trace('trace car')
  }
}
func1();
// 使用console.trace (仅仅只是在控制台中跟踪) 可以方便地调试JavaScript.想象一下，要查看第24行car实例调用函数funcZ的整个堆栈跟踪信息：

