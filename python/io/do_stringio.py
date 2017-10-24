#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'StringIO'
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
# getvalue()方法用于获得写入后的str。
print('01.',f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f=StringIO('Welcome\nBack\nGoodbye.')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())
