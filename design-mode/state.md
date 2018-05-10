## 状态模式
当一个对象的内在状态改变时,允许改变其行为,这个对象看起来像是改变了其类.

状态模式主要解决的是当控制一个对象状态转换的条件表达式过于复杂时的情况.  
把状态的判断逻辑转移到表示不同状态的一系列类当中,可以把复杂的判断逻辑简化.

如果这个状态判断很简单,那就没必要用状态模式了.

### 状态模式(State)结构图
```uml
@startuml
abstract class State{
    +Handle(Context)
}
class Context{
    -state: State
    +Request()
}
class ConcreteStateA{
    +Handle()
}
class ConcreteStateB{
    +Handle()
}
class ConcreteStateC{
    +Handle()
}
ConcreteStateA--|>State
ConcreteStateB--|>State
ConcreteStateC--|>State
Context o-->State
note bottom of State: 抽象状态类\n定义一个接口以封装与Context的一个特定状态相关的行为
note bottom of Context: 维护一个ConcreteState子类的实例\n这个实例定义当前的状态
note "具体状态\n每一个子类实现一个与Context的一个状态相关的行为" as n1
ConcreteStateA..n1
n1..ConcreteStateB
ConcreteStateC..n1
@enduml
```

### 状态模式的好处
- 将与特定状态相关的行为局部化,并且将不同状态的行为分割开来
- 通过定义新的子类可以很容易地增加新的状态和转换
- 消除庞大的条件分支语句
- 状态模式通过把各种状态转移逻辑分布到State的子类之间,来减少相互间的依赖

### 什么时候使用状态模式
当一个对象的行为取决于它的状态,并且它必须在运行时刻根据状态改变它的行为时
