#!/usr/bin/env python3
'数据去重'

import pandas as pd

df=pd.read_csv('the_wind_guardians.csv',encoding='gb18030')

df.drop_duplicates(subset=['评论','昵称'],keep='first',inplace=True)

df.to_csv('the_wind_guardians_norepeat.csv',encoding='gb18030')
