#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'分布式进程'
import time,sys,queue
from multiprocessing.managers import BaseManager
# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass
# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 连接到服务器，也就是运行task_master.py的机器:
server_addr='127.0.0.1'
print('Connect to server %s...'%server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m=QueueManager(address=(server_addr,5000),authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task=m.get_task_queue()
result=m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n=task.get(timeout=1)
        print('run task %d * %d...'%(n,n))
        r='%d * %d=%d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')

# 任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。

# 现在，可以试试分布式进程的工作效果了。先启动task_master.py服务进程

# 这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。

# Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中：

# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。

# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。