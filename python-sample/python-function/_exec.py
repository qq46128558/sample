#!/usr/bin/env python3

# exec()函数
# exec(object[, globals[, locals]])

import math

# 动态创建一个函数
# 必须使用正确的缩进，因为引用的代码是标准的 Python 代码
code = '''
def area_of_sphere(r):
    return 4 * math.pi * r ** 2
'''
context={}
context["math"] =  math
exec(code, context)
print(len(context)) 
# 3
# 执行上面的exec() 调用后，context 字典中将包含一个名为“area_of_shpere” 的键
print(context['area_of_sphere'](5))
# 314.1592653589793