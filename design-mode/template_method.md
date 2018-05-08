## 模板方式模式
定义一个操作中的算法的骨架, 而将一些步骤延迟到子类中.模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤.

### 模板方法模式(TemplateMethod)结构图
```uml
@startuml
abstract class AbstractClass{
    +TemplateMethod()
    +PrimitiveOperation1()
    +PrimitiveOperation2()
}
class ConcreteClass{
    +PrimitiveOperation1()
    +PrimitiveOperation2()
}

ConcreteClass--|>AbstractClass
note left of AbstractClass: 实现了一个模板方法\n定义了算法的骨架\n具体子类将重定义PrimitiveOperation\n以实现一个算法的步骤
note left of ConcreteClass: 实现PrimitiveOperation\n以完成算法中与特定子类相关的步骤
@enduml
```

- 把不变行为搬移到超类,去除子类中的重复代码
- 提供了一个很好的代码复用平台
- 利用模板方法模式提取类库中的公共行为到抽象类中(.net,java)



