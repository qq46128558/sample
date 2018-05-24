
""" 用 Python 脚本对图片进行清理 """

# 利用 Pillow 库，我们可以创建一个阈值过滤器来去掉渐变的背景色，只把文字留下来

from PIL import Image
import subprocess

def cleanFile(filePath,newFilePath):
    image=Image.open(filePath)

    # 对图片进行阈值过滤，然后保存 (120~143) 255是白色, 0是黑色
    image=image.point(lambda x:0 if x<120 else 255)
    image.save(newFilePath)

    # 调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(["tesseract",newFilePath,"output"])

    # 打开文件读取结果
    outputFile=open("output.txt","r")
    print(outputFile.read())
    outputFile.close()

cleanFile("text_2.png","text_2_clean.png")