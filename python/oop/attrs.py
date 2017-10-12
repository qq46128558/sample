#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用dir()'
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print('01.',dir('ABC'))
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，
print('02.','ABC'.__len__())
# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
# 剩下的都是普通属性或方法，比如lower()返回小写的字符串

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    # 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
    # 给实例绑定属性的方法是通过实例变量，或者通过self变量：
    def __init__(self):
        self.x=9
        self.__y='private' # _MyObject__y
    def power(self):
        return self.x*self.x
    # 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
    # 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
    name='MyObject'


obj=MyObject()
# print(dir(obj))
print('03.',hasattr(obj,'x')) # 有属性'x'吗？
print('04.',hasattr(obj,'y'))
# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# 可以传入一个default参数，如果属性不存在，就返回默认值：
print('05.',getattr(obj,'z',404))
print('06.',hasattr(obj,'z'))
# 也可以获得对象的方法
fn=getattr(obj,'power')
print('07.',fn())

# 只有在不知道对象信息的时候，我们才会去获取对象信息
def readImage(fp):
    if hasattr(fp,'read'):
        return readData(fp)
    return None
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

''' 类属性
>>> del obj.name # 如果删除实例的name属性
>>> print(obj.name) # 再次调用obj.name，由于实例的name属性没有找到，类的name属性就显示出来了
在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
Student '''