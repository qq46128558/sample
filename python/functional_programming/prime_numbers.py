#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 用filter求素数
''' 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
不断筛下去，就可以得到所有的素数。
用Python来实现这个算法，可以先构造一个从3开始的奇数序列： '''
# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
# 注意这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n=1
    while True:
        n+=2
        yield n
# 定义一个筛选函数, 用n把序列的n的倍数筛掉
# lambda作为一个表达式，定义了一个匿名函数, x为入口参数, 返回x%n>0的结果
# lambda 是为了减少单行函数的定义而存在的
# n为传入值, x为iterable元素
def _not_divisible(n):
    return lambda x:x%n>0
# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it=_odd_iter() # 初始序列
    while True:
        n=next(it) # 返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it) # 构造新序列 用n把序列的n的倍数筛掉
# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# 打印条件判断数以内的素数:
def main():
    for x in primes():
        if x<20:
            print(x)
        else:
            break
# 注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁

if __name__=='__main__':
    main()