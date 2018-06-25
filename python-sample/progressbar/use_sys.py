#!/usr/bin/env python3

import sys
import time

""" 标准输出中添加进度条 """


def progress_bar(total):
    # 获取标准输出
    _output=sys.stdout
    # 通过参数决定你的进度条总量是多少
    for count in range(total+1):
        # 这里的second只是作为工作量的一种代替
        # 这里应该是有你的主程序,main()
        _second=0.01
        # 模拟业务的消耗时间
        time.sleep(_second)
        # 输出进度条
        # \r： 将光标移动到当前行的首位而不换行；
        # \n：将光标移动到下一行，并不移动到首位；
        # \r\n：将光标移动到下一行首位
        _output.write(f'\rcomplete percent:{count:.0f}%')
        # 将标准输出一次性刷新
        _output.flush()

if __name__=='__main__':
    progress_bar(100)