## 享元模式
运用共享技术有效地支持大量细粒度的对象.

### 享元模式(Flyweight)结构图
```uml
@startuml
class FlyweightFactory{
    -flyweights:Hashtable
    GetFlyweight(in key:string):Flyweight
}
abstract class Flyweight{
    +Operation(in extrinsicstate:int)
}
class ConcreteFlyweight{
    +Operation(in extrinsicstate:int)
}
class UnsharedConcreteFlyweight{
    +Operation(in extrinsicstate:int)
}
class Client
FlyweightFactory o-->Flyweight
ConcreteFlyweight--|>Flyweight
UnsharedConcreteFlyweight--|>Flyweight
Client-->FlyweightFactory
Client-->ConcreteFlyweight
Client-->UnsharedConcreteFlyweight
note top of FlyweightFactory: 一个享元工厂,用来创建并管理Flyweight对象\n它主要是用来确保合理地共享Flyweight\n当用户请求一个Flyweight时\nFlyweightFactory对象提供一个已创建的实例或者创建一个(如不存在)
note bottom of Flyweight: 所有具体享元类的超类或接口\n通过这个接口\nFlyweight可以接受并作用于外部状态
note top of ConcreteFlyweight: 继承Flyweight超类或实现Flyweight接口\n并为内部状态增加存储空间
note bottom of UnsharedConcreteFlyweight: 指那些不需要共享的Flyweight子类\n因为Flyweight接口共享成为可能\n但它并不强制共享
@enduml
```

### 为什么要有UnsharedConcreteFlyweight的存在
大部分时间都需要共享对象来降低内存的损耗,但个别时候也有可能不需要共享的,那么此时UnsharedConcreteFlyweight子类就有存在的必要了,它可以解决那些不需要共享对象的问题.


### 应用场景
- 一个应用程序使用了大量的对象,而大量的这些对象造成了很大的存储开销时
- 对象的大多数状态可以外部状态,如果删除对象的外部状态,那么可以用相对较少的共享对象取代很多组对象
- 有足够多的对象实例可供共享时

### 实际应用
```c#
string titleA="大话设计模式";
string titleB="大话设计模式";
Console.WriteLine(Object.ReferenceEquals(titleA,titleB));
// 返回true,说明这两个字符串是相同的实例
```

### 其他应用(如棋类游戏)
- 大量的棋子对象
- 颜色是内部状态
- 方位坐标是外部状态
