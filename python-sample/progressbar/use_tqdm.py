#!/usr/bin/env python3

"""使用 Tqdm 模块来实现进度条"""
# https://github.com/tqdm/tqdm。

from time import sleep
from tqdm import tqdm

# 这里同样的，tqdm就是这个进度条最常用的一个方法
# 里面存一个可迭代对象

if __name__=='__main__':
    for i in tqdm(range(500)):
        # 模拟你的任务
        sleep(0.01)



