#!/usr/bin/env python3

'北京链家租房数据可视化呈现'


import logging
import pandas as pd
from pyecharts import Bar,Line,Overlap,Grid,Pie

logging.basicConfig(level=logging.INFO)

df=pd.read_csv('lianjia_filter.csv',encoding='utf_8_sig')

logging.info('{}{}'.format('\n',df.describe()))


'北京路段_房屋均价分布图'
df_detail_place=df.groupby(by='detail_place').price.agg(['mean','count']).reset_index().sort_values(by='count',ascending=False)[0:8]
logging.debug(df_detail_place)
#  df_detail_place.mean:'function' object has no attribute 'map'
df_detail_place['mean']=df_detail_place['mean'].map(lambda x:round(x,0))

line = Line("北京路段房租均价",title_pos="right")
line.add("路段",df_detail_place['detail_place'],df_detail_place['mean'],
	is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    mark_point=['min','max'],xaxis_interval=0,line_color='lightblue',
    line_width=1,mark_point_textcolor='black',mark_point_color='lightblue',
    is_splitline_show=False,
    legend_top="42%",legend_pos="25%")

bar = Bar("路段租房数量",title_top="40%")
bar.add("路段",df_detail_place['detail_place'],df_detail_place['count'],
	is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False,
    legend_top="42%",legend_pos="25%")

overlap = Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1,is_add_yaxis=True)
# overlap.render('北京路段_房屋均价分布图.html')

""" 房源价格区间分布图 """
bins=[0,3000,6000,12000,24000]
labels=['便宜','普通','高端','豪华']
# 价格分区离散化，并给每个区间取名(value_counts出现频率)
df_price=pd.cut(df['price'],bins=bins,labels=labels).value_counts().sort_index()
logging.info(df_price)
bar2=Bar("价格区间&房源数量分布")
bar2.add("房源数",df_price.index,df_price.values,
is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False,
    legend_top="2%",legend_pos="25%")
# bar.render('价格区间&房源数量分布.html')


""" 房屋面积分布 """
bins =[0,90,200,700]
level = ['小户型', '普通','大户型']
df_square = pd.cut(df['square'],bins = bins,labels = level).value_counts()

pie = Pie("房屋面积分布")
pie.add(
    "面积",
    df_square.index,
    df_square.values,
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical"
)


#房屋面积&价位分布
# 加一列square_level
df['square_level'] = pd.cut(df['square'],bins = bins,labels = level)
df_square_price = df.groupby('square_level').price.mean().reset_index()
df_square_price.price=df_square_price.price.map(lambda x:round(x,0))
logging.info(df_square_price)

bar3 = Bar("房屋面积&价位分布",title_top='55%',title_pos="55%")
bar3.add("平均价",df_square_price['square_level'],df_square_price['price'],
    is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False,
    legend_top='52%',legend_pos='75%')


grid=Grid(width=1280,height=700)
grid.add(bar2,grid_top="5%",grid_bottom="65%",grid_left="5%",grid_right="55%")
# overlap部分不能合并显示
grid.add(overlap,grid_top="45%",grid_bottom="5%",grid_left="5%",grid_right="55%")
# grid.add(pie,grid_top="5%",grid_bottom="55%",grid_left="55%",grid_right="5%")
# grid.add(bar3,grid_top="55%",grid_bottom="5%",grid_left="55%",grid_right="5%")
grid.render('北京房源数据分析.html')