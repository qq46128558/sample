#!/usr/bin/env python3

'播放数据排名'

import logging
import pandas as pd
from pyecharts import Bar
from pyecharts import Grid

logging.basicConfig(level=logging.INFO)

df=pd.read_csv('proseries.csv',encoding='gb18030')

# 2018/01/01-2018/08/28
# 按名称及剧类排序
df=df.groupby(by=['name','type']).agg({'play_num':'sum'}).reset_index()

df0=df[df['type']=='电视剧']
df1=df[df['type']=='网络剧']
df2=df[df['type']=='综艺']

# 放在这里除报错
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead

df0=df0.sort_values(by='play_num',ascending=False)[0:10]
df0['play_num']=df0['play_num'].map(lambda x: x//10000)
df1=df1.sort_values(by='play_num',ascending=False)[0:10]
df1['play_num']=df1['play_num'].map(lambda x: x//10000)
df2=df2.sort_values(by='play_num',ascending=False)[0:10]
df2['play_num']=df2['play_num'].map(lambda x: x//10000)

bar0=Bar('2018年电视剧热播排名',title_top='0%')
bar1=Bar('2018年网络剧热播排名',title_top='35%')
bar2=Bar('2018年综艺节目热播排名',title_top='70%')

bar0.add('电视剧播放量(亿)',df0['name'],df0['play_num'],is_splitline_show=True,legend_top='0%')
bar1.add('网络剧播放量(亿)',df1['name'],df1['play_num'],is_splitline_show=True,legend_top='35%')
bar2.add('综艺节目播放量(亿)',df2['name'],df2['play_num'],is_splitline_show=True,legend_top='70%')

grid=Grid(width=1280,height=500)

grid.add(bar0,grid_top='10%',grid_bottom='75%')
grid.add(bar1,grid_top='45%',grid_bottom='40%')
grid.add(bar2,grid_top='80%',grid_bottom='5%')

grid.render('proseries.html')
