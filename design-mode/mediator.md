## 中介者模式
用一个中介对象来封装一系列的对象交互.中介者使各对象不需要显式地相互引用,从而使其耦合松散,而且可以独立地改变它们之间的交互.

### 中介者模式(Mediator)结构图
```uml
@startuml
abstract class Mediator{
    +Send()
}
class ConcreteMediator{
    -colleague1:ConcreteColleague1
    -colleague2:ConcreteColleague2
    +Send()
}
abstract class Colleague{
    #mediator:Mediator
}
class ConcreteColleague1{
    +Send()
    +Notify()
}
class ConcreteColleague2{
    +Send()
    +Notify()
}
ConcreteMediator--|>Mediator
ConcreteColleague1--|>Colleague
ConcreteColleague2--|>Colleague
Colleague o-->Mediator
ConcreteMediator-->ConcreteColleague1
ConcreteMediator-->ConcreteColleague2
note bottom of Mediator:抽象中介者\n定义了同事对象到中介者对象的接口
note left of ConcreteMediator:具体中介者对象\n实现抽象类的方法\n它需要知道所有具体同事类\n并从具体同事接收消息\n向具体同事对象发出命令
note right of Colleague:抽象同事类
note "具体同事类\n每个具体同事只知道自己的行为\n而不了解其它同事类的情况\n但它们却都认识中介者对象" as n1
ConcreteColleague1..n1
n1..ConcreteColleague2
@enduml
```

### 优点
- Mediator的出现减少了Colleague的耦合
- 关注的对象就从对象各自本身的行为转移到它们之间的交互上来
- ConcreteMediator控制了集中化

### 缺点
- 把交互复杂性变为了中介者的复杂性,使得中介者会变得比任何一个ConcreteColleague都复杂

### 典型的中介者模式
计算器程序  
各个控件都有事件机制,而事件的执行都是在Form窗体的代码中完成,也就是说所有的控件交互都是由Form窗体来作中介,操作各个对象,这是典型的中介者模式应用.

### 应用场景
- 一组对象以定义良好但是复杂的方式进行通信的场合
- 定制一个分布在多个类中的行为,而又不想生成太多的子类的场合

