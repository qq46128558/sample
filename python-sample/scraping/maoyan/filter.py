#!/usr/bin/env python3
'数据去重'

import pandas as pd

df=pd.read_csv('hidden_man.csv',encoding='gb18030')

df=df.drop_duplicates(subset=['评论','昵称'],keep='first')
df.to_csv('hidden_man_norepeat.csv',encoding='gb18030')
