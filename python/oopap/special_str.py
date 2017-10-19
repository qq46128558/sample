#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'定制类__str__'

class Student(object):
    def __init__(self,name):
        self.name=name

    # <__main__.Student object at 0x00000000007C5B00>
    # 定义好__str__()方法，可以返回一个好看的字符串
    def __str__(self):
        return 'Student object (name: %s)'%self.name
    # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    __repr__=__str__
    
print('01.',Student('Michael'))