## 外观模式
为子系统中的一组接口提供一个一致的界面, 此模式定义了一个高层接口, 这个接口使得这一子系统更加容易使用.

- 体现依赖倒转原则和迪米特法则

### 外观模式(Facade)结构图
```uml
@startuml
class Client
package "SubSystem Classes" #pp{
    class Facade{
        +MethodA()
        +MethodB()
    }
    class SubSystemOne{
        +MethodOne()
    }
    class SubSystemTwo{
        +MethodTwo()
    }
    class SubSystemThree{
        +MethodThree()
    }
    class SubSystemFour{
        +MethodFour()
    }
    Client-->Facade
    Facade-->SubSystemOne
    Facade-->SubSystemTwo
    Facade-->SubSystemThree
    Facade-->SubSystemFour

    note left of Facade: Facade外观类\n知道哪些子系统类负责处理请求\n将客户的请求代理给适当的子系统对象
}
note "SubSystem Classes 子系统类集合\n实现子系统的功能,处理Facade对象指派的任务\n注意子类中没有Facade的任何信息\n即没有对Facade对象的引用" as n1
@enduml
```

### 什么时候使用
- 设计初期, 有意识的将不同的两个层分离
- 开发阶段, 增加外观Facade可以提供一个简单的接口, 减少它们之间的依赖
- 维护遗留的大型系统时, 开发一个外观Facade类, 与遗留代码交互所有复杂的工作
