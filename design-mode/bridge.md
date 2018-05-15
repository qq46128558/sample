## 桥接模式
将抽象部分与它的实现部分分离,使它们都可以独立地变化.
实现指的是抽象类和它的派生类用来实现自己的对象(比如:让手机既可以按照品牌来分类,也可以按照功能来分类).  
实现系统可能有多角度分类,每一种分类都有可能变化,那么就把这种多角度分离出来让它们独立变化,减少它们之间的耦合.

**只要真正地理解了设计原则,很多设计模式其实就是原则的应用**
- 单一职责原则(Single Responsibility)
- 开放-封闭原则(Open Close Principle)
- 依赖倒转原则(Depend)
- 合成聚合复用原则(CARP)
- 迪米特法则(Lod)

### 桥接模式(Bridge)结构图
```uml
@startuml
class Abstraction{
    #implementor: Implementor
    +SetImplementor()
    +Operation()
}
class RefinedAbstraction{
    +Operation()
}
abstract class Implementor{
    +Operation()
}
class ConcreteImplementorA{
    +Operation()
}
class ConcreteImplementorB{
    +Operation()
}
RefinedAbstraction--|>Abstraction
ConcreteImplementorA--|>Implementor
ConcreteImplementorB--|>Implementor
Abstraction o-->Implementor
note bottom of Abstraction: 抽象
note bottom of Implementor: 实现
note top of RefinedAbstraction: 被提炼的抽象
note "具体实现" as n1
ConcreteImplementorA..n1
n1..ConcreteImplementorB

@enduml
```

