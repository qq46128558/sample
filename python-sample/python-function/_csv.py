#!/usr/bin/env python3

""" csv操作 """

import csv
# encoding:gbk,gb18030,utf-8
with open('1.csv','w',encoding='gb18030',errors='ignore',newline='') as f:
    headers=['标题1','标题2','标题3','标题4']
    rows=[
        {'标题1':'1行值1','标题2':'1行值2','标题3':'1行值3','标题4':'1行值4'},
        {'标题1':'2行值1','标题2':'2行值2','标题3':'2行值3','标题4':'2行值4'}
    ]
    f_csv=csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
