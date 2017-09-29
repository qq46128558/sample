#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
l=list(range(1,11))
print('01.',l)

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做
# 列表生成式可以用一行语句生成上面的list
l=[x*x for x in range(1,11)]
print('02.',l)
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
l=[x*x for x in range(1,11) if x%2==0]
print('03.',l)

# 还可以使用两层循环，可以生成全排列：
l=[m+n for m in 'ABC' for n in '123']
print('04.',l)
# 三层和三层以上的循环就很少用到了

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
l=[d for d in os.listdir('.')]
print('05.',l)

# 列表生成式也可以使用两个变量来生成list：
d={'x':'A','y':'B','z':'C'}
l=[k+'='+v for k,v in d.items()]
print('06.',l)

# 把一个list中所有的字符串变成大写
l=['hello','world','ibm','apple']
l=[s.upper() for s in l]
print('07.',l)

l=['welcome','back',18,'kate',None]
l=[s.upper() for s in l if isinstance(s,str)]
print('08.',l)