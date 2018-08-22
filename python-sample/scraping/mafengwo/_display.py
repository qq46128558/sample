#!/usr/bin/env python3

'马蜂窝城市信息图表展现'

import logging
# import matplotlib.pyplot as plt
import pandas as pd
from pyecharts import Bar
from pyecharts import Grid

logging.basicConfig(level=logging.INFO)

# # 修正中文乱码问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['font.family']='sans-serif'

# 读取数据
df_yj=pd.read_csv('city_yj.csv',encoding='gb18030')
df_yj1=df_yj.sort_values(by="餐饮游记",ascending=False)[0:15]
df_yj2=df_yj.sort_values(by="景点游记",ascending=False)[0:15]
df_yj3=df_yj.sort_values(by="购物游记",ascending=False)[0:15]
df_yj4=df_yj.sort_values(by="娱乐游记",ascending=False)[0:15]
logging.info(df_yj1)

# 柱状图
bar1=Bar('餐饮类标签排名',title_top="1%") #递增25%
bar2=Bar('景点类标签排名',title_top="26%")
bar3=Bar('购物类标签排名',title_top="51%")
bar4=Bar('娱乐类标签排名',title_top="76%") 
# is_splitline_show 水平标线 xaxis_rotate 未知 legend_top 图例离页面顶部距离
bar1.add('餐饮游记',df_yj1['城市'],df_yj1['餐饮游记'],is_splitline_show=True,xaxis_rotate=30,legend_top="1%")
bar2.add('景点游记',df_yj2['城市'],df_yj2['景点游记'],is_splitline_show=True,xaxis_rotate=30,legend_top="26%")
bar3.add('购物游记',df_yj3['城市'],df_yj3['购物游记'],is_splitline_show=True,xaxis_rotate=30,legend_top="51%")
bar4.add('娱乐游记',df_yj4['城市'],df_yj4['娱乐游记'],is_splitline_show=True,xaxis_rotate=30,legend_top="76%")

grid = Grid(height=800)
# grid_bottom 图表底部离页面底部距离 grid_top 图表顶部离页面顶部距离
'''100%-(grid_bottom:80 + grid_top 5)=15%即为柱状图高的占比, 即4个图占60%空间,并留一些白''' 
'''先填出第一个图(80,5)与最后一个图(5,80)的位置, 然后用(80-5)/(4-1)=25为增量间距'''
grid.add(bar1,grid_bottom="80%",grid_top="5%")
grid.add(bar2,grid_bottom="55%",grid_top="30%")
grid.add(bar3,grid_bottom="30%",grid_top="55%") 
grid.add(bar4,grid_bottom="5%",grid_top="80%")
grid.render('城市分类标签.html')