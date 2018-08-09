#!/usr/bin/env python3

'python中is和==的区别'

import logging

logging.basicConfig(level=logging.INFO)


# python的变量像个便利贴，把他贴在哪个地方都可以，不需要管数据类型，只要你喜欢就可以
a=[1,2]
b=a
b.append(3)
logging.info(a)
# INFO:root:[1, 2, 3]
logging.info(a is b)
# INFO:root:True
logging.info(id(a))
logging.info(id(b))
# INFO:root:20155400

a=[1,2,3]
b=[1,2,3]
logging.info(a is b)
# INFO:root:False
logging.info(a==b)
# INFO:root:True
logging.info(id(a))
# INFO:root:20353608
logging.info(id(b))
# INFO:root:20354376

# python中有个intern机制,就是不管你创建了多少个相同的字符串，在python中都是会指向同一个对象的
a=1
b=1
logging.info(a is b)
# INFO:root:True
logging.info(a==b)
# INFO:root:True
logging.info(id(a))
logging.info(id(b))
# INFO:root:505610704

'''判断是否是同一个对象的时候就用is，不要用==，所以在判断该对象是什么类型的时候建议用is或者直接用isinstance()这个方法'''

# 类本身也是个对象，用type()方法会指向该对象
class Person():
	pass
p=Person()
logging.info(p is Person)
# INFO:root:False
logging.info(type(p) is Person)
# INFO:root:True


