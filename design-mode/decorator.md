## 装饰模式
动态地给一个对象添加一些额外的职责,就增加功能来说,装饰模式比生成子类更为灵活.

### 装饰模式结构图
```uml
@startuml
abstract class Component{
    +Operation()
}
class ConcreteComponent{
    +Operation()
}
abstract class Decorator{
    -component: Component
    +SetComponent()
    +Operation()
}
class ConcreteDecoratorA{
    -addedState: string
    +Operation()
}
class ConcreteDecoratorB{
    +Operation()
    -AddedBehavior()
}

ConcreteComponent--|>Component
Decorator--|>Component
Decorator o-->Component
ConcreteDecoratorA--|>Decorator
ConcreteDecoratorB--|>Decorator

note bottom of Component: Component是定义一个对象接口\n可以给这些对象动态地添加职责
note top of ConcreteComponent: ConcreteComponent是定义了一个具体的对象\n也可以给这个对象添加一些职责
note right of Decorator: Decorator,装饰抽象类\n继承了Component\n从外类来扩展Component类的功能\n但对于Component来说\n是无需知道Decorator的存在
note "ConcreteDecorator 就是具体的装饰对象\n起到给Component添加职责的功能" as n1
ConcreteDecoratorA..n1
n1..ConcreteDecoratorB
@enduml
```

装饰的方法是:
1. 用ConcreteComponent实例化对象c
2. 用ConcreteDecoratorA的实例化对象d1来包装c
3. 用ConcreteDecoratorB的实例化对象d2来包装d1
4. 最终执行d2的Operation()

~~~
ConcreteComponent c=new ConcreteComponent();
ConcreteDecoratorA d1=new ConcreteDecoratorA();
ConcreteDecoratorB d2=new ConcreteDecoratorB();
d1.SetComponent(c);
d2.SetComponent(d1);
d2.Operation();
~~~

- 装饰模式是利用SetComponent来对对象进行包装的
- 每个装饰对象的实现就和如何使用这个对象分离开了
- 每个装饰对象只关心自己的功能,不需要关心如何被添加到对象链当中
- 它把每个要装饰的功能放在单独的类中,并让这个类包装它所要装饰的对象
- `把类中的装饰功能从类中搬移去除,简化原有的类`
- 有效地把类的核心职责和装饰功能区分开
- 装饰模式的装饰顺序很重要(如加密数据和过滤词汇)

