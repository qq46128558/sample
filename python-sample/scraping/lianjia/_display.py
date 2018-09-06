#!/usr/bin/env python3

'北京链家租房数据可视化呈现'


import logging
import pandas as pd
from pyecharts import Bar,Line,Overlap

logging.basicConfig(level=logging.INFO)

df=pd.read_csv('lianjia_filter.csv',encoding='utf_8_sig')

logging.info('{}{}'.format('\n',df.describe()))


'北京路段_房屋均价分布图'
df_detail_place=df.groupby(by='detail_place').price.agg(['mean','count']).reset_index().sort_values(by='count',ascending=False)[0:20]
logging.debug(df_detail_place)

line = Line("北京主要路段房租均价")
line.add("路段",df_detail_place['detail_place'],df_detail_place['mean'],
	is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    mark_point=['min','max'],xaxis_interval=0,line_color='lightblue',
    line_width=4,mark_point_textcolor='black',mark_point_color='lightblue',
    is_splitline_show=False)

bar = Bar("北京主要路段房屋数量")
bar.add("路段",df_detail_place['detail_place'],df_detail_place['count'],
	is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)

overlap = Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1,is_add_yaxis=True)
overlap.render('北京路段_房屋均价分布图.html')