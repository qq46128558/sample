#!/usr/bin/env python3

'饼图式数据展示'

import logging
from pyecharts import Pie
from pyecharts import Style

# `Style`类可用于简化配置项编写，可用于在同一个图或者多个图内保持统一的风格
style=Style(
	title_color="white",
	title_pos="left",
	width=1366-15,
	height=594-16,
	background_color='black',
	)
logging.basicConfig(level=logging.INFO)

attr=['澳门','珠海','广州','北京']
value=[86,67,128,99]

# C:\Users\Peter\AppData\Local\Programs\Python\Python35\lib\site-packages\pyecharts\charts\pie.py
pie=Pie("饼图式数据展示","数据来源:手工录入",**style.init_style)
# center: 饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标，默认为 [50, 50]默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
# radius: 饼图的半径，数组的第一项是内半径，第二项是外半径，默认为 [0, 75]默认设置成百分比，相对于容器高宽中较小的一项的一半。
# rosetype: 是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。默认为'radius' radius：扇区圆心角展现数据的百分比，半径展现数据的大小。area：所有扇区圆心角相同，仅通过半径展现数据大小。
# is_legend_show: 显示图例
# is_label_show: 显示标签
pie.add("7-17",attr,value,center=[50,50],is_random=True,radius=[0,75],rosetype='area',is_legend_show=True,is_label_show=True)
pie.render('pie.html')
