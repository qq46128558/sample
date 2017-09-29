#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
d = {"a": 1, "b": 2, "c": 3}
for k, v in d.items():
    print('01.',k, v)
# 由于字符串也是可迭代对象，因此，也可以作用于for循环

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print('02.',isinstance('abc',Iterable))
print('03.',isinstance(123,Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
l=['A','B','C']
for i,value in enumerate(l):
    print('04.',i,value)

# for循环里，同时引用了两个变量，在Python里是很常见的
l=[(1,1),(2,4),(3,9)]
for x,y in l:
    print('05.',x,y)

from collections import Iterator
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
print('06.',isinstance([],Iterator))
print('07.',isinstance({},Iterator))
print('08.',isinstance((x for x in range(3)),Iterator))
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print('09.',isinstance(iter('abc'),Iterator))

''' 你可能会问，为什么list、dict、str等数据类型不是Iterator？
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。 '''
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

''' 凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的 '''
for x in [1,2,3,4,5]:
    pass

it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
    except StopIteration:
        break