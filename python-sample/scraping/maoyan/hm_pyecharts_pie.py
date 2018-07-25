#!/usr/bin/env python3

'pyecharts 饼图'

import logging
import pandas as pd
from pyecharts import ThemeRiver
from pyecharts import Pie

logging.basicConfig(level=logging.ERROR)

df=pd.read_csv('hidden_man_norepeat.csv',encoding='gb18030')
series=df['评分'].value_counts()

logging.info(df['评分'].value_counts())

dict = {"五星":0, "四星":0, "三星":0, "二星":0, "一星":0}
# logging.info(dir(series))
logging.info(series.to_dict())

# python无switch语句,官方说用if else
def switch(key):
    return {
        '5.0':'五星',
        '4.5':'五星',
        '4.0':'四星',
        '3.5':'四星',
        '3.0':'三星',
        '2.5':'三星',
        '2.0':'二星',
        '1.5':'二星',
        '1.0':'一星',
        '0.5':'一星',
    }.get(key)

# 将分值用switch分成星级
for k,v in series.to_dict().items():
    dict[switch(str(k))]+=v


logging.info(dict)

pie=Pie("饼图-星级玫瑰图示例",title_pos="center",width=1440-15,height=767-16)
pie.add("7-17",list(dict.keys()),list(dict.values()),center=[75,50],is_random=True,radius=[30,75],rosetype='area',is_legend_show=False,is_label_show=True)
pie.render('pie.html')
