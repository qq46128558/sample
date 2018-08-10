#!/usr/bin/env python3

'进程池示例2'
'如果要启动大量的子进程，可以用进程池的方式批量创建子进程'
'多线程'


import logging
import time
import os
from multiprocessing import Pool

logging.basicConfig(level=logging.INFO)
# 全局变量
# 如果多个线程同时对同一个全局变量操作，会出现资源竞争问题
Code='ABC'

def multi_processing(i,name):
	# global Code
	# print('Processing {}'.format(i))
	logging.info('Begin processing:{},Pid:{} PPid:{}'.format(i,os.getpid(),os.getppid()))
	time.sleep(1)
	logging.info('End processing:{} Global:{} Name:{}'.format(i,Code,name))

# 需要加这一句, 否则报错:
'''RuntimeError:
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.'''
if __name__=='__main__':
	# 子进程数(线程数)(一般输入CPU核数)
	p=Pool(4)
	for i in range(5):
		p.apply_async(multi_processing,args=(i,chr(97+i)))
	logging.info('Wait for all subprocesses done...')
	p.close()
	# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
	p.join()
	logging.info('All subprocesses done.')

# 遗留问题:
# 如何获取方法的返回值?