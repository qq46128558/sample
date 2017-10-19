#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'定制类__getitem__'

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            # 如果n是切片对象, 需要处理一下
            for x in range(n):
                a,b=b,a+b
            return a
        # 但是没有对step参数作处理：
        # 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L

# 现在，就可以按下标访问数列的任意一项了：
f=Fib()
print(f[50]) # 循环到100后返回
print(f[0:5])

# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
''' 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。 '''

