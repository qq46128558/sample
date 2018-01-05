# -*- coding: utf-8 -*-
'''
Python中Thread类的start()和run()方法的区别
http://blog.csdn.net/chenpkai/article/details/70943609
start()方法
开始线程活动。
对每一个线程对象来说它只能被调用一次，它安排对象在一个另外的单独线程中调用run()方法（而非当前所处线程）。
当该方法在同一个线程对象中被调用超过一次时，会引入RuntimeError(运行时错误)。
run()方法
代表了线程活动的方法。
你可以在子类中重写此方法。标准run()方法调用了传递给对象的构造函数的可调对象作为目标参数，如果有这样的参数的话，顺序和关键字参数分别从args和kargs取得。
'''

import threading

class Mythread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threading
        self.name=name
        self.counter=counter
    
    def run(self):
        currentThreadName=threading.currentThread()
        # print('Running in',currentThreadName,self.threadID,self.name,self.counter)
        print('Running in',currentThreadName)
    
if __name__=='__main__':
    t=Mythread(1,'mythrd',1)
    # Running in <_MainThread(MainThread, started 13448)>
    t.run()
    # Running in <Mythread(mythrd, started 11268)>
    t.start()


# 线程的概念：线程的起动并不是简单的调用了RUN方法,而是由一个线程调度器来分别调用所有线程的RUN方法

# 我们普通的RUN方法如果没有执行完是不会返回的,也就是会一直执行下去,这样RUN方法下面的方法就不可能会执行了,可是线程里的RUN方法却不一样,它只有一定的CPU时间,执行过后就给别的线程了,这样反复的把CPU的时间切来切去,因为切换的速度很快,所以我们就感觉是很多线程在同时运行一样.

''' 简单的调用run方法是没有这样效果的,所以必须调用Thread类的start方法来启动线程. '''
# 所以启动线程有两种方法
# 一是写一个类继承自Thread类,然后重写里面的run方法,用start方法启动线程
# 二是写一个类实现Runnable接口,实现里面的run方法,用new Thread(Runnable target).start()方法来启动

# 这两种方法都必须实现RUN方法,这样线程起动的时候,线程管理器好去调用RUN方法.