#!/usr/bin/env python3

'''python字符串格式化 %操作符'''
# https://www.cnblogs.com/zyq-blog/p/5946905.html

__author__='Peter'


# %s    字符串 (采用str()的显示)
print("first value:%s,second value:%s" % ('abc',123))
# first value:abc,second value:123

# 用dict传值
print("first value:%(fv)s,secord value:%(sv)s" % {'fv':123,'sv':'abc'})
# first value:123,secord value:abc

# %r    字符串 (采用repr()的显示)
print("my value:%r" % 'abc')
# my value:'abc'

# %c    单个字符
print("my value:%c" % 65)
# my value:A

# %d/%i    十进制整数
print("my value:%d" % 10)
# my value:10

# %o    八进制整数(传入10进制，返回8进制)
print("my value:%o" % 8)
# my value:10

# %x    十六进制整数(传入10进制，返回16进制)
print("my value:%x" % 16)
# my value:10

# %e/%E    指数 (基底写为e/E)
print("my value:%e" % 10000)
# my value:1.000000e+04

# %f/%F    浮点数
print("my value:%f" % (10/3))
# my value:3.333333
# %g/%G    指数(e)或浮点数 (根据显示长度)

# 格式控制
# %[(name)][flags][width].[precision]typecode
# (name)为命名
# flags可以有+,-,' '或0。+表示右对齐(默认)。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充
# width表示显示宽度
# precision表示小数点后精度

print("my value:% 10x" % 10)
# my value:         a
print("my value:%04d" % 5)
# my value:0005
print("my value:%10.3f" % 2.3)
# my value:     2.300

# 使用*动态带入量
print("my value:%*.3f" % (10,2.3))
# my value:     2.300
