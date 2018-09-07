#!/usr/bin/env python3

'地图式数据展示'

import logging
from pyecharts import Geo
from pyecharts import Style

logging.basicConfig(level=logging.INFO)


# style = Style(
#    title_color = "#fff",
#    title_pos = "left",
#    width = 1440-15, # (document.documentElement.scrollWidth)
#    height = 767-16, # (document.documentElement.scrollHeight)
#    background_color = "#404a59"
# )
# **style.init_style
# 也可以传入上面的style
# 初始化
geo=Geo('地图式数据展示','数据来源:手工录入',title_color="#fff",title_top="5%",title_pos="center",width=1366-15,height=594-16,background_color="#404a59")


attr=['珠海','澳门','北京','广州','深圳','杭州','青岛','孝感','新丰县','乳源瑶族自治县','昆明','厦门']
value=[101,27,86,68,12,23,5,2,7,9,150,39]
# 传入数据
# 城市：图示
# visual_range: 图例数值范围
# visual_text_color: 图例颜色
# legend_top: 图例顶部位置
# legend_pos: 图例水平位置
# symbol_size: 地图上的符号大小
# is_visualmap: 是否显示图例
# is_piecewise: 分段显示图例
# visual_split_number: 图例分段数量
geo.add("城市",attr,value,visual_range=[0,100],visual_text_color="white",legend_top="15%",legend_pos="center",symbol_size=10,is_visualmap=True,is_piecewise=True,visual_split_number=4)
geo.render('geo.html')