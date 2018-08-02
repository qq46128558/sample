#!/usr/bin/env python3

'Pandas 常用的数据结构有两种：Series 和 DataFrame。这些数据结构构建在 Numpy 数组之上，这意味着它们效率很高。'

# 导入相关库
import logging
import numpy as np
import pandas as pd

logging.basicConfig(level=logging.ERROR)

""" Series 是一个带有 名称 和索引的一维数组 """

# 存储了 4 个年龄：18/30/25/40
user_age=pd.Series(data=[18,30,25,40])
logging.info(user_age)
# INFO:root:0    18
# 1    30
# 2    25
# 3    40
# dtype: int64

# 利用index构建年龄对应用户名
user_age.index=["Tom","Bob","Mary","James"]
logging.info(user_age)
# INFO:root:Tom      18
# Bob      30
# Mary     25
# James    40
# dtype: int64

# 为 index 起个名字
user_age.index.name="user_name"
logging.info(user_age)
# INFO:root:user_name
# Tom      18
# Bob      30
# Mary     25
# James    40
# dtype: int64

# 给 Series 起个名字
user_age.name="用户年龄信息"
logging.info(user_age)
# INFO:root:user_name
# Tom      18
# Bob      30
# Mary     25
# James    40
# Name: 用户年龄信息, dtype: int64

""" 一个 Series 包括了 data、index 以及 name """

# 快速实现上面的功能
index=pd.Index(["Tom", "Bob", "Mary", "James"], name="user_name")
user_age=pd.Series(data=[18, 30, 25, 40],index=index,name="用户年龄信息")
print(user_age)
# user_name
# Tom      18
# Bob      30
# Mary     25
# James    40
# Name: 用户年龄信息, dtype: int64

# 自己手动指定数据类型
user_age=pd.Series(data=[18, 30, 25, 40],index=index,name="用户年龄信息",dtype=float)
logging.info(user_age)
# INFO:root:user_name
# Tom      18.0
# Bob      30.0
# Mary     25.0
# James    40.0
# Name: 用户年龄信息, dtype: float64


""" Series 包含了 dict 的特点，也就意味着可以使用与 dict 类似的一些操作。我们可以将 index 中的元素看成是 dict 中的 key。 """
# 获取 Tom 的年龄
logging.info(user_age["Tom"])
# INFO:root:18.0

# 可以通过 get 方法来获取。通过这种方式的好处是当索引不存在时，不会抛出异常
logging.info(user_age.get("Tom"))
# INFO:root:18.0


""" 切片操作 """
# 获取第一个元素
logging.info(user_age[0])
# INFO:root:18.0

# 获取前三个元素
logging.info(user_age[:3])
# INFO:root:user_name
# Tom     18.0
# Bob     30.0
# Mary    25.0
# Name: 用户年龄信息, dtype: float64

# 获取年龄大于30的元素
logging.info(user_age[user_age>30])
# INFO:root:user_name
# James    40.0
# Name: 用户年龄信息, dtype: float64

# 获取第4个和第二个元素
print(user_age[[3,1]])
# user_name
# James    40.0
# Bob      30.0
# Name: 用户年龄信息, dtype: float64


""" 向量化操作 """
print(user_age+1)
# user_name
# Tom      19.0
# Bob      31.0
# Mary     26.0
# James    41.0
# Name: 用户年龄信息, dtype: float64


print(np.exp(user_age))
# user_name
# Tom      6.565997e+07
# Bob      1.068647e+13
# Mary     7.200490e+10
# James    2.353853e+17
# Name: 用户年龄信息, dtype: float64
