## 观察者模式
又叫做发布-订阅模式, 定义了一种一对多的依赖关系, 让多个观察者对象同时监听某一个主题对象. 这个主题对象在状态发生变化进, 会通知所有观察者对象, 使它们能够自动更新自己.

### 观察者模式(Observer)结构图
```uml
@startuml
abstract class Subject{
    -IList<Observer> observers
    +Attach(in: Observer)
    +Detach(in: Observer)
    +Notify()
}
abstract class Observer{
    +Update()
}
class ConcreteSubject{
    +SubjectState
}
class ConcreteObserver{
    -String name
    -Subject ConcreteSubject
    -String observerState
    +Update()
}
ConcreteSubject--|>Subject
ConcreteObserver--|>Observer
Subject-->Observer
ConcreteObserver-->ConcreteSubject
note left of Subject: Subject类,抽象主题\n它把所有观察者对象的引用保存在一个聚集里\n每个主题都可以有任何数量的观察者\n抽象主题提供一个接口\n可以增加和删除观察者对象
note left of ConcreteSubject: ConcreteSubject类,具体主题\n将有关状态存入具体观察者对象\n在具体主题的内部状态改变时\n给所有登记过的观察者发出通知
note left of Observer: Observer类, 抽象观察者\n为所有的具体观察者定义一个接口\n在得到主题的通知时更新自己
note left of ConcreteObserver: ConcreteObserver类,具体观察者\n实现抽象观察者角色所要求的更新接口\n以便使本身的状态与主题的状态相协调
@enduml
```

**将一个系统分割成一系列相互协作的类有一个很不好的副作用, 那就是需要维护相关对象间的一致性. 我们不希望为了维持一致性而使各类紧密耦合, 这样会给维护,扩展和重用都带来不便**

### 什么时候使用观察者模式
- 当一个对象的改变需要同时改变其他对象的时候
- 而且它不知道具体有多少对象有待改变时

观察者模式所做的工作其实就是在解除耦合.让耦合的双方都依赖于抽象, 而不是依赖于具体.从而使得各自的变化都不会影响另一边的变化.(依赖倒转原则的最佳体现)

**抽象观察者也可以用接口来定义**


### 事件委托
```c#
// 声明一个委托
delegate void EventHandler();
// 声明一事件update,,类型为委托EventHandler
public event EventHandler Update;

public void Notify(){
    // 在访问通知方法时,调用更新
    Update();
}
...
主题实例.Update+=new EventHandler(观察者实例.方法);
```
- 委托就是一种引用方法的类型
- 一旦为委托分配了方法,委托将与该方法具有完全相同的行为
- 委托可以具有参数及返回值
- 委托的实例将代表一个具体的函数
- 一个委托可以搭载多个方法,委托对所搭载的方法并不需要属于同一个类

**先有观察者模式,再有委托事件技术**
