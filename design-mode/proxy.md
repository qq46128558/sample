## 代理模式
为其他对象提供一种代理以控制对这个对象的访问.

### 代理模式(Proxy)结构图
```uml
@startuml
abstract class Subject{
    +Request()
}
class RealSubject{
    +Request()
}
class Proxy{
    -realSubject: RealSubject
    +Request()
}
class Client

Client-->Subject
RealSubject--|>Subject
Proxy--|>Subject
Proxy-->RealSubject

note bottom of Subject: Subject类,定义了RealSubject和Proxy的共用接口\n这样就在任何使用RealSubject的地方都可以使用Proxy
note left of RealSubject: RealSubject类,定义Proxy所代表的真实实体
note left of Proxy: Proxy类,保存一个引用使得代理可以访问实体\n并提供一个与Subject的接口相同的接口\n这样代理就可以用来替代实体

@enduml
```

### 应用场景
- 远程代理,也就是为一个对象在不同的地址空间提供局部代表.这样可以隐藏一个对象存在于不同地址空间的事实.
    - WebService应用,客户端调用代理就可以远程访问
- 虚拟代理,是根据需要创建开销很大的对象.通过它来存放实例化需要很长时间的真实对象.
    - 浏览器使用代理模式来优化下载
- 安全代理,用来控制真实对象访问时的权限.
- 智能指引,是指当调用真实对象时,代理处理另外一些事.
    - 如计算真实对象的引用次数,当该对象没有引用时,可以自动释放它
    - 第一次引用一个持久对象时,将它装入内存
    - 访问一个实际对象前,检查是否已经锁定它,以确保其他对象不能改变它
    - 它们都是通过代理在访问一个对象时附加一些内务处理

代理模式其实就是在`访问对象时引入一定程度的间接性`,因为这种间接性,可以附加多种用途.


