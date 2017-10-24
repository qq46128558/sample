#!/usr/env/bin python3
# -*- coding: utf-8 -*-
'操作文件和目录'
# 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

# 打开Python交互式命令行，我们来看看如何使用os模块的基本功能：
import os
print('01.',os.name) # 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# 要获取详细的系统信息，可以调用uname()函数：
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
# print('02.',os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print('02.',os.environ.get('sessionname'))

# 查看当前目录的绝对路径:
print('03.',os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('/Users/michael', 'testdir')
print('04.',os.path.join(r'd:\projects\www\sample\python\io','testdir'))
# 然后创建一个目录:
# os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
# os.rmdir('/Users/michael/testdir')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print('04.',os.path.split(r'd:\projects\www\sample\python\io\myfile.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print('05.',os.path.splitext(r'd:\projects\www\sample\python\io\myfile.txt'))
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。


# 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# 删掉文件:
# >>> os.remove('test.py')

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print('06.',[x for x in os.listdir('.') if os.path.isdir(x)])

# 要列出所有的.py文件，也只需一行代码：
print('07.',[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。

''' 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。 '''
import os
def search(path,condition):
    L=[]
    for x,y,z in os.walk(path): # x 路径, y 目录 z 文件
       L=L+[os.path.join(x,z[i]) for i in range(len(z)) if condition in z[i]] # 查找文件
    if L:
        # print(L)
        pass
    else:
        print('None')
    for file in L:
        # print(os.path.relpath(file,path))
        print(file)

search('..\io','do')
