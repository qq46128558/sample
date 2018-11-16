#!/usr/bin/env python3

"""快速入门画图神器 Matplotlib"""

import logging
# 导入相关模块
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.ERROR)

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

if __name__=='__main__':
    # 通过dict实现switch
    sample={1:draw1,2:draw2,3:draw3}

    sample.get(1)()
    plt.show()
