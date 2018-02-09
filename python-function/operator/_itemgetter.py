'用于获取对象的哪些维的数据，参数为一些序号'

import operator

a=[1,2,3]
# 定义函数b，获取对象的第1个域的值
b=operator.itemgetter(1)
print(b(a))
# 2

# 定义函数b，获取对象的第1个域和第0个的值
b=operator.itemgetter(1,0)
print(b(a))
# (2, 1)