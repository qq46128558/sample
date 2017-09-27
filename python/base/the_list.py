#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmate = ['Michael', 'Bob', 'Tracy']
print('01.', classmate)
print('02.', len(classmate))
print('03.', classmate[1])
# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1
# 还可以用-1做索引，直接获取最后一个元素
print('04.', classmate[-1])
# 以此类推，可以获取倒数第2个、倒数第3个：-2,-3, 当然，倒数第4个就越界了。
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
print('05.', classmate.append('Adam'))
print('06.', classmate[-1])
# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmate.insert(0, 'Jack')
print('07.', classmate)
# 要删除list末尾的元素，用pop()方法：
classmate.pop()
print('08.', classmate)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmate.pop(0)
print('09.', classmate)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmate[0] = 'Sarah'
print('10.', classmate)
# list里面的元素的数据类型也可以不同
classmate.append(123)
# list元素也可以是另一个list,可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到
classmate.append([True, 3.14, 'ABC'])
print('11.', classmate)
print('12.', len(classmate))
print('13.', classmate[-1][0])
