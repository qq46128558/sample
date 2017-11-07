#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'just a pillow sample'
# 有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：
from PIL import Image,ImageFilter
im=Image.open('../../../1353022505371.jpg')
print(im.format,im.size,im.mode)
# 按比例缩小10倍的size
thumbsize=tuple(map(lambda x: x/10,im.size))
im.thumbnail(thumbsize)
im.save('thumb.jpg','JPEG')

# 其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等

# 第三方库都会在Python官方的pypi.python.org网站注册
# https://pypi.python.org/pypi

# 比如，模糊效果也只需几行代码：
im=Image.open('../../../1353022505371.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
from PIL import ImageDraw,ImageFont
import random
# 随机字母:
def rndChar():
    return chr(random.randint(65,90))
# 随机颜色1:
def rndColor1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 随机颜色1:
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
# 创建Font对象:
# 报错:OSError: cannot open resource, 需要提供字体全路径
font=ImageFont.truetype('c:/windows/fonts/Arial.ttf',36)
# 创建Draw对象:
draw=ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor1())
# 输出文字:
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
# 模糊:
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')

# 要详细了解PIL的强大功能，请请参考Pillow官方文档：
# https://pillow.readthedocs.org/


