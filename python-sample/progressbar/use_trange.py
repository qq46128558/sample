#!/usr/bin/env python3
# encoding: utf-8

""" 多线程进度条 """

from time import sleep
from tqdm import tqdm,trange
from multiprocessing import Pool,freeze_support,RLock
import sys

# [0, 1, 2, 3, 4, 5, 6, 7, 8]
L=list(range(9))

def progresser(n):
    interval=0.001/(n+2)
    total=5000
    #0,est.2.50s: 100%|██████████| 5000/5000 [00:08<00:00, 568.72it/s]
    # str.format()
    # :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
    # ^、<、>分别是居中、左对齐、右对齐，后面带宽度
    # .2表示长度为2的精度
    text="#{},est.{:<04.2}s".format(n,interval*total)
    # position应该是间隔输出
    for i in trange(total,desc=text,position=1):
        sleep(interval)

if __name__=='__main__':
    freeze_support() # for windows support
    p=Pool(len(L),
    # again, for windows support
    initializer=tqdm.set_lock,initargs=(RLock(),)
    )
    p.map(progresser,L)