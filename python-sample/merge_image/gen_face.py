#!/usr/bin/env python3

'Python自动生成表情包'

__author__='Python雁横'

from PIL import Image,ImageDraw,ImageFont

myimage=Image.open('head.jpg')
face=Image.open('face.jpg')
# 把表情叠加到模板上
myimage.paste(face,(int(myimage.width/2-face.width/2),30))
# myimage.show()

# 文字叠加
draw=ImageDraw.Draw(myimage)
font=ImageFont.truetype('simhei.ttf',20)
fontstring="尴尬而不失礼貌的微笑"
# 往图层里输入文字
draw.text((10,myimage.height-30),fontstring,filt=(0,0,0),font=font)
# myimage.show()
myimage.save('./result.jpg')