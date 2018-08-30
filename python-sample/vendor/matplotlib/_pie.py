#!/usr/bin/env python3
# 画饼图用的库
import matplotlib.pyplot as plt

# 微信中性别字段的取值有Unkonw、Male和Female三种，其对应的数值分别为0、1、2。
# 设置绘图对象的大小
plt.figure(figsize=(8,8))
# 参数设置这个饼为正圆
plt.axes(aspect=1)

plt.pie(
	[7,87,38], 	# 性别统计结果
	labels=['未知','男','女'],		# 设置饼图的标签
	colors=['red','blue','coral'],	# 饼图区域配色
	explode=[0,0,0.1],				# 凸出部分 0.1 凸出这部分，female
	labeldistance=1.1,				# 标签距离圆点距离，1.1指1.1倍半径的位置
	autopct='%3.1f%%',				# 饼图区域文本格式,%3.1f%%表示小数有三位，整数有一位的浮点数
	shadow=False,					# 饼图是否显示阴影
	startangle=90,			# 起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
	pctdistance=0.6,		# 饼图区域文本距离圆点距离
	)
# 图例
plt.legend(loc='upper left',bbox_to_anchor=(-0.1,1))
# 解决 Windows 环境下乱码问题
# font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15) 
# plt.title(u'微信好友性别比例', fontproperties=font_set)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.title(u'微信好友性别比例')
plt.savefig('pie_chart_wechat.jpg')
plt.show()