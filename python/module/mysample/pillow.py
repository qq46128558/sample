#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'just a pillow sample'
# 有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：
from PIL import Image
im=Image.open('../../../1353022505371.jpg')
print(im.format,im.size,im.mode)
# 按比例缩小10倍的size
thumbsize=tuple(map(lambda x: x/10,im.size))
im.thumbnail(thumbsize)
im.save('thumb.jpg','JPEG')

# 其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等

# 第三方库都会在Python官方的pypi.python.org网站注册
