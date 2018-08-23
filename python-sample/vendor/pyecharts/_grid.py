#!/usr/bin/env python3

'Grid组合图(如多个柱状图)'

import logging
import pandas as pd
from pyecharts import Bar
from pyecharts import Grid

logging.basicConfig(level=logging.INFO)

# 读入数据为呈现图表
df=pd.read_csv('city_yj.csv',encoding='gb18030')
# 餐饮游记排序后再切片取前20名
df1=df.sort_values(by="餐饮游记",ascending=False)[0:20]
logging.info(df1)
df2=df.sort_values(by="景点游记",ascending=False)[0:20]
df3=df.sort_values(by="娱乐游记",ascending=False)[0:20]
df4=df.sort_values(by="购物游记",ascending=False)[0:20]


# title_top 标题的top位置(可以用百分比) width 图表宽 height 图表高
# title_pos 可以控制标题的x轴位置,可以用百分比
# 先算出柱状图高度占比，下面有，得出间隔增量是25
bar1=Bar('餐饮类标签排名',title_top="0%")
bar2=Bar('景点类标签排名',title_top="25%")
bar3=Bar('娱乐类标签排名',title_top="50%")
bar4=Bar('购物类标签排名',title_top="75%")
# is_splitline_show 显示X轴的标尺线
# xaxis_rotate 未知
# legend_top 图例的顶部位置(可以用百分比)
# legend_pos 以控制图例的x轴位置,可以用百分比
# 图例的名字不同，则柱状图的颜色不同
bar1.add('餐饮游记',df1['城市'],df1['餐饮游记'],is_splitline_show=True,xaxis_rotate=30,legend_top="0%")
bar2.add('景点游记',df2['城市'],df2['景点游记'],is_splitline_show=True,xaxis_rotate=30,legend_top="25%")
bar3.add('娱乐游记',df3['城市'],df3['娱乐游记'],is_splitline_show=True,xaxis_rotate=30,legend_top="50%")
bar4.add('购物游记',df4['城市'],df4['购物游记'],is_splitline_show=True,xaxis_rotate=30,legend_top="75%")

grid=Grid(width=1280,height=700)
# grid_top grid组件离容器顶部距离
# grid_bottom grid组件离容器底部距离
# 也支持grid_left grid_right
# 100-(80+5)=15 容器的高度占比
grid.add(bar1,grid_top="5%",grid_bottom="80%")
# 四个柱状图高度占比:4*15=60
# 中间隔占比:100-60-5-5(第一5和最后5)=30,30/3=10
# 则间隔增量是：10(间隔占比)+15(柱状图高度占比)=25
grid.add(bar2,grid_top="30%",grid_bottom="55%")
grid.add(bar3,grid_top="55%",grid_bottom="30%")
grid.add(bar4,grid_top="80%",grid_bottom="5%")
'''
# 布局如图
——————————————
5
——————————————
15 餐饮游记
——————————————
10
——————————————
15 景点游记
——————————————
10
——————————————
15 娱乐游记
——————————————
10
——————————————
15 购物游记
——————————————
5
——————————————
'''

grid.render("grid.html")