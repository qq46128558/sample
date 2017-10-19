#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用@property'
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('Score must be an integer!')
        if value<0 or value>100:
            raise ValueError('Score must between 0~100!')
        self._score=value

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student2(object):
    # 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('Score must be an integer!')
        if value<0 or value>100:
            raise ValueError('Score must between 0~100!')
        self._score=value

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value
    # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    @property
    def age(self):
        return 2017-self._birth


s=Student2()
s.birth=1997
print('01.',s.age)
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._width*self._height

s=Screen()
s.width=1024
s.height=768
print('02.',s.resolution)
# python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常。
assert s.resolution==786432,'1024 * 768 = %d ?'%s.resolution
