## UML 类图

```uml
UML 类图图示样例
@startuml
abstract class 动物 {
    +有生命
    +新陈代谢(in o2:氧气 in warter:水)
    +繁殖()
}
class 氧气
class 水
abstract class 鸟{
    +羽毛
    +有角质喙没有牙齿
    +下蛋()
}
class 翅膀
class 鸭{
    +下蛋()
}
class 企鹅{
    +下蛋()
}
class 气候
class 大雁{
    +下蛋()
    +飞()
}
class 雁群{
    +V形飞行()
    +一形飞行()
}
interface 飞翔{
    +飞()
}
class 唐老鸭{
    +讲话()
}
讲人话()--唐老鸭

note right of 动物: 类\n第一行:类名称\n第二行:特性\n第三行操作\n类名为斜体,此类为抽象类

动物..>氧气
动物..>水
note "依赖关系" as n1
动物..n1
n1..水
动物..n1
n1..氧气

鸟--|>动物
note "合成(组合)关系" as n2
鸟 "1" *-->"2" 翅膀
鸟..n2
n2..翅膀
鸭--|>鸟
企鹅--|>鸟
企鹅-->气候
note "关联关系" as n3
企鹅..n3
n3..气候
大雁--|>鸟
雁群 o-->大雁
note "聚合关系" as n4
大雁..n4
n4..雁群
大雁..|>飞翔
note "实现接口" as n5
大雁..n5
n5..飞翔
note bottom of 飞翔: 接口\n矩形表示法\n第一行:接口名称\n第二行:接口方法
唐老鸭--|>鸭
note top of 唐老鸭: 接口\n棒棒糖表示法\n圆圈旁为接口名称\n接口方法在实现类中出现

@enduml
```