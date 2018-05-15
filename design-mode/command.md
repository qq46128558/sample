## 命令模式
将一个请求封装为一个对象,从而使你可用不同的请求对客户进行参数化.对请求排队或记录请求日志,以及支持可撤消的操作.

### 命令模式(Command)结构图
```uml
@startuml
class Client
class Invoker{
    -command:Command
    +SetCommand()
    +ExecuteCommand()
}
abstract class Command{
    #receiver:Receiver
    +Execute()
}
class ConcreteCommand{
    +Execute()
}
class Receiver{
    +Action()
}
Client..>Invoker
Client..>Receiver
Invoker o-->Command
ConcreteCommand--|>Command
ConcreteCommand-->Receiver
note right of Invoker:要求该命令执行这个请求
note bottom of Command:用来声明执行操作的接口
note top of ConcreteCommand:将一个接收者对象绑定于一个动作\n调用接收者相应的操作,以实现Execute
note bottom of Receiver:知道如何实施与执行一个请求相关的操作\n任何类都可能作为一个接收者
@enduml
```

### 优点
- 它能较容易地设计一个命令队列
- 在需要的情况下,可以较容易地将命令记入日志
- 允许接收请求的一方决定是否要否决请求
- 可以容易地实现对请求的撤消与重做
- 增加新的具体命令类很容易
- **把请求一个操作的对象与知道怎么执行一个操作的对象分开**

**敏捷开发原则:不要为代码添加基于猜测的,实际不需要的功能**
