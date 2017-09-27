#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmate = ('Michael', 'Bob', 'Tracy')
print('01.', classmate)
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1)
print('02.', t)
t = (1,)
print('03.', t)
# 可变的tuple: 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素
t = ('a', 'b', ['A', 'B'])
t[-1][0] = 'x'
t[-1][1] = 'y'
print('04.', t)
