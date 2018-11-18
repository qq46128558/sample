#!/usr/bin/env python3

"""快速入门画图神器 Matplotlib"""

import logging
# 导入相关模块
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.INFO)

# 首先通过 np.linspace 方式生成 x，它包含了 50 个元素的数组，这 50 个元素均匀的分布在 [0, 2pi] 的区间上。然后通过 np.sin(x) 生成 y。
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)

# 画一个简单的图形
def draw1():
    # 设置 figure
    # 你可以认为Matplotlib绘制的图形都在一个默认的 figure 中，当然了，你可以自己创建 figure，好处就是可以控制更多的参数，常见的就是控制图形的大小，这里创建一个 figure，设置大小为 (6, 3)。
    plt.figure(figsize=(6,3))

    # 有了 x 和 y 数据之后，我们通过 plt.plot(x, y) 来画出图形，并通过 plt.show() 来显示。
    # 绘制出图形之后，我们可以自己调整更多的样式，比如颜色、点、线
    # 比如 'y*-' ，其中 y 表示黄色，* 表示 星标的点，- 表示实线。
    plt.plot(x,y,'y*-',label='sin(x)')

    # 有时候，可能需要在一个图纸里绘制多个图形，这里我们同时绘制了 (x, y), (x, y * 2)两个图形。
    plt.plot(x,y*2,'m--',label='2sin(x)') 
    # 蓝色b绿色g红色r青色c品红m黄色y黑色k白色w
    # 点.像素,圆o方形s三角形^
    # 直线-虚线--点线:点划线-.

    # 设置legend(配合label才有显示)
    plt.legend(loc='best')
    
    # 设置标题
    plt.title("sin(x) & 2sin(x)")
    
    

# 设置坐标轴
def draw2():
    draw1()
    # 通过 xlim 和 ylim 来设限定轴的范围，通过 xlabel 和 ylabel 来设置轴的名称。
    plt.xlim(0,np.pi+1)
    plt.ylim(-3,3)
    plt.xlabel('X')
    plt.ylabel('Y')

# 可以通过 xticks 和 yticks 来设置轴的刻度
def draw3():
    draw1()
    plt.xticks((0,np.pi*0.5,np.pi,np.pi*1.5,np.pi*2))
    plt.yticks((-2.0,-1.5,-1.0,-0.5,0,0.5,1.0,1.5,2))

# 添加注释
def draw4():
    plt.plot(x,y)
    x0=np.pi
    y0=0
    # 画出标注点
    plt.scatter(x0,y0,s=50)
    # 'sin(np.pi)=%s' % y0 代表标注的内容，可以通过字符串 %s 将 y0 的值传入字符串；
    # 参数 xycoords='data' 是说基于数据的值来选位置;
    # xytext=(+30, -30) 和 textcoords='offset points' 表示对于标注位置的描述 和 xy 偏差值，即标注位置是 xy 位置向右移动 30，向下移动30；
    # arrowprops 是对图中箭头类型和箭头弧度的设置，需要用 dict 形式传入。
    plt.annotate('sin(np.ni)=%s'%y0,xy=(np.pi,0),xycoords='data',xytext=(+30,-30),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
    # 也可以使用 plt.text 函数来添加注释
    # plt.text(0.5, -0.25, "sin(np.pi) = 0", fontdict={'size': 16, 'color': 'r'})

# 使用子图
def draw5():
    # 有时候我们需要将多张子图展示在一起，可以使用 subplot() 实现。即在调用 plot() 函数之前需要先调用 subplot() 函数。
    ax1=plt.subplot(2,2,1) # （行，列，活跃区）
    plt.plot(x,np.sin(x),'r')
    plt.subplot(2,2,2,sharey=ax1) # 与 ax1 共享y轴
    plt.plot(x,2*np.sin(x),'g')
    ax2=plt.subplot(2,2,3)
    plt.plot(x,np.cos(x),'b')
    plt.subplot(2,2,4,sharey=ax2)
    plt.plot(x,2*np.cos(x),'y')
    # 上面的 subplot(2, 2, x) 表示将图像窗口分为 2 行 2 列。x 表示当前子图所在的活跃区。

# 有时候我们需要不同大小的子图
def draw6():
    plt.subplot(2,1,1) # （行，列，活跃区）
    plt.plot(x,np.sin(x),'r')
    # 解释下为什么活跃区为 4，因为上一步中使用 plt.subplot(2, 1, 1) 将整个图像窗口分为 2 行 1 列, 第1个小图占用了第1个位置, 也就是整个第1行. 这一步中使用 plt.subplot(2, 3, 4) 将整个图像窗口分为 2 行 3 列, 于是整个图像窗口的第1行就变成了3列, 也就是成了3个位置, 于是第2行的第1个位置是整个图像窗口的第4个位置。
    ax1=plt.subplot(2,3,4)
    plt.plot(x,2*np.sin(x),'g')
    plt.subplot(2,3,5,sharey=ax1)
    plt.plot(x,np.cos(x),'b')
    plt.subplot(2,3,6,sharey=ax1)
    plt.plot(x,2*np.cos(x),'y')

# 散点图
def colorbar():
    k=500
    x=np.random.rand(k)
    y=np.random.rand(k)
    logging.info(x[:10])
    # INFO:root:[0.39439996 0.6414791  0.71569981 0.30267446 0.15495104 0.38977327 0.41445457 0.97683185 0.19737104 0.62186213]
    logging.info(y[:10])
    # INFO:root:[0.13488103 0.13076497 0.49393922 0.94226616 0.81893848 0.94828212 0.736714   0.75390657 0.74986627 0.61326751]
    size=np.random.rand(k)*50 # 生成每个点的大小
    colour=np.arctan2(x,y) # 生成每个点的颜色大小
    plt.scatter(x,y,s=size,c=colour)
    plt.colorbar() # 添加颜色栏
    # 上面我们首先生成了要绘制的数据的点x 和 y，接下来为每个数据点生成控制大小的数组 size，然后未每个数据点生成控制颜色的数组 colour。最后通过 colorbar() 来增加一个颜色栏。

# 柱状图
def bar():
    k=10
    x=np.arange(k)
    logging.info(x)
    # INFO:root:[0 1 2 3 4 5 6 7 8 9]
    y=np.random.rand(k)
    logging.info(y)
    # INFO:root:[0.88245081 0.03883995 0.94164021 0.02237071 0.80930982 0.93510309 0.03257937 0.01406703 0.30612616 0.02356784]
    plt.bar(x,y) # 画出 x 和 y 的柱状图
    # 增加数值
    for x,y in zip(x,y):
        plt.text(x,y,'%0.2f'%y,ha='center',va='bottom')
    # 生成数据 x 和 y 之后，调用 plt.bar 函数绘制出柱状图，然后通过 plt.text 标注数值，设置参数 ha='center' 横向居中对齐，设置 va='bottom'纵向底部（顶部）对齐。

# 中文乱码解决(曲线图示侠)
def chinese():
    # Matplotlib 有个让人恼火的问题是，默认情况下，Matplotlib 中文会乱码。
    x = ['北京', '上海', '深圳', '广州']
    y = [60000, 58000, 50000, 52000]
    # 其实只需要配置下后台字体即可
    plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    plt.plot(x, y)

if __name__=='__main__':
    # 通过dict实现switch
    sample={1:draw1,2:draw2,3:draw3,4:draw4,5:draw5,6:draw6}
    shape={1:colorbar,2:bar,3:chinese}

    # 修改get值调用不同方法
    # sample.get(6)()
    shape.get(3)()

    plt.show()
