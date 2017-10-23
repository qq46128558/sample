#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'单元测试'
# 这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。
# 我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'"%key)
    def __setattr__(self,key,value):
        self[key]=value

