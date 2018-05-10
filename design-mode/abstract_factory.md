## 抽象工厂模式
提供一个创建一系列相关或相互依赖对象的接口,而无需指定它们具体的类.

- 符合依赖倒转原则
- 符合开放-封闭原则(扩展开放,修改封闭)

### 反射技术
- using System.Reflection;
- 格式:　Assembly.Load("程序集名称").CreateInstance("命名空间.类名称")
- 反射是利用实符串来实例化对象
- 程序由编译时转为运行时


### 抽象工厂模式(Abstract Factory)结构图(简单工厂+反射改进)
抽象工厂模式当增加功能表时,涉及大量改动,所以下图用简单工厂+反射来改进
```uml
@startuml
class DataAccess{
    -db: string
    +CreateUser(): IUser
    +CreateDepartment(): IDepartment
}
interface IUser
class SqlserverUser
class AccessUser
interface IDepartment
class SqlserverDepartment
class AccessDepartment
SqlserverUser..|>IUser
AccessUser..|>IUser
SqlserverDepartment..|>IDepartment
AccessDepartment..|>IDepartment
DataAccess..>IUser
DataAccess..>IDepartment
@enduml
```

PS: 读配置文件using System.Configuration;(ConfigurationManager.AppSettings["XX"];)