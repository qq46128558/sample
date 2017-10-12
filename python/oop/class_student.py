#!/usr/bin/env python3
# -*= coding: utf-8 -*-

'class sample'
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s: %s'%(self.name,self.score))


bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。