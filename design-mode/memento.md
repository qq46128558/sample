## 备忘录模式
在不破坏封装性的前提下,捕获一个对象的内部状态,并在该对象之外保存这个状态.这样以后就可将该对象恢复到原先保存的状态.

### 备忘录模式(Memento)结构图
```uml
@startuml
class Originator{
    +State
    +SetMemento(in m: Memento)
    +CreateMemento()
}
class Memento{
    +State
}
class Caretaker{
    -Memento: Memento
}
Originator..>Memento
Caretaker o-->Memento
note top of Originator: 负责创建一个备忘录Memento\n用以记录当前时刻它的内部状态\n并可使用备忘录恢复内部状态
note bottom of Memento: 负责存储Originator对象的内部状态\n并可防止Originator以外的其他对象访问备忘录Memento
note top of Caretaker: 负责保存好备忘录Memento
@enduml
```

**把要保存的细节给封装在Memento中**

### 什么时候使用备忘录模式
- 适用于功能比较复杂的,但需要维护或记录属性历史的类 
- 需要保存的属性只是众多属性中的一小部份时,Originator可以根据保存的Memento信息还原到前一状态
- 命令模式可以使用备忘录模式来存储可撤消操作的状态
- 使用备忘录可以把复杂的对象内部信息对其他的对象屏蔽起来
- 当角色状态改变时,有可能这个状态无效,这时候可以使用暂时存起来的备忘录将状态复原

### 缺点
如果状态数据很大很多,备忘录对象会耗内存

