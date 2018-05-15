## 职责链模式
使多个对象都有机会处理请求,从而避免请求的发送者和接收者之间的耦合关系.将这个对象连成一条链,并沿着这条链传递请求,直到有一个对象处理它为止.

### 职责链模式(Chain of Responsibility)结构图
```uml
@startuml
class Client
abstract class Handler{
    #successor:Handler
    +SetSuccessor(in successor:Handler)
    +HandleRequest(in request:int)
}
class ConcreteHandler1{
    +HandleRequest(in request:int)
}
class ConcreteHandler2{
    +HandleRequest(in request:int)
}
Client-->Handler
ConcreteHandler1--|>Handler
ConcreteHandler2--|>Handler
ConcreteHandler2 o--> Handler
note bottom of Handler:定义一个处理请求的接口
note "具体处理类\n处理它所负责的请求\n可访问它的后继者,如果可处理该请求\n就处理之,否则就将该请求转发给它的后继者" as n1
ConcreteHandler1..n1
n1..ConcreteHandler2
@enduml
```

### 优点
