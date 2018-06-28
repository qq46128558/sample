#!/usr/bin/env python3

# 创建生成器表达式
# (expression for item in iterable)
# (expression for item in iterable if condition)
# yield语句也可以生成generator

print(type(x*x for x in range(1,4)))
# <class 'generator'>
print((x*x for x in range(1,4)))
# <generator object <genexpr> at 0x0000000000A36D00>
print([x*x for x in range(1,4)])
# [1, 4, 9]
generator=(x*x for x in range(1,4))
while True:
    try:
        print(next(generator))
    except StopIteration:
        break
    else:
        pass
# 1
# 4
# 9
print([x*x for x in range(1,10) if x%2==0])
# [4, 16, 36, 64]
