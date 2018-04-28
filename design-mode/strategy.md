## 策略模式
策略模式是一种定义一系列算法的方法,从概念上来看,所有这些算法完成的都是相同的工作,只是实现不同,它可以以相同的方式调用所有的算法,减少了各种算法类与使用算法类之间的耦合.

- 简化了单元测试,每个算法都有自己的类,可能通过自己的接口单独测试
- 用来封装算法,封装任何类型的规则
- 只要在分析过程中听到:**需要在不同时间应用不同的业务规则**,就可以考虑使用策略模式
- Context中用到了switch不够完美,但可以用反射技术(抽像工厂模式中讲解)

### 策略模式结构图

```uml
@startuml
class Context{
    +ContextInterface()
}
abstract class Strategy{
    +AlgorithmInterface()
}
class ConcreteStrategyA{
    +AlgorithmInterface()
}
class ConcreteStrategyB{
    +AlgorithmInterface()
}
class ConcreteStrategyC{
    +AlgorithmInterface()
}

note top of Context: Context上下文\n用一个ConcreteStrategy来配置维护一个对Strategy对象的引用
Context o--> Strategy
note bottom of Strategy: 策略类\n定义所有支持的算法的公共接口
ConcreteStrategyA --|> Strategy
ConcreteStrategyB --|> Strategy
ConcreteStrategyC --|> Strategy
note "具体策略类\n封装了具体的算法或行为\n继承于Strategy" as n1
ConcreteStrategyA..n1
ConcreteStrategyB..n1
ConcreteStrategyC..n1

@enduml
```

~~~
// 简单工厂模式的用法 (两个类)
CashSuper csuper = CashFactory.createCashAccept(str);
...=csuper.GetResult(...)

// 策略模式与简单工厂结合的用法 (一个类,耦合更低)
CashContext csuper = new CashContext(str);
...=csuper.GetResult(...)
~~~
