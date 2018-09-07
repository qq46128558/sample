#!/usr/bin/env python3

'重叠图(折线+柱状)'


import logging
import pandas as pd
from pyecharts import Bar,Line,Overlap

logging.basicConfig(level=logging.INFO)

# df=pd.read_csv('city_cy.csv',encoding='utf_8_sig')
df=pd.read_csv('city_cy.csv',encoding='gb18030')

logging.info('{}{}'.format('\n',df.describe()))


'城市餐饮点评top20+count(特色美食数)'
df_filter=df.groupby(by='城市').票数.agg(['count','sum']).reset_index().sort_values(by='sum',ascending=False)[0:20]
# 换种写法的话,暂未知如何按票数下的sum列排序
# df_filter=df.groupby(by='城市').agg({'票数':['count','sum']}).reset_index().sort_values(by='票数.sum',ascending=False)[0:20]
# df_filter=df.groupby(by='城市').agg({'票数':['count','sum']}).reset_index()[['城市','票数'['count']]]

logging.info(df_filter)


# 遗留问题,此title重叠后无显示
line = Line("特色美食统计",title_pos="right")
line.add("特色美食数量",df_filter['城市'],df_filter['count'],
	is_splitline_show=True,
	is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    mark_point=['min','max'],xaxis_interval=0,line_color='lightblue',
    line_width=4,mark_point_textcolor='black',mark_point_color='lightblue',
    legend_top="10",legend_pos="right")

bar = Bar("美食之城Top20",title_pos="left")
bar.add("票数",df_filter['城市'],df_filter['sum'],
	is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)

overlap = Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1,is_add_yaxis=True)
overlap.render('overlap.html')