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
   title_pos = "left",
   width = 1440-15, # (document.documentElement.scrollWidth)
   height = 767-16, # (document.documentElement.scrollHeight)
   background_color = "#404a59"
)

geo = Geo("《邪不压正》评论人群地理位置","数据来源:猫眼电影",**style.init_style)
# 城市：图示
# visual_range: 图例数值范围
# visual_text_color: 图例颜色
# symbol_size: 地图上的符号大小
# is_visualmap: 是否显示图例
# is_piecewise: 分段显示图例
# visual_split_number: 图例分段数量
geo.add("城市",series.keys().tolist(),series.values.tolist(),visual_range=[0,25],visual_text_color="white",symbol_size=10,is_visualmap=True,is_piecewise=True,visual_split_number=4)
geo.render('geo.html')


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

# C:\Users\46128\AppData\Local\Programs\Python\Python36\lib\site-packages\pyecharts\charts\geo.py line 40
        # # edit by peter 2018-07-25
        # if coordinate is None:
        #     coordinate=get_coordinate(name+"县")
        #     if coordinate is None:
        #         coordinate=get_coordinate(name+"市")
        #         if coordinate is None:
        #             coordinate=get_coordinate(name+"区")
        #             if coordinate is None and name=="湘西":
        #                 coordinate=get_coordinate(name+"土家族苗族自治州")