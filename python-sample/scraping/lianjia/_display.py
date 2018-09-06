#!/usr/bin/env python3

'北京链家租房数据可视化呈现'


import logging
import pandas as pd
logging.basicConfig(level=logging.INFO)

df=pd.read_csv('lianjia_filter.csv',encoding='utf_8_sig')

logging.info('{}{}'.format('\n',df.describe()))
