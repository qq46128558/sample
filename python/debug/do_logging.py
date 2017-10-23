#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'logging'

''' 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件： '''
import logging
# 指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging.basicConfig(level=logging.INFO)
s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
