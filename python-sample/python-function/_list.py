#/usr/bin/env python3

'list应用'

import logging

logging.basicConfig(level=logging.INFO)

# 多个list合并为一个
# 使用+号: 运算符的重载
l1=[1,2,3]
l2=[4,5,6]
logging.info(l1+l2)
# INFO:root:[1, 2, 3, 4, 5, 6]
# 使用extend方法: 比较简洁，但会覆盖原始list
l3=[7,8,9]
l3.extend(l1)
logging.info(l3)
# INFO:root:[7, 8, 9, 1, 2, 3]
# 使用切片: 功能比较强大，可以将一个列表插入另一个列表的任意位置
# 加到尾部
l1[len(l1):]=l2
logging.info(l1)
# INFO:root:[1, 2, 3, 4, 5, 6]
# 加到头部
l4=[1,2,3]
l4[:0]=l2
logging.info(l4)
# INFO:root:[4, 5, 6, 1, 2, 3]

