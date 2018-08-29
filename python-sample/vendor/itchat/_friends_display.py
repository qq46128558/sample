#!/usr/bin/env python3

'分析微信好友信息'

# 登陆微信，获取朋友信息的库
import itchat
# # 计数用的库
# import collections
# # 画饼图用的库
# import matplotlib.pyplot as plt
# # 解决图片中文乱码
# from matplotlib.font_manager import FontProperties
# # 画地图用的库
# from pyecharts import Map
# from pyecharts import Geo

# 全球国家地图: echarts-countries-pypkg (1.9MB): 世界地图和 213 个国家，包括中国地图
# pip install echarts-countries-pypkg    
# 中国省级地图: echarts-china-provinces-pypkg (730KB)：23 个省，5 个自治区
# pip install echarts-china-provinces-pypkg 
# 中国市级地图: echarts-china-cities-pypkg (3.8MB)：370 个中国城市
# pip install echarts-china-cities-pypkg  
# 中国县区级地图: echarts-china-counties-pypkg (4.1MB)：2882 个中国县·区
# pip install echarts-china-counties-pypkg 
# 中国区域地图: echarts-china-misc-pypkg (148KB)：11 个中国区域地图，比如华南、华北
# pip install echarts-china-misc-pypkg   

# 登陆微信网页版(使用手机扫描二维码就可以登录)
itchat.login()
# 获取当前微信好友信息
# 返回的 friends 是一个集合，第一个元素是当前用户，也就是你自己，集合中的每一个元素都是一个字典结构，可以注意到这里有Sex、City、Province、NickName、Signature等
friends=itchat.get_friends(update=True)[0:]

# 由于 friends 集合里第一个表示的是自己，所以我们从第二个开始获取
# 微信中性别字段的取值有Unkonw、Male和Female三种，其对应的数值分别为0、1、2。
# 我们将会得到如 sexs = [1,0,1,0,1,0,1,0,2,1,1,2,1] 的集合
sexs=list(map(lambda x:x['Sex'],friends[1:]))

sex_counts=[0,1,2]
# 通过Collection模块中的Counter()对这三种不同的取值进行统计
sex=collections.Counter(sexs)
# 性别统计结果
