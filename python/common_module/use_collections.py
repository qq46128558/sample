#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'collections'
# collections是Python内建的一个集合模块，提供了许多有用的集合类。

from collections import namedtuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
point=namedtuple('Point',['x','y'])
p=point(100,100)
print('01.',p.x,p.y)
# 可以验证创建的Point对象是tuple的一种子类：

from collections import deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q=deque(['a','b','c'])
q.append('d')
q.appendleft('e')
print('02.',q)
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

from collections import defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print('03.',dd['key2'])
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

from collections import OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
d=OrderedDict([('a',1),('y',3),('n',2)])
print('04.',d)

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdateOrderDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdateOrderDict,self).__init__()
        self._capacity=capacity

    def __setitem__(self,key,value):
        containKey=1 if key in self else 0
        if len(self)-containKey>=self._capacity:
            last=self.popitem(last=false)
            print('remove:',last)
        if containKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)

from collections import Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
c=Counter()
for i in 'programming':
    c[i]=c[i]+1
print('05.',c)

