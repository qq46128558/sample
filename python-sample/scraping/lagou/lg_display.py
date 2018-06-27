#!/usr/bin/env python3


""" 爬取拉勾网职位并分析 """
from pylab import mpl
import pandas as pd
import logging
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread
import statsmodels.api as sm

logging.basicConfig(level=logging.ERROR)


# 使matplotlib模块能显示中文
mpl.rcParams['font.sans-serif']=['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus']=False    # 解决保存图像是负号'-'显示为方块的问题

# 读取数据  
df=pd.read_csv('lagou-jobs.csv',encoding='gb18030')

# 数据清洗,剔除实习岗位
logging.info(df[df['职位名称'].str.contains('实习')].index)
logging.info(df[df['职位名称'].str.contains('外包')].index)
# inplace=True：不创建新的对象，直接对原始对象进行修改；
# inplace=False：对数据进行修改，创建并返回新的对象承载其修改结果。
df.drop(df[df['职位名称'].str.contains('实习')].index,inplace=True)
df.drop(df[df['职位名称'].str.contains('外包')].index,inplace=True)
logging.info(df.describe())

# 工作经验
# 由于CSV文件内的数据是字符串形式,先用正则表达式将字符串转化为列表,再取区间的均值
pattern='\d+'
# logging.info(df['工作经验'].str.findall(pattern))
df['工作年限']=df['工作经验'].str.findall(pattern)
avg_work_year=[]
for i in df['工作年限']:
    # i:['1','3']
    # 如果工作经验为'不限'或'应届毕业生',那么匹配值为空,工作年限为0
    if len(i)==0:
        avg_work_year.append(0)
    # 如果匹配值为一个数值,那么返回该数值 
    elif len(i)==1:
        avg_work_year.append(int(''.join(i)))
    # 如果匹配值为一个区间,那么取平均值
    else:
        # logging.info(sum(list(map(int,i)))/len(i))
        avg_work_year.append(sum(list(map(int,i)))/len(i))
df['经验']=avg_work_year

# 工资
# 将字符串转化为列表,再取区间的前25%，比较贴近现实
df['salary']=df['工资'].str.findall(pattern)
avg_salary=[]
for i in df['salary']:
    # i:['10','20']
    f=lambda n,m:n+(m-n)/4
    # print(f(*list(map(int,i))))
    avg_salary.append(f(*map(int,i)))
df['月薪']=avg_salary

# 将清洗后的数据保存,以便检查 
df.to_csv('draft.csv',index=False,encoding='gb18030')

# 描述统计 
logging.info('PHP开发工资描述:\n{}'.format(df['月薪'].describe()))
# INFO:root:PHP开发工资描述:
# count    447.000000 合计
# mean      13.253915 均值
# std        4.528697
# min        3.750000 最小
# 25%        9.750000 地位
# 50%       12.500000 中位
# 75%       16.250000 高位
# max       31.250000 最大
# Name: 月薪, dtype: float64

# 绘制频率直方图并保存 
if False:
    plt.hist(df['月薪'],bins=12)
    plt.xlabel('工资(k)')
    plt.ylabel('频数')
    plt.title('工资直方图')
    plt.savefig('histogram.jpg')
    plt.show()

# 绘制饼图并保存
if False:
    logging.info(df['区域'].value_counts())
    count=df['区域'].value_counts()
    # 将龙华区和龙华新区的数据汇总
    try:
        count['龙华新区']+=count['龙华区']
        del count['龙华区']
    except Exception as e:
        logging.info(e)

    plt.pie(count,labels=count.keys(),labeldistance=1.4,autopct='%2.1f%%')
    plt.axis('equal')   # 使饼图为正圆形 
    plt.legend(loc='upper left',bbox_to_anchor=(-0.1,1))
    plt.savefig('pie_chart.jpg')
    plt.show()

# 绘制词云,将职位福利中的字符串汇总
if False:
    text=''
    for line in df['职位福利']:
        text+=line
    # stopwords
    text=text.replace('福利','').replace('PHP','')

    # 使用jieba模块将字符串分割为单词列表  
    cut_text=' '.join(jieba.cut(text))
    color_mask=imread('2018-06-27_8-55-24.png')   #设置背景图
    cloud = WordCloud(  
            font_path = 'simhei.ttf',             #'yahei.ttf',   
            background_color = 'white',  
            mask = color_mask,  
            max_words = 1000,  
            max_font_size = 100          
            )  
    word_cloud=cloud.generate(cut_text)
    # 从背景图片生成颜色值
    # 重新上色
    word_cloud.recolor(color_func=ImageColorGenerator(color_mask))
    # 保存词云图片
    word_cloud.to_file('word_cloud.jpg')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()

# 实证统计,将学历不限的职位要求认定为最低学历:大专
df['学历要求']=df['学历要求'].replace('不限','大专')
# 学历分为大专\本科\硕士,将它们设定为虚拟变量(按我理解是行转列呈现)
# 大专 本科 硕士
#   1   0   0
dummy_edu = pd.get_dummies(df['学历要求'],prefix = '学历') 
# logging.info(dummy_edu)
# 构建回归数组(按我理解是拼列)
df_with_dummy = pd.concat([df['月薪'],df['经验'],dummy_edu],axis = 1)
# logging.info(df_with_dummy)

# 得工资与工作经验、学历的关系
# 建立多元回归模型 (未理解)
y = df_with_dummy['月薪']  
x = df_with_dummy[['经验','学历_大专','学历_本科','学历_硕士']]  
x=sm.add_constant(x)   
model = sm.OLS(y,x)  
results = model.fit()  
print('回归方程的参数：\n{}\n'.format(results.params))  
print('回归结果：\n{}'.format(results.summary()))