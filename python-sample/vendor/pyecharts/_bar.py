#!/usr/bin/env python3

'柱状图'

import logging
import pandas as pd
from pyecharts import Bar

logging.basicConfig(level=logging.INFO)

# 读入数据为呈现图表
df=pd.read_csv('city_yj.csv',encoding='gb18030')
# 餐饮游记排序后再切片取前20名
df=df.sort_values(by="餐饮游记",ascending=False)[0:20]
logging.info(df)
# 还原排序
# df=df.sort_values(by="城市")

# title_top 标题的top位置(可以用百分比) width 图表宽 height 图表高
# title_pos 可以控制标题的x轴位置,可以用百分比
bar=Bar('餐饮类标签排名',title_top="10",width=800,height=500)
# is_splitline_show 显示X轴的标尺线
# xaxis_rotate 未知
# legend_top 图例的顶部位置(可以用百分比)
# legend_pos 以控制图例的x轴位置,可以用百分比
# is_stack 未知
# xaxis_interval X轴间隔多少个“城市”显示
# yaxix_min 未知
bar.add('游记数量',df['城市'],df['餐饮游记'],
	is_splitline_show=True,xaxis_rotate=30,legend_top="10",
	is_stack=True,xaxis_interval=0,yaxix_min=4.2
	)
bar.render('bar.html')