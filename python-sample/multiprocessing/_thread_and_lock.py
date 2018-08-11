#!/usr/bin/env python3

'多线程'
# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核
'Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。'

import logging
import time,threading


# 多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了,所以需要用Lock()
lock=threading.Lock()
logging.basicConfig(level=logging.INFO)
items=[]

def scraping(i):
	global items
	value=str(i)+":"+chr(i+96)
	logging.info(value)
	items.append(value)
	# 加个sleep(1),不然太快看不出
	time.sleep(1)

def run_thread(ctrl):
	for i in [j*2-ctrl for j in range(1,51)]:
		# 先要获取锁:
		lock.acquire()
		logging.info("Scraping page: {}".format(i))
		try:
			scraping(i)
		finally:
			# 改完了一定要释放锁:
			lock.release()

if __name__=='__main__':
	# 抓取奇数页
	t1=threading.Thread(target=run_thread,args=(1,))
	# 抓取偶数页
	t2=threading.Thread(target=run_thread,args=(0,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	logging.info(items)
