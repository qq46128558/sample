#!/usr/bin/env python3

""" pandas DataFrame统计数据出现的频率"""

import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)

data={'地区':['北京', '深圳', '上海', '广州','北京','北京','北京','北京','北京','广州', '广州', '广州', '广州', '广州', '深圳', '深圳', '深圳', '上海', '上海']}
df=pd.DataFrame(data)

# 出现频率
series=df['地区'].value_counts()
logging.info(series)
# INFO:root:北京    6
# 广州    6
# 深圳    4
# 上海    3
# Name: 地区, dtype: int64

# 取数据频次的键
logging.info(series.keys().tolist())
# INFO:root:['广州', '北京', '深圳', '上海']

# 取数据频次的值
logging.info(series.values.tolist())
# INFO:root:[6, 6, 4, 3]

# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
logging.debug(dir(series))