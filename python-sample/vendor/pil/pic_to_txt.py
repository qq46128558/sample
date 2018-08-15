#!/usr/bin/env python3

'图片转字符画'

# 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像
# 可以使用灰度值公式将像素的 RGB 值映射到灰度值
# gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

# 创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号

import logging
# PIL 是一个 Python 图像处理库
from PIL import Image

logging.basicConfig(level=logging.INFO)

#  是我们的字符画所使用的字符集，一共有 70 个字符，字符的种类与数量可以自己根据字符画的效果反复调试的
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 字符画的宽高 (宽在原来的比例值上再增加1~1.5倍,如原来是290:293)
WIDTH=115
HEIGHT=50

# 将256灰度映射到70个字符上，也就是RGB值转字符的函数：
# alpha透明度
def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    length=len(ascii_char)
    # 计算灰度
    gray=int(0.2126*r+0.7152*g+0.0722*b)
    # by peter: +1未理解(验证不+1也正常)
    unit=(256.0+1)/length
    # 不同的灰度对应着不同的字符
    # 通过灰度来区分色块
    return ascii_char[int(gray/unit)]

if __name__=='__main__':
    # img='../../../1353022505371.jpg'
    img="./07_01 290x293.jpg"
    im=Image.open(img)
    # 不改变图像大小的话太大看不出来
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)
    # WIDTH=im.width
    # HEIGHT=im.height
    txt=""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # 获得相应的字符
            txt+=get_char(*im.getpixel((j,i)))
        # 一行像素对应的灰度字符获取完成,换行
        txt+="\n"
    # 打印出字符画
    print(txt)
    # 将字符画 写入文件中
    with open('output.txt','w') as f:
        f.write(txt)
