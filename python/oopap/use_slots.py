#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用__slots__'

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    # 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
    __slots__=('name','age','score','set_age','set_score')
    

s=Student()
# 然后，尝试给实例绑定一个属性：
s.name='Michael'
# 还可以尝试给实例绑定一个方法：
def set_age(self,age):
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print ('01.',s.age)
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score=score
Student.set_score=set_score
# 给class绑定方法后，所有实例均可调用：
s.set_score(90)
print('02.',s.score)
# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class GraduateStudent(Student):
    pass
g=GraduateStudent()
g.nickname='Kate'

