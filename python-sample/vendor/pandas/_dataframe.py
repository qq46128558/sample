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
