#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'pdb'
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb
import pdb

# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
s='0'
n=int(s)
# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
# 这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。
pdb.set_trace() # 运行到这里会自动暂停
print(10/n)

# 以参数-m pdb启动后，pdb定位到下一步要执行的代码
# python -m pdb do_pdb.py
# 输入命令l来查看代码
# 输入命令n可以单步执行代码
# 任何时候都可以输入命令p 变量名来查看变量
# 输入命令q结束调试，退出程序
# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法 pdb.set_trace() 

# IDE
# 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm：
# http://www.jetbrains.com/pycharm/
# 另外，Eclipse加上pydev插件也可以调试Python程序。
# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。