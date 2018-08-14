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
if False:
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
# 将年龄进行离散化（分桶），直白来说就是将年龄分成几个区间
logging.info(pd.cut(user_info.age,3))
# INFO:root:user_name
# Tom      (17.978, 25.333]
# Bob      (25.333, 32.667]
# Mary     (17.978, 25.333]
# James      (32.667, 40.0]
# Name: age, dtype: category
# Categories (3, interval[float64]): [(17.978, 25.333] < (25.333, 32.667] < (32.667, 40.0]]

# 自定义离散区间
logging.info(pd.cut(user_info.age,[1,18,30,50]))
# INFO:root:user_name
# Tom       (1, 18]
# Bob      (18, 30]
# Mary     (18, 30]
# James    (30, 50]
# Name: age, dtype: category
# Categories (3, interval[int64]): [(1, 18] < (18, 30] < (30, 50]]

# 给每个区间起个名字
logging.info(pd.cut(user_info.age,[1,18,30,50],labels=['childhood','youth','middle']))
# INFO:root:user_name
# Tom      childhood
# Bob          youth
# Mary         youth
# James       middle
# Name: age, dtype: category
# Categories (3, object): [childhood < youth < middle]

# qcut 是根据每个值出现的次数来进行离散化的
logging.info(pd.qcut(user_info.age,3))
# INFO:root:user_name
# Tom      (17.999, 25.0]
# Bob        (25.0, 30.0]
# Mary     (17.999, 25.0]
# James      (30.0, 40.0]
# Name: age, dtype: category
# Categories (3, interval[float64]): [(17.999, 25.0] < (25.0, 30.0] < (30.0, 40.0]]



'''排序功能'''
# 按照索引进行正序排
logging.info(user_info.sort_index())
# INFO:root:           age       city     sex
# user_name
# Bob         30   ShangHai    male
# James       40   ShenZhen    male
# Mary        25  GuangZhou  female
# Tom         18    BeiJing    male

# 按照列进行倒序排
# user_info.sort_index(axis=1, ascending=False)

# 按照年龄排序
logging.info(user_info.sort_values(by="age"))
# INFO:root:           age       city     sex
# user_name
# Tom         18    BeiJing    male
# Mary        25  GuangZhou  female
# Bob         30   ShangHai    male
# James       40   ShenZhen    male

# 按照年龄和城市来一起排序
# user_info.sort_values(by=["age", "city"])

# 获取最大的n个值或最小值的n个值
logging.info(user_info.age.nlargest(2))
# INFO:root:user_name
# James    40
# Bob      30
# Name: age, dtype: int64

# user_info.age.nsmallest(n)


'''DataFrame中取一列就是Series(Series 包含了 dict 的特点)'''

logging.info(type(user_info.age))
logging.info(type(user_info['age']))
# INFO:root:<class 'pandas.core.series.Series'>


'''函数应用'''
# map 是 Series 中特有的方法，通过它可以对 Series 中的每个元素实现转换
# apply 方法既支持 Series，也支持 DataFrame，在对 Series 操作时会作用到每个值上，在对 DataFrame 操作时会作用到所有行或所有列（通过 axis 参数控制
# applymap 方法针对于 DataFrame，它作用于 DataFrame 中的每个元素，它对 DataFrame 的效果类似于 apply 对 Series 的效果

# 通过年龄判断用户是否属于中年人（30岁以上为中年）
logging.info(user_info.age.map(lambda x: "yes" if x>=30 else "no"))
# INFO:root:user_name
# Tom       no
# Bob      yes
# Mary      no
# James    yes
# Name: age, dtype: object

# 通过城市来判断是南方还是北方
logging.info(user_info.city.map({"BeiJing": "north","ShangHai": "south","GuangZhou": "south","ShenZhen": "south"}))
# INFO:root:user_name
# Tom      north
# Bob      south
# Mary     south
# James    south
# Name: city, dtype: object

# 通过年龄判断用户是否属于中年人（30岁以上为中年）
# 对 Series 来说，apply 方法 与 map 方法区别不大。
logging.info(user_info.age.apply(lambda x: "yes" if x >= 30 else "no"))
# INFO:root:user_name
# Tom       no
# Bob      yes
# Mary      no
# James    yes
# Name: age, dtype: object

# 对 DataFrame 来说，apply 方法的作用对象是一行或一列数据（一个Series）
# axis=0 各列的max
logging.info(user_info.apply(lambda x:x.max(),axis=0)) 
# Name: age, dtype: object
# INFO:root:age           40
# city    ShenZhen
# sex         male
# dtype: object

# axis=0时, x是一列Series
logging.info(user_info.apply(lambda x:type(x),axis=0)) 
# INFO:root:age     <class 'pandas.core.series.Series'>
# city    <class 'pandas.core.series.Series'>
# sex     <class 'pandas.core.series.Series'>
# dtype: object

# axis=1时, x是一行Series
logging.info(user_info.apply(lambda x:type(x),axis=1)) 
# INFO:root:user_name
# Tom      <class 'pandas.core.series.Series'>
# Bob      <class 'pandas.core.series.Series'>
# Mary     <class 'pandas.core.series.Series'>
# James    <class 'pandas.core.series.Series'>
# dtype: object

# 所有值转为小写
logging.info(user_info.applymap(lambda x:str(x).lower()))
# INFO:root:          age       city     sex
# user_name
# Tom        18    beijing    male
# Bob        30   shanghai    male
# Mary       25  guangzhou  female
# James      40   shenzhen    male


'''修改列/索引名称'''
# 修改列名
logging.info(user_info.rename(columns={"age":"Age","city":"City","sex":"Sex"}))
# INFO:root:           Age       City     Sex
# user_name
# Tom         18    BeiJing    male
# Bob         30   ShangHai    male
# Mary        25  GuangZhou  female
# James       40   ShenZhen    male

# 修改索引名
logging.info(user_info.rename(index={"Tom":"tom"}))
# INFO:root:           age       city     sex
# user_name
# tom         18    BeiJing    male
# Bob         30   ShangHai    male
# Mary        25  GuangZhou  female
# James       40   ShenZhen    male

'''类型操作'''
# 获取每种类型的列数
logging.info(user_info.get_dtype_counts())
# INFO:root:int64     1
# object    2
# dtype: int64

# 转换数据类型
logging.info(user_info.age.astype(float))
# INFO:root:user_name
# Tom      18.0
# Bob      30.0
# Mary     25.0
# James    40.0
# Name: age, dtype: float64

# 常见的有转为数字、日期、时间差，Pandas 中分别对应 to_numeric、to_datetime、to_timedelta 方法
user_info['height']=["178", "168", "178", "180cm"]
# 强转失败时将有问题的元素赋值为NaN
logging.info(pd.to_numeric(user_info.height,errors='coerce'))
# INFO:root:user_name
# Tom      178.0
# Bob      168.0
# Mary     178.0
# James      NaN
# Name: height, dtype: float64

# 强转失败时返回原有的数据
logging.info(pd.to_numeric(user_info.height,errors='ignore'))
# INFO:root:user_name
# Tom        178
# Bob        168
# Mary       178
# James    180cm
# Name: height, dtype: object

