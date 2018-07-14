#!/usr/bin/env python3

""" matplotlib pyplot应用 """

import matplotlib.pyplot as plt

# 修正中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'

# 饼图
# 数据 autopct='%2.2f%%'(2位小数)
plt.pie([568,1200,38,124],labels=['集团','南区','中区','离岸'],labeldistance=1.1,autopct='%d%%')
# 使饼图为正圆形 
plt.axis('equal')
# 图例
plt.legend(loc='upper left',bbox_to_anchor=(-0.1,1))
# 标题
plt.title(u'饼图示例数据')
# 保存文件
plt.savefig('pie_chart.jpg')
# 弹窗显示
plt.show()