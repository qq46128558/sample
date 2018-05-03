## 开放-封闭原则
是说软件实体(类,模块,函数等等)应该可以扩展,但是不可修改.

- 对于扩展是开改的
- 对于更改是封闭的
- 面对需求,对程序的改动是通过增加新代码进行的
- 开放-封闭原则是面向对象设计的核心所在
- 仅对程序中呈现出频繁变化的那些部分做出抽象

```uml
@startuml
class 客户端类
abstract class 运算类{
    +NumberA: double
    +NumberB: double
    +GetResult(): double
}
class 加法类{
    +GetResult(): double
}
class 减法类{
    +GetResult(): double
}
class 乘法类{
    +GetResult(): double
}
class 除法类{
    +GetResult(): double
}

客户端类-->运算类
加法类--|>运算类
减法类--|>运算类
乘法类--|>运算类
除法类--|>运算类
@enduml
```
