#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'多重继承'

# 首先，主要的类层次仍按照哺乳类和鸟类设计
class Animal(object):
    pass
# 大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass

# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')
class RunnableMixIn(object):
    def run(self):
        print('Running...')


# 各种动物
# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
class Parrot(Bird,Flyable):
    pass
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：
class Ostrich(Bird,RunnableMixIn):
    pass
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

# Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
# 比如，编写一个多进程模式的TCP服务，定义如下：
''' class MyTCPServer(TCPServer,ForkingMixIn):
    pass '''
# 编写一个多线程模式的UDP服务，定义如下：
''' class MyUDPServer(UDPServer,ThreadingMixIn):
    pass '''
# 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
''' class MyTCPServer(TCPServer, CoroutineMixIn):
    pass '''
# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。


