#!/usr/bin/env python3

'位运算的应用'
# &	按位与运算符
# |	按位或运算符
# ^	按位异或运算符
# ~	按位取反运算符
# << 左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
# >> 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数

import logging

'应用一: 通过位运算表示状态的组合: 4只读 2可写 1执行'
def app1():
	r,w,x=4,2,1
	logging.info('r:{}/{} b:{}/{} c:{}/{}'.format(r,bin(r),w,bin(w),x,bin(x)))
	# INFO:root:r:4/0b100 b:2/0b10 c:1/0b1
	logging.info('r|w ={}/{}'.format(r|w,bin(r|w)))
	# INFO:root:r|w =6/0b110
	logging.info('w|x ={}/{}'.format(w|x,bin(w|x)))
	# INFO:root:w|x =3/0b11
	logging.info('r|w|x ={}/{}'.format(r|w|x,bin(r|w|x)))
	# INFO:root:r|w|x =7/0b111
	logging.info('r|w|w ={}/{}'.format(r|w|w,bin(r|w|w)))
	# INFO:root:r|w|w =6/0b110

'应用二: 现在有1000个瓶子，里面999瓶是水，1瓶是毒药。最少通过多少次的试验，能确定哪瓶是毒药。'
# 从000000001-1111111111，代表1号到1024号（1001-1024个瓶子可以忽视，因为只需要1000个），可以看到，每个数都有十位，那么我们让每只小白鼠负责一列，将这一列的编号出现1的瓶子中的液体混合着喝下去。如果某只小白鼠死了那么可以判定这列为1的所有瓶子中，有一瓶是毒药。通过十只小白鼠的生死情况组合来看，不难发现那瓶是毒药的瓶子编号。
def app2():
	pass

	
logging.basicConfig(level=logging.INFO)
# 按位运算符是把数字看作二进制来进行计算的
if __name__=='__main__':
	app1()
	

