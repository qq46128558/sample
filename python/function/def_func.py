#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
# return None可以简写为return
from abstest import my_abs
print('01.', my_abs(-100))
# import的用法在后续模块一节中会详细介绍。

# 如果想定义一个什么事也不做的空函数，可以用pass语句：


def nop():
    pass
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。


# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
import math
# 返回多个值


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 同时获得返回值
x, y = move(100, 100, 60, math.pi / 6)
print('02.', x, y)

# 但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print('03.', r)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0 的两个解。
# 解:(-b+/-delta开根)/2a
# delta=2b-4ac
def quadratic(a,b,c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
        raise TypeError('Bad operand type.')
    delta=b*b-4*a*c
    if delta>=0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return x1,x2
    else:
        return

print('04.',quadratic(2,3,1))
print('05.',quadratic(1,3,-4))