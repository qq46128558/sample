## [plantuml-markdown](https://github.com/shenjian74/plantuml-markdown "https://github.com/shenjian74/plantuml-markdown")


[使用手册](http://plantuml.com/PlantUML_Language_Reference_Guide.pdf "http://plantuml.com/PlantUML_Language_Reference_Guide.pdf")


## 类图

- 继承 (extension) <|--
- 合成 (composition) *--
- 聚合 (aggregation) o--

使用”..” 来代替”--” 可以得到点线

```uml
@startuml
Class01 <|-- Class02
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 -- Class10
@enduml

@startuml
Class11 <|.. Class12
Class13 --> Class14
Class15 ..> Class16
Class17 ..|> Class18
Class19 <--* Class20
@enduml

@startuml
Class21 #-- Class22
Class23 x-- Class24
Class25 }-- Class26
Class27 +-- Class28
Class29 ^-- Class30
@enduml
```


- 在关系之间使用标签来说明时, 使用”:” 后接标签文字。
- 对元素的说明，你可以在每一边使用 "" 来说明.

```uml
@startuml
Class01 "1" *-- "many" Class02 : contains
Class03 o-- Class04 : aggregation
Class05 --> "1" Class06
@enduml
```

- 在标签的开始或结束位置添加 < 或 > 以表明是哪个对象作用到哪个对象上。

```uml
@startuml
class Car
Driver - Car : drives >
Car *- Wheel : have 4 >
Car -- Person : < owns
@enduml
```

- 为了声明域或者方法，你可以使用后接域名或方法名
- 系统检查是否有括号来判断是方法还是域。

```uml
@startuml
Object <|-- ArrayList
Object : equals()
ArrayList : Object[] elementData
ArrayList : size()
@enduml
```
