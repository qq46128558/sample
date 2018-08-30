#!/usr/bin/env python3

'地图式省份数据展示'

import logging
from pyecharts import Map

logging.basicConfig(level=logging.INFO)

# 初始化
map=Map('地图式(省份)数据展示','数据来源:手工录入',title_color="#fff",title_top="5%",title_pos="center",width=1366-15,height=594-16,background_color="#404a59")


attr=['广东','台湾','北京','湖南','西藏','江西','广西','湖北','云南','福建','浙江','四川']
value=[101,27,86,68,12,23,5,2,7,9,150,39]

map.add("省份",attr,value,maptype='china',is_visualmap=True,visual_text_color='#000',legend_top="15%")
map.render('map.html')