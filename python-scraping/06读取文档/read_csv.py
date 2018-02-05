#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from io import StringIO

data=urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
dataFile=StringIO(data)
csvReader=csv.reader(dataFile)

for row in csvReader:
    print('The album "'+row[0]+'" was released in '+str(row[1]))


# csv.DictReader 会返回把 CSV 文件每一行转换成 Python 的字典对象返回，而不是列表对象
# dictReader=csv.DictReader(dataFile) # 为NONE
dictReader=csv.DictReader(StringIO(data))

# 并把字段列表保存在变量 dictReader.fieldnames 里
print("-------",dictReader.fieldnames,"-------")

for row in dictReader:
    print(row)  