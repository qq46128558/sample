#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'错误处理'
# 高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外
try:
    print('try...')
    # r=10/0
    r=10/int('a')
    print('result:',r)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
# 错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：
except ValueError as e:
    print('ValueError:',e)
# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
else:
    print('no error!')
finally:
    print('finally...')
print('END')
# finally如果有，则一定会被执行（可以没有finally语句）

# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
# UnicodeError是ValueError的子类
# 常见的错误类型和继承关系看这里：
''' https://docs.python.org/3/library/exceptions.html#exception-hierarchy '''
# 不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。

