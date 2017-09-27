#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 根据Python的缩进规则，如果if语句判断是True，就把缩进的语句执行了，否则，什么也不做。
age = 20
if age >= 18:
    print('Adult')
elif age >= 6:
    print('Teenager')
else:
    print('Kid')
# 注意不要少写了冒号:

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
if age:
    print(True)

''' 根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖 '''

heigh = input('Please input your height(m):')
weight = input('and input your weight(kg):')
bmi = float(weight) / (float(heigh)**2)
print('BMI值:%.2f' % bmi)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28 and bmi <= 32:
    print('肥胖')
elif bmi > 25 and bmi <= 28:
    print('过重')
elif bmi > 18.5 and bmi <= 25:
    print('正常')
else:
    print('过轻')
