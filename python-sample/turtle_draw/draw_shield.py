#!/usr/bin/env python3

""" 用Python画个美队盾牌 """
import turtle as t
import logging

logging.basicConfig(level=logging.INFO)

# 「抬笔」->「移动画笔」->「落笔」函数
def setpen(x,y):
    # 抬笔
    t.penup()
    # 移动画笔到x,y
    t.goto(x,y)
    # 落笔
    t.pendown()
    # 未知
    t.setheading(0)

# 画盾牌
def circle(x,y,r,color):
    # 为了保证画出的圆够圆，所以我们把圆的边设置的多一些
    n=36 # by Peter: 此处3为三角形，4为正方形
    angle=360/n
    pi=3.1415926
    # 周长
    c=2*pi*r
    # 每条边的长度
    l=c/n
    # 起始位置
    start_x=x-1/2
    start_y=y+r
    # 移动画笔
    setpen(start_x,start_y)
    # 选择画笔颜色
    t.pencolor(color)
    # 选择背景色
    t.fillcolor(color)
    # 填充
    t.begin_fill()
    # t.hideturtle()
    # t.penup()
    logging.info('边数:{} 转边角度:{} 周长:{} 边长:{} x:{} y:{}'.format(n,angle,c,l,start_x,start_y))
    for i in range(n):
        # 画线
        t.forward(l)
        # 转角
        t.right(angle)
    t.end_fill()

# 画五角星(未理解)
def five_star(l):
    setpen(0, 0)
    t.setheading(162)
    # add by peter: 看画线路径
    t.pencolor('white')

    t.forward(150)
    t.setheading(0)
    t.fillcolor('WhiteSmoke')
    t.begin_fill()
    t.hideturtle()
    # add by peter: 看画线路径
    # t.penup()

    for i in range(5):
        t.forward(l)
        # 五角星的五个顶角各是36°, 180-36=144,转边角度144
        t.right(144)
    t.end_fill()

# 主函数
def shield():
    circle(0,0,300,'red')
    circle(0,0,250,'white')
    circle(0,0,200,'red')
    circle(0,0,150,'blue')
    five_star(284)

if __name__=='__main__':
    shield()
    # 结束乌龟图
    t.done()
    # 最后结果图有偏差，原因未知    
