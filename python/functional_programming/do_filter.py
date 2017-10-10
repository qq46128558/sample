#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(x):
    return x%2==1
o=filter(is_odd,range(1,16)) # 返回filter object filter()函数返回的是一个Iterator
print('01.',list(o))

# 把一个序列中的空字符串删掉，可以这么写
def not_empty(s):
    return s and s.strip()
o=filter(not_empty,['A', '', 'B', None, 'C', '  ']) # filter()函数返回的是一个Iterator
print('02.',list(o))


# prime_numbers.py 参考理解
# n是传入值, x是iterable的元素
def _not_divisible(n):
    return lambda x:print(n,x)
list(filter(_not_divisible(3),[1,4,7]))



