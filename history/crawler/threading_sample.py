# -*- coding: utf-8 -*-

'''
python网络爬虫入门（三）———多线程 
http://blog.csdn.net/Bo_wen_/article/details/50927688
报错:
Traceback (most recent call last):
  File "threading.py", line 22, in <module>
    t=threading.Thread(target=do_something,name=j)
AttributeError: module 'threading' has no attribute
'Thread'
Exception ignored in: <module 'threading' from 'D:\\Projects\\WWW\\sample\\crawler\\threading.py'>
AttributeError: module 'threading' has no attribute
'_shutdown'

解决:
.py文件名注意不能是threading.py
'''

import time
import threading


def do_something(threadName):
    for i in range(3):
        time.sleep(1)
        print('线程',threadName,':',i)

class Mythread(threading.Thread):
    def __init__(self,threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    # run()方法
    # 代表了线程活动的方法。
    # 你可以在子类中重写此方法。标准run()方法调用了传递给对象的构造函数的可调对象作为目标参数，如果有这样的参数的话，顺序和关键字参数分别从args和kargs取得。
    def run(self):
        do_something(self.threadName)

if __name__=='__main__':
    thread=[]
    start=time.time()
    for j in range(3):
        # 创建线程
        t=Mythread(j)
        thread.append(t)

    # 启动线程
    for t in thread:
        t.start()
    # 主线程等待子线程
    for t in thread:
        t.join()
    
    end=time.time()
    print('运行时间:',end-start,"s")