## 解释器模式
给定一个语言,定义它的文法的一种表示,并定义一个解释器,这个解释器使用该表示来解释语言中的句子.

如果一种特定类型的问题发生的频率足够高,那么可能就值得将该问题的各个实例表述为一个简单语言中的句子.这样就可以构建一个解释器,该解释器通过解释这些句子来解决该问题.

### 优点
很容易地改变和扩展文法,因为该模式使用类来表示文法规则,你可使用继承来改变或扩展文法.也比较容易实现文法,因为定义抽象语法树中各个节点的类的实现大体类似,这些类都易于直接编写.

### 不足
解释器模式为文法中的每一条规则至少定义了一个类,因此包含许多规则的文法可能难以管理和维护.建议当文法非常复杂时,使用其他的技术如语法分析程序或编译器生成器来处理.

### 实际应用场景
- 正则表达式
- 浏览器

### 解释器模式(Interpreter)结构图
```uml
@startuml
class Client
class Context{
    -input:String
    -output:String
}
abstract class AbstractExpression{
    +Interpret(in context:Context)
}
class TerminalExpression{
    +Interpret(in context:Context)
}
class NonterminalExpression{
    +Interpret(in context:Context)
}
TerminalExpression--|>AbstractExpression
NonterminalExpression--|>AbstractExpression
AbstractExpression o--> Context
Client-->Context
Client-->AbstractExpression
note bottom of Context:包含解释器之外的一些全局信息
note bottom of AbstractExpression:抽象表达式\n声明一个抽象的解释操作\n这个接口为抽象语法树中所有的节点所共享
note top of TerminalExpression:终结符表达式\n实现与文法中的终结符相关联的解释操作
note top of NonterminalExpression:非终结符表达式\n为文法中的非终结符实现解释操作\n对文件中的每一条规则R1,R2...Rn都需要一个具体非终结符表达式类
@enduml
```

客户端代码
```C#
Context context=new Context();
IList<AbstractExpression> list=new List<AbstractExpression>();
list.Add(new TerminalExpression());
list.Add(new NonterminalExpression());
list.Add(new TerminalExpression());
list.Add(new TerminalExpression());

foreach(AbstractExpression exp in list){
    exp.Interpret(context);
}
```

### 应用场景
- 当有一个语言需要解释执行,并且你可将该语言中的句子表示为一个抽象语法树时
