#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MapReduce: Simplified Data Processing on Large Clusters
# http://research.google.com/archive/mapreduce.html


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x**2
r=map(f,range(1,10)) # 返回的是iterator
print('01.',list(r)) # Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x,y):
    return x*10+y
# 传入函数,序列
r=reduce(add,[x for x in range(1,10) if x%2!=0])
print('02.',r)

# map+reduce结合,编写一个字符串转整数的函数
def str2int(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def fn(x,y):
        return x*10+y
    return reduce(fn,map(char2num,s))
print('03.',str2int('08001'))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper()+name[1:].lower()
l=['adam','LISA','barT']
print('04.',list(map(normalize,l)))

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(x,y):
    return x*y
print('05.',reduce(prod,[x for x in range(3,10) if x%2!=0]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# 我的原始版
def str2float1(s):
    def char2num(s):
        if s=='.':
            return
        else:
            return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def fn(x,y):
        if y==None:
            return x
        else:
            return x*10+y
    f=reduce(fn,map(char2num,s))
    # 查找小数点位置, 再除以10的n次方, 得出小数
    f=f/(10**(len(s)-s.find('.')-1))
    print('06.',f)
str2float1('0123.456')

# 改进版
def str2float(s):
    point=0
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}[s]
    def fn(x,y):
        nonlocal point
        if y==-1:
            point=1
            return x
        elif point==0:
            return x*10+y
        else:
            point*=10
            return x+y/point
            
    f=reduce(fn,map(char2num,s))
    return f
print('07.',str2float('0123.4567'))

