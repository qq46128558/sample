## 迭代器模式
提供一种方法顺序访问一个聚合对象中各个元素,而又不暴露该对象的内部表示.

- 为遍历不同的聚集结构提供开始,下一个,是否结束,当前哪一项等统一的接口
- 高级编程语言已经把这个模式做在语言中了: foreach

### 何时使用迭代器模式
- 当你需要访问一个聚集对象,而且不管这些对象是什么都需要遍历的时候
- 你需要对聚集有多种方式遍历时(由于继承Iterator,所以增加ConcreteIteratorX即可多方式遍历)


### 迭代器模式(Iterator)结构图
```uml
@startuml
class Client
abstract class Aggregate{
    +CreateIterator():Iterator
}
class ConcreteAggregate{
    -items:IList<object>
    +CreateIterator():Iterator
    +Count
    +this[int index]:object
}
abstract class Iterator{
    +First()
    +Next()
    +IsDone()
    +CurrentItem()
}
class ConcreteIterator{    
    -aggregate:ConcreteAggregate
    -current:int
}
Client-->Iterator
Client-->Aggregate
ConcreteAggregate--|>Aggregate
ConcreteIterator--|>Iterator
ConcreteAggregate..>ConcreteIterator
ConcreteIterator-->ConcreteAggregate
note left of Aggregate: 聚集抽象类
note bottom of ConcreteAggregate: 具体聚集类,继承Aggregate
note left of Iterator: 迭代抽象类,用于定义\n得到开始对象\n得到下一对象\n判断是否结尾\n当前对象\n等抽象方法,统一接口
note top of ConcreteIterator: 具体迭代器类,继承Iterator\n实现开始,下一个,是否结尾,当前对象\n等方法
@enduml
```


```c#
class ConcreteAggregate:Aggregate{
    private IList<object> items=new List<object>();
    public override Iterator CreateIterator(){
        return new ConcreteIterator(this);
    }
    public int Count{
        get {return items.Count;}
    }
    public object this[int index]{
        get {return items[index];}
        set {items.Insert(index,value);}
    }
}
```


```c#
// foreach in在编译器里做了些什么?
IEnumerator<string> e=xxx.GetEnumerator();
while (e.MoveNext()){
    return e.Current;
}
```

### 优点
迭代器(Iterator)模式就是分离了集合对象的遍历行为,抽象出一个迭代器类来负责,这样既可以做到不暴露集合的内部结构,又可以让外部代码透时地访问集合内部的数据.

