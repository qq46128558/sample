## 原型模式
用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象.

- 一般在初始化信息不发生变化的情况下,克隆是最好的办法
- 不用重新初始化对象


### 原型模式(Prototype)结构图
```
@startuml
class Client{
    -prototype: Prototype
}
abstract class Prototype{
    +Clone()
}
class ConcretePrototype1{
    +Clone()
}
class ConcretePrototype2{
    +clone()
}

Client-->Prototype
ConcretePrototype1--|>Prototype
ConcretePrototype2--|>Prototype
note top of Client: 让一个原型克隆自身\n从而创建一个新的对象
note bottom of Prototype: 原型类,声明一个克隆自身的接口
note "具体原型类,实现一个克隆自身的操作" as n1
ConcretePrototype1..n1
n1..ConcretePrototype2

@enduml
```

**原型抽象类Prototype对应.NET提供的ICloneable接口**


- 浅复制: 对象的引用仍然指向原来的对象
- 深复制: 引用对象指向复制的新对象