#!/usr/bin/env python3

""" pandas DataFrame的应用 """

import pandas as pd
from numpy import NaN
import time

# 写csv文件
list=[]
dict={
    'comment':'完全不知道演什么，从来没看过这么差劲的片子～',
    'date':'2018/7/21',
    'rate':2,
    'city':'长沙',
}
list.append(tuple(dict.values()))
dict={
    'comment':'好看，意犹未尽，反派干脆利落，惨烈的剧情却配了雄伟的交响乐，优美的享受着就看完了整部片子。',
    'date':'2018/7/21',
    'rate':5,
    'city':'晋中',
}
list.append(tuple(dict.values()))
df=pd.DataFrame(data=list,columns=['评论','日期','评分','城市'])
df.to_csv('hidden_man.csv',index=False,encoding='gb18030')

# 读csv文件
df=pd.read_csv('hidden_man.csv',encoding='gb18030')
print(df['城市'])
# 0    长沙
# 1    晋中
# Name: 城市, dtype: object




# 将dict转成DataFrame(列模式)
dict={'浙': 541, '苏': 485, '粤': 477}
# If using all scalar values, you must pass an index
df=pd.DataFrame(dict,index=[0])
print(df,'\n')
#      浙    苏    粤
# 0  541  485  477


# 将list转成DataFrame(行模式)
list=[('浙', 541), ('苏', 485), ('粤', 477)]
df=pd.DataFrame(data=list,columns=['地区','数量'])
print(df,'\n')
#   地区   数量
# 0  浙  541
# 1  苏  485
# 2  粤  477

# 将dict转成DataFrame(列模式)
dict={'标题1':['值1','值2','值3','值4','值空'],'标题2':['值5','值6','值7','值8',NaN]}
df=pd.DataFrame(dict)
print(df,'\n')
#   标题1 标题2
# 0  值1  值5
# 1  值2  值6
# 2  值3  值7
# 3  值4  值8
# 4  值空  NaN

# 取标题2等于值7的行
df_one=df[df['标题2']=='值7']
print(df_one,'\n')
#   标题1 标题2
# 2  值3  值7

# 移除标题2等于值7的行
df_drop=df.drop(df[df['标题2']=='值7'].index,inplace=False)
print(df_drop,'\n')
#   标题1  标题2
# 0  值1   值5
# 1  值2   值6
# 3  值4   值8
# 4  值空  NaN

# 查找NaN值并替换为字符串'无'
df['标题2'][df['标题2'].isnull()]='无'
print(df,'\n')
#   标题1 标题2
# 0  值1  值5
# 1  值2  值6
# 2  值3  值7
# 3  值4  值8
# 4  值空   无

# 将标题2的内容,值字替换为正字
df['标题2']=df['标题2'].str.replace('值','正')
print(df,'\n')
#   标题1 标题2
# 0  值1  正5
# 1  值2  正6
# 2  值3  正7
# 3  值4  正8
# 4  值空   无

# 删除带正字的行
df_drop2=df.drop(df[df['标题2'].str.contains('无')].index,inplace=False)
print(df_drop2,'\n')
#   标题1 标题2
# 0  值1  正5
# 1  值2  正6
# 2  值3  正7
# 3  值4  正8

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



# 数据去重
data={'pop':['a','b','c','d','b','c','d'],'state':[1,2,3,4,5,6,7]}
df=pd.DataFrame(data)
# keep='first' 将重复数据保留一个
a = df.drop_duplicates(subset=['pop'],keep='first')
print(a)
#   pop  state
# 0   a      1
# 1   b      2
# 2   c      3
# 3   d      4


# 查看(上面)有哪些重复得数据
# keep=False 将重复数据全部去除
b=df.drop_duplicates(subset=['pop'],keep=False)
a=a.append(b,ignore_index=True)
a.drop_duplicates(subset=['pop'],keep=False,inplace=True)
print(a)
#   pop  state
# 1   b      2
# 2   c      3
# 3   d      4


# 先有结构,再append数据
df=pd.DataFrame(columns=['date','name','value'])
df=df.append({'date':time.ctime(),'name':'Rose','value':101},ignore_index=True)
df=df.append({'date':time.ctime(),'name':'Mary','value':160},ignore_index=True)
df=df.append({'date':time.ctime(),'name':'Loli','value':86},ignore_index=True)
print(df)
#                        date  name value
# 0  Tue Aug 28 13:48:43 2018  Rose   101
# 1  Tue Aug 28 13:48:43 2018  Mary   160
# 2  Tue Aug 28 13:48:43 2018  Loli    86
