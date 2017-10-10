#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置的sorted()函数就可以对list进行排序：
L=[36,5,-12,9,-21]
print('01.',sorted(L))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print('02.',sorted(L,key=abs))
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
N=['bob','about','Zoo','Credit']
print('03.',sorted(N))
# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
print('04.',sorted(N,key=str.upper))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print('05.',sorted(N,key=str.upper,reverse=True))
# 从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

# 假设我们用一组tuple表示学生名字和成绩：
T=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
# 用sorted()对上述列表分别按名字排序：
print('06.',sorted(T,key=lambda x:x[0]))
# 再按成绩从高到低排序：
print('07.',sorted(T,key=lambda x:x[1],reverse=True))

# 教程源码用这个:
from operator import itemgetter
print('08.',sorted(T,key=itemgetter(0)))
print('09.',sorted(T,key=itemgetter(1),reverse=True))


