#!/usr/bin/env python3

'人群地理位置图'

# 引用了pecharts，logging放这里才有效果
import logging
import pandas as pd
from pyecharts import Style
from pyecharts import Geo


logging.basicConfig(level=logging.INFO)

# 读取城市数据
df=pd.read_csv('hidden_man_norepeat.csv',encoding='gb18030')

# df.drop(df[df['城市']=='大丰'].index,inplace=True)

series=df['城市'].value_counts()
# logging.info(series.keys().tolist())
# logging.info(series.values.tolist())
# logging.info(len(series.keys().tolist()))
# logging.info(len(series.values.tolist()))

style = Style(
   title_color = "#fff",
   title_pos = "center",
   width = 1200,
   height = 600,
   background_color = "#404a59"
)

# geo = Geo("《邪不压正》评论人群地理位置","数据来源:猫眼电影",**style.init_style)
# geo.add("",series.keys().tolist(),series.values.tolist(),visual_range=[0,20],
#  visual_text_color="#fff",symbol_size=20,
#  is_visualmap=True,is_piecewise=True, 
#  visual_split_number=4)
# geo.render()


# data = [("惠来县", 80), ('漳州', 180)]
# geo = Geo("全国主要城市空气质量", "data from pm2.5")
# attr, value = geo.cast(data)
# geo.add("city", attr, value, visual_range=[0, 200], maptype='china', visual_text_color="#fff",
#         symbol_size=10, is_visualmap=True)
# # geo.show_config()
# geo.render()


# 安装了地图仍报错
# ValueError: No coordinate is specified for 惠来
# 解决: 是字符串完全匹配问题, 改为惠来县即可