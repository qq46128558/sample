#!/usr/bin/env python3

import pandas as pd

dict={'标题1':['值1','值2','值3','值4'],'标题2':['值5','值6','值7','值8']}
df=pd.DataFrame(dict)
print(df)
#   标题1 标题2
# 0  值1  值5
# 1  值2  值6
# 2  值3  值7
# 3  值4  值8

list1=['VC','1/1/1','增强免疫力']
list2=['钙','2/0/2','强化骨骼']
list3=['锌','0/1/0','提高男性魅力']
L=[]
L.append(list1)
L.append(list2)
L.append(list3)
df=pd.DataFrame(data=L,columns=['营养素','用量','主要作用'])
print(df)
#   营养素     用量    主要作用
# 0  VC  1/1/1   增强免疫力
# 1   钙  2/0/2    强化骨骼
# 2   锌  0/1/0  提高男性魅力
df.to_csv('1.csv',index=False,encoding='gbk')
# 1/1/1 写入为2001/1/1问题,未解决