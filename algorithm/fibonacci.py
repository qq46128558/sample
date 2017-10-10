#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
    n,a,b=0,0,1
    while n<max:
        n+=1
        yield b
        a,b=b,a+b
    return 'Done'

for x in fib(10):
    print(x)