#!/usr/bin/env python3

""" 福彩双色球信息数据分析 """

import logging
import pandas as pd
from numpy import NaN
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

logging.basicConfig(level=logging.INFO)

df=pd.read_csv('ssq_info.csv',encoding='gb18030')
# 排除2005-01-02之前的数据,因为没有中奖信息
df=df[(df["time"]>='2005-01-02')]

# logging.info(df['region'].isnull())
# 检测DataFrame的NaN值并替换为:无
df['region'][df['region'].isnull()]='无'

# 连接中奖地区字符串
text=",".join(df['region'])
# 将深圳替换为粤
text=text.replace("深圳",'粤')
# 去掉,
text=text.replace(",","")

# 使用jieba模块将字符串分割为单字列表 
# print(next(jieba.cut(text)))
cut_text=''.join(jieba.cut(text))
# print(cut_text)

# 将分词结果进行计数(传入字符串统计单字符,也可以传入tuple/list)
c=Counter(cut_text)
# df_region=pd.DataFrame(c,index=['中奖数量'])
# 挑选出字频top10
c=c.most_common(10)
logging.info(c)
logging.info(Counter(("深圳","深圳","粤")))
logging.info(Counter(["深圳","深圳","粤"]))
logging.info(Counter('深圳 深圳 粤'))

df_region=pd.DataFrame(data=c,columns=['region','quantity'])
# print(df_region)

# 显示matplotlibrc文件的地址
# print(matplotlib.matplotlib_fname())

# 修正中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'

if False:
    # 饼图数据
    plt.pie(df_region['quantity'],labels=df_region['region'],labeldistance=1.1,autopct='%2.1f%%')
    # 使饼图为正圆形 
    plt.axis('equal')
    # 图例
    plt.legend(loc='upper left',bbox_to_anchor=(-0.1,1))
    # 标题
    plt.title(u'双色球中奖率Top10')
    # 保存文件
    plt.savefig('pie_chart.jpg')
    # 弹窗显示
    plt.show()