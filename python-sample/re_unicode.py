#!/usr/bin/env python3

""" 正则剔除标点符号 """

import re

str='那是一个秋天，风儿那么缠绵。'
strdata=re.findall(r'[\u4E00-\u9FD5]+',str)

# 中文字的unicode范围
# print('\u4E00')
# print('\u9FD5')

print(str)
print(strdata)
print(''.join(strdata))

