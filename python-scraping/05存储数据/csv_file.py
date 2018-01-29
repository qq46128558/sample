#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Python 的 csv 库可以非常简单地修改 CSV 文件'

import csv
# Python 会自动创建文件（不会自动创建文件夹）。如果文件已经存在，Python 会用新的数据覆盖 test.csv 文件
# newline=''不会出现空行
# w+ 打开可读写文件，若文件存在则文件长度清为零，即该文件内容会消失。若文件不存在则建立该文件
csvFile=open("test.csv","w+",newline='')
try:
    writer=csv.writer(csvFile)
    writer.writerow(('number','number plus 2','number times 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()

