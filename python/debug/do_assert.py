#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'调试'
''' 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看 '''
# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。
''' 第二种方法,断言 '''
''' 把print()替换为logging是第三种方式，和assert比，logging不会抛出错误，而且可以输出到文件： '''
def foo(s):
    n=int(s)
    # assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    # 如果断言失败，assert语句本身就会抛出AssertionError：
    assert n!=0,'n is zero!'
    # 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O(大写字母)参数来关闭assert：
    # 关闭后，你可以把所有的assert语句当成pass来看。
    return 10/n
def main():
    foo('0')

main()