'''
用于获取对象的哪些维的数据，参数为一些序号
operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。
'''

import operator

a=[1,2,3]
# 定义函数b，获取对象的第1个域的值
get_1=operator.itemgetter(1)
print(get_1(a))
# 2

# 定义函数b，获取对象的第1个域和第0个的值
get_1_0=operator.itemgetter(1,0)
print(get_1_0(a))
# (2, 1)

a2=[(1,2),(4,5),(7,8)]
b=operator.itemgetter(0)
print(b(a2))
# (1, 2)

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# sorted函数用来排序，sorted(iterable[, cmp[, key[, reverse]]])
# 根据第二个域和第三个域进行排序
result=sorted(students,key=operator.itemgetter(1,2))
print(result)
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]