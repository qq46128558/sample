#!/usr/bin/env python3

'折线图'

import logging
import pandas as pd
from pyecharts import Line

logging.basicConfig(level=logging.INFO)

# 读入数据为呈现图表
df=pd.read_csv('city_yj.csv',encoding='gb18030')
# 餐饮游记排序后再切片取前20名
df=df.sort_values(by="餐饮游记",ascending=False)[0:20]
logging.info(df)
# 还原排序
df=df.sort_values(by="城市")

# title_top 标题的top位置(可以用百分比) width 图表宽 height 图表高
# title_pos 可以控制标题的x轴位置,可以用百分比
line=Line('餐饮类标签',title_top="10",width=800,height=500)
# is_splitline_show 显示X轴的标尺线
# is_stack 未知
# xaxis_rotate 未知
# yaxix_min 未知
# mark_point 标记点(min,max)
# xaxis_interval X轴间隔多少个“城市”显示
# line_color 县颜色
# line_width 线宽
# mark_point_textcolor 标记点的字体颜色
# mark_point_color 未知
# legend_top 图例的顶部位置(可以用百分比)
# legend_pos 以控制图例的x轴位置,可以用百分比
line.add("游记数量",df['城市'],df['餐饮游记'],
    is_splitline_show=True,
	is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    mark_point=['min','max'],xaxis_interval=0,line_color='lightblue',
    line_width=4,mark_point_textcolor='black',mark_point_color='lightblue',
    legend_top="10",legend_pos="right")
line.render('line.html')
