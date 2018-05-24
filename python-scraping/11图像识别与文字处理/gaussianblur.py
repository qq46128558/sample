
""" 像素级的变换操作处理图片 """

from PIL import Image,ImageFilter

kitten=Image.open("07_01 290x293.jpg")
blurkitten=kitten.filter(ImageFilter.GaussianBlur)
blurkitten.save("blur.jpg")
blurkitten.show()