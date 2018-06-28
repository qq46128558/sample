#!/usr/bin/env python3

""" eval()函数 """
# eval(expression, globals=None, locals=None)
# globals 和 locals参数是可选的，如果提供了globals参数，那么它必须是dictionary类型；如果提供了locals参数，那么它可以是任意的map对象

# 动态代码的执行
print(eval('(2**8)-1'))
# 255


