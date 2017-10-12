#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class student sample'
# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

# 在Python中，定义类是通过class关键字：
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
class Student(object):
    pass

# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的
print('01.',Student)
bart=Student()
print('02.',bart)
# 可以看到，变量bart指向的就是一个Student的实例，后面的0xxx是内存地址，每个object的地址都不一样，而Student本身则是一个类。
# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
bart.name='Bart Simpson'
print('03.',bart.name)


# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student2(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    # 数据封装
    # 这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
    def print_score(self):
        print('%s: %s'%(self.name,self.score))
    # 封装的另一个好处是可以给Student类增加新的方法，比如get_grade
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

''' 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。 '''

lisa=Student2('Lisa Simpson',87)
lisa.print_score()
print('04.',lisa.get_grade())
