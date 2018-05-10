## 适配器模式
将一个类的接口转换成客户希望的另外一个接口.Adapter模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作.

**类似电源适配器**

- 系统的数据和行为都正确,但接口不符时,我们应该考虑用适配器
- 适配器模式主要应用于希望复用一些现存的类,但是接口又与复用环境要求不一致的情况
- 类适配器模式
    - 多重继承(对一个接口与另外一个接口进行匹配),部份语言不支持,C++支持
- 对象适配器


### 适配器模式(Adapter)结构图
```uml
@startuml
class Client{
    -target: Target
}
class Target{
    +Request()
}
class Adapter{
    -adaptee: Adaptee
    +Request()
}
class Adaptee{
    +SpecificRequest()
}
Client-->Target
Adapter--|>Target
Adapter-->Adaptee
note left of Target: 这是客户所期待的接口\n目标可以是具体的或抽象的类\n也可以是接口
note bottom of Adapter: 通过在内部包装一个Adaptee对象\n把源接口转换成目标接口
note bottom of Adaptee: 需要适配的类
@enduml
```

### 何时使用适配器模式
- 想使用一个已存在的类,但如果它的接口,也就是它的方法和你的要求不同时
- 两个类所做的事相同或相似,但是具有不同的接口时
- 双方都不太容易修改的时候再使用适配器

**.NET中的DataAdapter就是适配器模式:不必关注不同数据库的数据细节**
