## 面向对象基础

- 类,就是具有相同的属性和功能的对象的抽象的集合
    - 类是对象的抽象
- 实例,就是一个真实的对象
- 构造方法,又叫构造函数,其实就是对类进行初始化
- 方法重载,提供了创建同名的多个方法的能力
- 属性,是一个方法或一对方法(get,set)
- 封装,每个对象都包含它能进行操作所需要的所有信息,这个特性称为封装,因此对象不必依赖其他对象来完成自己的操作
- 继承,对象的继承代表了一种is-a的关系,如果两个对象A和B,可以描述为B是A,则表明B可以继承A(构造方法不能被继承,只能被调用)
- 多态,表示不同的对象可以执行相同的动作,但要通过它们自己的实现代码来执行
- 修饰符virtual,表示虚方法,可以被子类重写
- 抽象类,通常代表一个抽象概念,它提供一个继承的出发点,当设计一个新的抽象类时,一定是用来继承的,所以,在一个以继承关系形成的等级结构里面,树叶节点应当是具体类,而树枝节点均应当是抽象类
    - 抽象类是对类的抽象
    - 抽象类可以给出一些成员的实现
    - 抽象类的抽象成员可被子类部分实现
    - 一个类只能继承一个抽象类
    - 对于一些相似的类的抽象,用继承抽象类
- 接口,是把隐式公共方法和属性组合起来,以封装特定功能的一个集合.实现接口的类就必须要实现接口中的所有方法和属性.
    - 接口是对行为的抽象
    - 接口不包含成员的实现
    - 接口的成员需要实现类完全实现
    - 一个类可以支持多个接口,多个类也可以支持相同的接口.
    - 如果行为跨越不同类的对象,可使用接口
- 装箱,就是把值类型打包到Object引用类型的一个实例中
    - `int i=123;`
    - `object o=(object)i;`
- 拆箱,就是指从对象中提取值类型
    - `o=123;`
    - `i=(int)o`

### 集合
```c#
using System.Collections;
IList arrayAnimal;
```

### 泛型
```C#
using System.Collections.Generic;
IList<Animal> arrayAnimal;
```

### 委托与事件
```C#
class CatShoutEventArgs:EventArgs{}
class cat{
    // 声明委托
    public delegate void CatShoutEventHandler(object sender,CatShoutEventArgs args);
    // 声明事件,事件类型是委托
    public event CatShoutEventHandler CatShout;
    public void Shout(){
        CatShoutEventArgs e=new CatShoutEventArgs();
        CatShout(this,e);
    }
}
class mouse{
    public void Run(object sender,CatShoutEventArgs args){}
}
static void Main(string[] args){
    cat.CatShout+=new Cat.CatShoutEventHandler(mouse1.Run);
    cat.Shout();
}
```