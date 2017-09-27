#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# range(101)就可以生成0-100的整数序列
sum = 0
for x in range(101):
    sum += x
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
# 比如我们要计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

# 在循环中，break语句可以提前退出循环
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
# 只打印奇数
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# 有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
