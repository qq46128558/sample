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
df.drop(df[df['城市'].str.contains('县')].index,inplace=True)
df.drop(df[df['城市'].str.contains('区')].index,inplace=True)

# 按城市分组
# df=df.groupby(by="城市").agg({'点评':sum}).reset_index()
# df.to_csv('xiaolongxia_dianping_sum.csv',index=False,encoding='gb18030')
# 人均
# df.drop(df[df['人均']==0].index,inplace=True)
# df=df.groupby(by='城市').agg({'人均':'mean'}).reset_index()
# df.to_csv('xiaolongxia_renjun_mean.csv',index=False,encoding='gb18030')
# 口味环境服务
# df.drop(df[df['口味']==0].index,inplace=True)
# df=df.groupby(by='城市').agg({'口味':'mean','环境':'mean','服务':'mean'}).reset_index()
# df.to_csv('xiaolongxia_kouwei_mean.csv',index=False,encoding='gb18030')
# quit()


# 点评分
df_dianping=df.groupby(by="城市").agg({'点评':sum}).reset_index()
df_dianping=df_dianping.sort_values(by="点评",ascending=False)[0:20]
logging.info(df_dianping)
# 人均消费
df_renjun=df.drop(df[df['人均']==0].index,inplace=False)
df_renjun=df_renjun.groupby(by='城市').agg({'人均':'mean'}).reset_index()
df_renjun=df_renjun.sort_values(by="人均",ascending=False)[0:20]
df_renjun['人均']=df_renjun['人均'].map(lambda x:int(x))
# 口味环境服务
df_kouwei=df.drop(df[df['口味']==0].index,inplace=False)
df_kouwei=df_kouwei.groupby(by='城市').agg({'口味':'mean'}).reset_index()
df_kouwei=df_kouwei.sort_values(by='口味',ascending=False)[0:20]
df_kouwei['口味']=df_kouwei['口味'].map(lambda x:round(x,2))

df_huanjing=df.drop(df[df['环境']==0].index,inplace=False)
df_huanjing=df_huanjing.groupby(by='城市').agg({'环境':'mean'}).reset_index()
df_huanjing=df_huanjing.sort_values(by='环境',ascending=False)[0:20]
df_huanjing['环境']=df_huanjing['环境'].map(lambda x:round(x,2))

df_fuwu=df.drop(df[df['服务']==0].index,inplace=False)
df_fuwu=df_fuwu.groupby(by='城市').agg({'服务':'mean'}).reset_index()
df_fuwu=df_fuwu.sort_values(by='服务',ascending=False)[0:20]
df_fuwu['服务']=df_fuwu['服务'].map(lambda x:round(x,2))

# 柱状图
bar1=Bar('小龙虾人气城市',title_top="10px",title_pos="5%")
bar2=Bar('人均消费排名',title_top="180px",title_pos="5%")
bar3=Bar('口味评分排名',title_top="350px",title_pos="5%")
bar4=Bar('环境评分排名',title_top="520px",title_pos="5%")
bar5=Bar('服务评分排名',title_top="690px",title_pos="5%")

# is_splitline_show 水平标线 xaxis_rotate 未知 legend_top 图例离页面顶部距离
bar1.add('点评',df_dianping['城市'],df_dianping['点评'],is_splitline_show=True,xaxis_rotate=30,legend_top="10px",legend_pos="50%")
bar2.add('人均消费',df_renjun['城市'],df_renjun['人均'],is_splitline_show=True,xaxis_rotate=30,legend_top="180px",legend_pos="50%")
bar3.add('评分',df_kouwei['城市'],df_kouwei['口味'],is_splitline_show=True,xaxis_rotate=30,legend_top="350px",legend_pos="50%")
bar4.add('评分',df_huanjing['城市'],df_huanjing['环境'],is_splitline_show=True,xaxis_rotate=30,legend_top="520px",legend_pos="50%")
bar5.add('评分',df_fuwu['城市'],df_fuwu['服务'],is_splitline_show=True,xaxis_rotate=30,legend_top="690px",legend_pos="50%")

grid = Grid(height=1200,width=1280)
# grid_bottom 图表底部离页面底部距离 grid_top 图表顶部离页面顶部距离
'''100%-(grid_bottom:80 + grid_top 5)=15%即为柱状图高的占比, 即4个图占60%空间,并留一些白''' 
'''先填出第一个图(80,5)与最后一个图(5,80)的位置, 然后用(80-5)/(4-1)=25为增量间距'''
# grid.add(bar1,grid_bottom="80%",grid_top="6%" ,grid_left="5%",grid_right="55%")
grid.add(bar1,grid_top="50px",grid_bottom="1050px")
grid.add(bar2,grid_top="220px",grid_bottom="880px")
grid.add(bar3,grid_top="390px",grid_bottom="710px")
grid.add(bar4,grid_top="560px",grid_bottom="540px")
grid.add(bar5,grid_top="730px",grid_bottom="370px")
grid.render('小龙虾.html')