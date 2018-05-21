## 访问者模式
表示一个作用于某对象结构中的各元素的操作.它使你可以在不改变各元素的类的前提下定义作用于这些元素的新操作.

### 访问者模式(Visitor)结构图
```uml
@startuml
class Client
abstract class Visitor{
    +VisitConcreteElementA(in:ConcreteElementA)
    +VisitConcreteElementB(in:ConcreteElementB)
}
class ConcreteVisitor1{
    +VisitConcreteElementA(in:ConcreteElementA)
    +VisitConcreteElementB(in:ConcreteElementB)
}
class ConcreteVisitor2{
    +VisitConcreteElementA(in:ConcreteElementA)
    +VisitConcreteElementB(in:ConcreteElementB)
}
class ObjectStructure{
    -elements:IList<Element>
    +Attach(in:Element)
    +Detach(in:Element)
    +Accept(in:Visitor)
}
abstract class Element{
    +Accept(in visitor:Visitor)
}
class ConcreteElementA{
    +Accept(in visitor:Visitor)
    +OperationA()
}
class ConcreteElementB{
    +Accept(in visitor:Visitor)
    +OperationB()
}
Client-->Visitor
Client-->ObjectStructure
ObjectStructure-->Element
ConcreteElementA--|>Element
ConcreteElementB--|>Element
ConcreteVisitor1--|>Visitor
ConcreteVisitor2--|>Visitor
note bottom of Visitor:为该对象结构中ConcreteElement的\n每一个类声明一个Visit操作
note "具体访问者\n实现每个由Visitor声明的操作\n每个操作实现算法的一部分\n而该算法片断乃是对应于结构中对象的类" as n1
n1..ConcreteVisitor1
ConcreteVisitor2..n1
note bottom of ObjectStructure:能枚举它的元素\n可以提供一个高层的接口以允许访问者访问它的元素
note bottom of Element:定义一个Accept操作\n它以一个访问者为参数
note "具体元素\n实现Accept操作" as n2
ConcreteElementA..n2
n2..ConcreteElementB
@enduml
```

- Element是固定的分类
- Visitor是状态

### 应用场景
- 访问者模式适用于数据结构相对稳定的系统
- 有比较稳定的数据结构,又有易于变化的算法

### 优点
- 增加新的操作很容易,因为增加新的操作就意味增加一个新的访问者.
- 访问者模式将有关的行为集中到一个访问者对象中.

### 缺点
- 使增加新的数据结构变得困难.

