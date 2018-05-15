## 单例模式
保证一个类仅有一个实例,并提供一个访问它的全局访问点.

所有类都有构造方法,不编码则系统默认生成空的构造方法,若有显示定义的构造方法,默认的构造方法就会失效.

**只要将类的构造方法写成是private的,那么外部程序就不能用new来实例化它.**

**但是我们可以再写一个public方法,叫做GetInstance(),这个方法的目的就是返回一个类实例.**

- 通常我们可以让一个全局变量使得一个对象被访问,但它不能防止你实例化多个对象
- 一个最好的方法就是让类自身负责保存它的唯一实例
- 这个类可以保证没有其他实例可以被创建,并且它可以提供一个访问该实例的方法

### 单例模式(Singleton)结构图
```uml
@startuml
class Singleton{
    -instance:Singleton
    -Singleton()
    +GetInstance()
}
note left of Singleton: Singleton类\n定义一个GetInstance操作\n允许客户访问他的唯一实例\nGetInstance是一个静态方法\n主要负责创建自己的唯一实例
@enduml
```

### 优点
- 对唯一实例的受控访问

### 与实用类(如Math等)的区别
|实用类|单例类
|-|-
|不保存状态,仅提供一些静态方法或静态属性|有状态的
|不能用于继承多态|可以有子类来继承
|一些方法属性的集合|有着唯一的对象实例

**多线程同时调用GetInstance(),会有可能造成创建多个实例,所以需要锁处理**

### 锁处理
lock是确保当一个线程位于代码的临界区时,另外一个线程不进入临界区.如果其他线程试图进入锁定的代码,则它将一直等待(即被阻止),直到该对象被释放.

```C#
// 程序运行时创建一个静态只读的进程辅助对象
private static readonly object syncRoot=new Object();
public statice Singleton GetInstance(){
    if (instance==null){
        // 不直接lock(instance)是因为instance未创建
        look(syncRoot){
            // 再加一层判断是因为多线程同时调用时,都可以通过上面的第一层判断(那时还没lock)
            if (instance==null){
                instance=new Singleton();
            }
        }
    }
    return instance;
}
```

### 静态初始化
C#提供静态初始化方法,即可解决多线程环境下不安全问题,如下:

```c#
public sealed class Singleton{
    private static readonly Singleton instance=new Singleton();
    private Singleton(){}
    public static Singleton GetInstance(){
        return instance;
    }
}
```