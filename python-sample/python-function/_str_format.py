#!/usr/bin/env python3

'''python字符串格式化 {}操作符'''
# https://www.cnblogs.com/zyq-blog/p/5946905.html

__author__='Peter'

# 通过位置映射
print('my value:{},{}'.format('abc',123))
print('my value:{1},{0}'.format(123,'abc'))

# 通过关键字参数映射
print('my value:{value1},{value2}'.format(value1='abc',value2=123))

# 通过对象属性映射
class Person:
    def __init__(self,value1,value2):
        self.value1,self.value2=value1,value2
        print('my value:{self.value1},{self.value2}'.format(self=self))
        
Person('abc',123)
# 通过下标映射
p=['abc',123]
print('my value:{0[0]},{0[1]}'.format(p))
# my value:abc,123

# 填充常跟对齐一起使用
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面可带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print('my value:{:>10},{}'.format('abc',123))
# my value:       abc,123

# 格式限定符 它有着丰富的的“格式限定符”（语法是{}中带:号)
print('my value:{:>10},{:7.2f}'.format('abc',123))
# my value:       abc, 123.00
# 2进制,10进制,8进制,16进制,千位分隔符
print('my value:{:>10},{:b}'.format('abc',123))
print('my value:{:>10},{:d}'.format('abc',123))
print('my value:{:>10},{:o}'.format('abc',123))
print('my value:{:>10},{:x}'.format('abc',123))
print('my value:{:>10},{:,}'.format('abc',123123))
# my value:       abc,1111011
# my value:       abc,123
# my value:       abc,173
# my value:       abc,7b
# my value:       abc,123,123

