#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d={'Michael':95,'Bob':75,'Tracy':85,'Michael':100}
# 直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢
print(d['Michael'])
# 为什么dict查找速度这么快？
# dict就是给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('Thomas' in d)
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas',-1))
# 要删除一个key，用pop(key)方法
d.pop('Bob')
print(d)
# dict内部存放的顺序和key放入的顺序是没有关系的

''' 和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。 '''
# 需要牢记的第一条就是dict的key必须是不可变对象