#!/usr/bin/env python3

'北京链家租房数据清洗'

import logging
import pandas as pd
import re

logging.basicConfig(level=logging.INFO)

df=pd.read_csv('lianjia.csv',encoding='utf_8_sig')

# 58.13平米  => 58.13
df['square']=df.square.map(lambda x:re.search(r'(\d+\.?\d*)',x).group(1))
# 石佛营租房 => 石佛营
df['detail_place']=df.detail_place.map(lambda x:re.search(r'^(.*)租房$',x).group(1))
# 高楼层(共6层) => 高楼层
df.floor=df.floor.map(lambda x:re.search(r'(.*)\(.*\)$',x).group(1))
# 高楼层(共6层) => 6
df.total_floor=df.total_floor.map(lambda x:re.search(r'^.*\(共(\d+)层\)$',x).group(1))

df.to_csv('lianjia_filter.csv',index=False,encoding='utf_8_sig')
