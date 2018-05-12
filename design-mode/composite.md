## 组合模式
将对象组合成树形结构以表示'部分-整体'的层次结构.组合模式使得用户对单个对象和组合对象的使用具有一致性.

### 组合模式(Composite)结构图
```uml
@startuml
class Client
abstract class Component{
    +Add(in c:Component)
    +Remove(in c:Component)
    +Display(in depth:int)
}
class Leaf{
    +Display(in depth:int)
}
class Composite{
    -children:List<Component>
    +Add(in c:Component)
    +Remove(in c:Component)
    +Display(in depth:int)
}
Client-->Component
Leaf--|>Component
Composite--|>Component
Composite o-->Component
note bottom of Component: 组合中的对象声明接口\n在适当情况下\n实现所有类共有接口的默认行为\n声明一个接口用于访问和管理Component的子部件
note top of Leaf: 在组合中表示叶节点对象\n叶节点没有子节点
note top of Composite: 定义有枝节点行为\n用来存储子部件\n在Component接口中实现与子部件有关的操作\n比如增加Add和删除Remove
@enduml
```

### 透明方式
在Component中声明所有用来管理子对象的方法,其中包括Add,Remove等,这样实现Component接口的所有子类都具备了Add和Remove.这样做的好处就是叶节点和枝节点对于外界没有区别,它们具备完全一致的行为接口.但问题也很明显,因为Leaf类本身不具备Add(),Remove()方法的功能,所以实现它是没有意义的.

### 安全方式
在Component接口中不去声明Add和Remove方法,那么子类的Leaf也就不需要去实现它,而是在Composite声明所有用来管理子类对象的方法,不过由于不够透明,所以树叶和树枝类将具有不同的接口,客户端的调用需要做相应的判断,带来了不便.

### 什么时候使用组合模式
- 需求中是体现部分与整体层次结构时
- 希望用户可以忽略组合对象与单个对象的不同,统一地使用组合结构中的所有对象时

### 组合模式的好处
- 让客户可以一致地使用组合结构和单个对象
- 基本对象可以被组合成更复杂的组合对象,而这个组合对象又可以被组合,不断地递归下去