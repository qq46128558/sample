#!/usr/bin/env python3

'''DataFrame 是一个带有索引的二维数据结构，每列可以有自己的名字，并且可以有不同的数据类型。'''

import logging
import pandas as pd
# 这些数据结构构建在 Numpy 数组之上，这意味着它们效率很高。
import numpy as np

logging.basicConfig(level=logging.INFO)

# 构建dataframe
index=pd.Index(data=["Tom", "Bob", "Mary", "James"], name="user_name")
data={
    "age": [18, 30, 25, 40],
    "city": ["BeiJing", "ShangHai", "GuangZhou", "ShenZhen"]
}
user_info=pd.DataFrame(data=data,index=index)
logging.info(user_info)
# INFO:root:           age       city
# user_name
# Tom         18    BeiJing
# Bob         30   ShangHai
# Mary        25  GuangZhou
# James       40   ShenZhen

# 另一种方式: 先构建一个二维数组，然后再生成一个列名称列表
data=[
[18, "BeiJing"], 
[30, "ShangHai"], 
[25, "GuangZhou"], 
[40, "ShenZhen"]
]
columns=['age','city']
user_info=pd.DataFrame(data=data,index=index,columns=columns)
logging.info(user_info)
# INFO:root:           age       city
# user_name
# Tom         18    BeiJing
# Bob         30   ShangHai
# Mary        25  GuangZhou
# James       40   ShenZhen


# 访问行
logging.info(user_info.loc["Tom"])
# INFO:root:age          18
# city    BeiJing
# Name: Tom, dtype: object

logging.info(user_info.iloc[0])
# INFO:root:age          18
# city    BeiJing
# Name: Tom, dtype: object

# 用切片访问多行
logging.info(user_info.iloc[1:3])
# INFO:root:           age       city
# user_name
# Bob         30   ShangHai
# Mary        25  GuangZhou

# 访问列
logging.info(user_info.age)
logging.info(user_info['age'])
# INFO:root:user_name
# Tom      18
# Bob      30
# Mary     25
# James    40
# Name: age, dtype: int64


# 访问多列
logging.info(user_info[["city","age"]])
# INFO:root:                city  age
# user_name
# Tom          BeiJing   18
# Bob         ShangHai   30
# Mary       GuangZhou   25
# James       ShenZhen   40

# 新增列
user_info["sex"]="male"
logging.info(user_info)
# INFO:root:           age       city   sex
# user_name
# Tom         18    BeiJing  male
# Bob         30   ShangHai  male
# Mary        25  GuangZhou  male
# James       40   ShenZhen  male

# 删除列
user_info.pop("sex")
logging.info(user_info)
# INFO:root:           age       city
# user_name
# Tom         18    BeiJing
# Bob         30   ShangHai
# Mary        25  GuangZhou
# James       40   ShenZhen

# 新增列(不同值)
user_info["sex"]=["male", "male", "female", "male"]
logging.info(user_info)
# INFO:root:           age       city     sex
# user_name
# Tom         18    BeiJing    male
# Bob         30   ShangHai    male
# Mary        25  GuangZhou  female
# James       40   ShenZhen    male

# 不修改原有的dataframe而新增列,用assign
user_info_M=user_info.assign(age_ten_year=user_info.age+10)
logging.info(user_info)
# INFO:root:           age       city     sex
# user_name
# Tom         18    BeiJing    male
# Bob         30   ShangHai    male
# Mary        25  GuangZhou  female
# James       40   ShenZhen    male
logging.info(user_info_M)
# INFO:root:           age       city     sex  age_ten_year
# user_name
# Tom         18    BeiJing    male            28
# Bob         30   ShangHai    male            40
# Mary        25  GuangZhou  female            35
# James       40   ShenZhen    male            50

# 不修改原有的dataframe而新增列,用assign
user_info_M=user_info_M.assign(sex_code=np.where(user_info_M["sex"]=="male",1,0))
logging.info(user_info_M)
# INFO:root:           age       city     sex  age_ten_year  sex_code
# user_name
# Tom         18    BeiJing    male            28         1
# Bob         30   ShangHai    male            40         1
# Mary        25  GuangZhou  female            35         0
# James       40   ShenZhen    male            50         1


'''常用的基本功能'''
# 了解下数据的整体情况
user_info.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 4 entries, Tom to James
# Data columns (total 3 columns):
# age     4 non-null int64
# city    4 non-null object
# sex     4 non-null object
# dtypes: int64(1), object(2)
# memory usage: 288.0+ bytes

# 查看头部的 n 条数据可以使用 head 方法，查看尾部的 n 条数据可以使用 tail 方法
logging.info(user_info.head(1))
# INFO:root:           age     city   sex
# user_name
# Tom         18  BeiJing  male

# 获取数据的形状（4行3列）
logging.info(user_info.shape)
# INFO:root:(4, 3)
# 获取数据的转置
logging.info(user_info.T)
# INFO:root:user_name      Tom       Bob       Mary     James
# age             18        30         25        40
# city       BeiJing  ShangHai  GuangZhou  ShenZhen
# sex           male      male     female      male

# 获取它包含的原有数据（ndarray）
logging.info(user_info.values)
# INFO:root:[[18 'BeiJing' 'male']
#  [30 'ShangHai' 'male']
#  [25 'GuangZhou' 'female']
#  [40 'ShenZhen' 'male']]



'''描述与统计'''
# 数据的简单统计指标:查看年龄的最大值
logging.info(user_info.age.max())
# INFO:root:40
# 类似的，通过调用 min、mean、quantile、sum 方法可以实现最小值、平均值、中位数以及求和

# 累加求和:最后的结果就是将上一次求和的结果与原始当前值求和作为当前值
logging.info(user_info.age.cumsum())
# INFO:root:user_name
# Tom       18
# Bob       48
# Mary      73
# James    113
# Name: age, dtype: int64

# 一次性获取多个统计指标
# 总数、平均数、标准差、最小值、最大值、25%/50%/75% 分位数
logging.info(user_info.describe())
# INFO:root:             age
# count   4.000000
# mean   28.250000
# std     9.251126
# min    18.000000
# 25%    23.250000
# 50%    27.500000
# 75%    32.500000
# max    40.000000
logging.info(user_info.describe()['age']['mean'])
# INFO:root:28.25

# 查看非数字类型的列的统计指标
# 总数，去重后的个数、最常见的值、最常见的值的频数
logging.info(user_info.describe(include=['object']))
# INFO:root:             city   sex
# count           4     4
# unique          4     2
# top     GuangZhou  male
# freq            1     3

# 统计下某列中每个值出现的次数
logging.info(user_info.sex.value_counts())
# INFO:root:male      3
# female    1
# Name: sex, dtype: int64

# 获取某列最大值或最小值对应的索引idxmax idxmin 
logging.info(user_info.age.idxmax())
# INFO:root:James



'''离散化'''
