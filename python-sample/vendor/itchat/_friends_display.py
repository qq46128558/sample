#!/usr/bin/env python3

'分析微信好友信息'

import logging
import pandas as pd

# 计数用的库
import collections
# 画饼图用的库
import matplotlib.pyplot as plt
# 解决图片中文乱码
from matplotlib.font_manager import FontProperties
# 画地图用的库
from pyecharts import Map
from pyecharts import Geo

logging.basicConfig(level=logging.INFO)

# 全球国家地图: echarts-countries-pypkg (1.9MB): 世界地图和 213 个国家，包括中国地图
# pip install echarts-countries-pypkg    
# 中国省级地图: echarts-china-provinces-pypkg (730KB)：23 个省，5 个自治区
# pip install echarts-china-provinces-pypkg 
# 中国市级地图: echarts-china-cities-pypkg (3.8MB)：370 个中国城市
# pip install echarts-china-cities-pypkg  
# 中国县区级地图: echarts-china-counties-pypkg (4.1MB)：2882 个中国县·区
# pip install echarts-china-counties-pypkg 
# 中国区域地图: echarts-china-misc-pypkg (148KB)：11 个中国区域地图，比如华南、华北
# pip install echarts-china-misc-pypkg   

# 获取当前微信好友信息(已在_friends_get.py中获取过)
df=pd.read_csv('friends.csv',encoding='utf_8_sig')

df_sex=df.Sex.value_counts()
logging.info(df_sex.sort_index().values)

# 微信中性别字段的取值有Unkonw、Male和Female三种，其对应的数值分别为0、1、2。
# 设置绘图对象的大小
plt.figure(figsize=(8,8))
# 参数设置这个饼为正圆
plt.axes(aspect=1)
plt.pie(
	df_sex.sort_index().values, 	# 性别统计结果
	labels=['未知','男','女'],		# 设置饼图的标签
	colors=['red','blue','coral'],	# 饼图区域配色
	explode=[0,0,0.1],				# 凸出部分 0.1 凸出这部分，female
	labeldistance=1.1,				# 标签距离圆点距离，1.1指1.1倍半径的位置
	autopct='%3.1f%%',				# 饼图区域文本格式,%3.1f%%表示小数有三位，整数有一位的浮点数
	shadow=False,					# 饼图是否显示阴影
	startangle=90,			# 起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
	pctdistance=0.6,		# 饼图区域文本距离圆点距离
	)
# 解决 Windows 环境下乱码问题
# font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15) 
# plt.title(u'微信好友性别比例', fontproperties=font_set)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.title(u'微信好友性别比例')
plt.savefig('friends_pie.jpg')
plt.show()
