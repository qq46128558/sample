#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：
# http://docs.python.org/3/library/functions.html#abs
# 也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
# max函数max()可以接收任意多个参数，并返回最大的那个
print('01.',max(10,3,9,7))
# Python内置的常用函数还包括数据类型转换函数
print('02.',int('123'))
print('03.',float(123))
print('04.',str(1.23))
print('05.',bool(1))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a=abs
print('06.',a(-1))

