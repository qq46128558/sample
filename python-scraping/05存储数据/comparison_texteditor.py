#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'获取 HTML 表格并写入 CSV 文件'

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj=BeautifulSoup(html,'html.parser')
# 主对比表格是当前页面上的第一个表格
table=bsObj.findAll('table',{"class":"wikitable"})[0]
rows=table.findAll("tr")
# wt模式下，Python写文件时会用\r\n来表示换行
with open("comparison_texteditor.csv","wt",newline='',encoding='utf-8') as f:
    writer=csv.writer(f)
    try:
        for row in rows:
            csvRow=[]
            for cell in row.findAll(['td','th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
    except Exception as e:
        print(e)



