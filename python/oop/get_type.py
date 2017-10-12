#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'获取对象信息'
# 基本类型都可以用type()判断
print('01.',type('ABC'))
print('02.',type(123))
print('03.',type(None))
print('04.',type(True))
print('05.',type(abs))
# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print('06.',type('ABC')==str)
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types
def fn():
    pass
print('07.',type(fn)==types.FunctionType)
print('08.',type(abs)==types.BuiltinFunctionType)
print('09.',type(lambda x:x)==types.LambdaType)
print('10.',type(x for x in range(10))==types.GeneratorType)

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 能用type()判断的基本类型也可以用isinstance()判断：
print('11.',isinstance(b'a',bytes))
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print('12.',isinstance([1,],(list,tuple)))
print('13.',isinstance((1,),(list,tuple)))
