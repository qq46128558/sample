## 建造者模式
又叫生成器模式,将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以创建不同的表示.


### 建造者模式(Builder)结构图
```uml
@startuml
class Director{
    -Builder builder
    +Construct()
}
abstract class Builder{
    +BuildPart()
    +GetResult()
}
class ConcreteBuilder{
    -Product product
    +BuildPart()
    +GetResult()
}
class Product{
    +Add(part)
    +Show()
}
Director o-->Builder
ConcreteBuilder--|>Builder
ConcreteBuilder..>Product
note left of Director: 指挥者\n构建一个使用Builder接口的对象
note bottom of Builder: Builder是为创建一个Product对象的各个部件指定的抽象接口
note top of ConcreteBuilder: 具体建造者\n实现Builder接口\n构造和装配各个部件
note bottom of Product: 具体产品
@enduml
```

### 什么时候使用建造者模式
主要是用于创建一些复杂的对象, 这些对象内部构建间的建造顺序通常是稳定的, 但对象内部的构建通常面临着复杂的变化.

建造者模式是在, 当 创建复杂对象的算法 应该 独立于 该对象的组成部分 以及它们的装配方法时适用的模式.

