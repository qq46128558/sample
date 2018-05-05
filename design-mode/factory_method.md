## 工厂方法模式
定义一个用于创建对象的接口,让子类决定实例化哪一个类.工厂方法使一个类的实例化延迟到其子类.

- **符合开放-封闭原则**
- 工厂方法把简单工厂的内部逻辑判断移到了客户端代码来进行
- 工厂方法模式是简单工厂模式的进一步抽象和推广


**区别简单工厂模式**
简单工厂模式的最大优点在于工厂类中包含了必要的逻辑判断,根据客户端的选择条件动态实例化相关的类,对于客户端来说,去除了与具体产品的依赖.

### 工厂方法模式(Factory Method)结构图
```uml
@startuml
class Product
class ConcreteProduct
interface Creator{
    +FactoryMethod()
}
Class ConcreteCreator{
    +FactoryMethod()
}
ConcreteProduct--|>Product
ConcreteCreator--|>Creator
ConcreteCreator..>ConcreteProduct

note bottom of Product: 定义工厂方法所创建的对象的接口
note left of ConcreteProduct: 具体的产品,实现了Product接口
note bottom of Creator: 声明工厂方法,该方法返回一个Product类型的对象
note left of ConcreteCreator: 重定义工厂方法以返回一个ConcreteProduct实例
@enduml
```

