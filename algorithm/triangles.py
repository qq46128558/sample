#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 杨辉三角的实现
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

def triangles():
    l=[1]
    yield l
    while True:
        # 用range取list的序号,通过序号取list的值
        l=[l[i]+l[i+1] for i in range(len(l)-1)]
        # 开始位置插入1
        l.insert(0,1)
        # 结束位置插入1
        l.insert(len(l),1)
        yield l

# 执行函数
f=triangles()
n=1
while True:
    print(next(f))
    n+=1
    if n>10:
        break