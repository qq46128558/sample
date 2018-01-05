# -*- coding: utf-8 -*-

'''多线程示例2'''

import time,threading

def do_something():
    for i in range(3):
        time.sleep(1)
        print('线程',threading.current_thread().name,':',i)

if __name__=='__main__':
    start=time.time()
    threads=[]
    # 创建线程
    for i in range(3):
        threads.append(threading.Thread(target=do_something,name='T'+str(i)))
    # 启动线程
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end=time.time()
    # 四舍五入,截取小数位
    print('用时:',round(end-start,3),'s')
