#!/usr/bin/env python3

'大众点评小龙虾统计信息'

import logging
# import matplotlib.pyplot as plt
import pandas as pd
from pyecharts import Bar
from pyecharts import Grid

logging.basicConfig(level=logging.INFO)

# 读取数据
df=pd.read_csv('xiaolongxia.csv',encoding='gb18030')

# 按城市分组
# df=df.groupby(by="城市").agg({'点评':sum}).reset_index()
# df.to_csv('xiaolongxia_dianping_sum.csv',index=False,encoding='gb18030')
# 人均
# df.drop(df[df['人均']==0].index,inplace=True)
# df=df.groupby(by='城市').agg({'人均':'mean'}).reset_index()
# df.to_csv('xiaolongxia_renjun_mean.csv',index=False,encoding='gb18030')
# quit()


# 点评分
df=pd.read_csv('xiaolongxia_dianping_sum.csv',encoding='gb18030')
df_dianping=df.sort_values(by="点评",ascending=False)[0:20]
logging.info(df_dianping)
# 人均消费
df=pd.read_csv('xiaolongxia_renjun_mean.csv',encoding='gb18030')
df_renjun=df.sort_values(by="人均",ascending=False)[0:20]


# 柱状图
bar1=Bar('小龙虾人气城市',title_top="10px",title_pos="5%")
bar2=Bar('人均消费排名',title_top="120px",title_pos="5%")

# is_splitline_show 水平标线 xaxis_rotate 未知 legend_top 图例离页面顶部距离
bar1.add('点评',df_dianping['城市'],df_dianping['点评'],is_splitline_show=True,xaxis_rotate=30,legend_top="10px",legend_pos="50%")
bar2.add('人均消费',df_renjun['城市'],df_renjun['人均'],is_splitline_show=True,xaxis_rotate=30,legend_top="120px",legend_pos="50%")

grid = Grid(height=700,width=1280)
# grid_bottom 图表底部离页面底部距离 grid_top 图表顶部离页面顶部距离
'''100%-(grid_bottom:80 + grid_top 5)=15%即为柱状图高的占比, 即4个图占60%空间,并留一些白''' 
'''先填出第一个图(80,5)与最后一个图(5,80)的位置, 然后用(80-5)/(4-1)=25为增量间距'''
# grid.add(bar1,grid_bottom="80%",grid_top="6%" ,grid_left="5%",grid_right="55%")
grid.add(bar1,grid_top="50px",grid_bottom="550px")
grid.add(bar2,grid_top="170px",grid_bottom="430px")
grid.render('小龙虾.html')