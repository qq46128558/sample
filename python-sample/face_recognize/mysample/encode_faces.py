
#!/usr/bin/env python3

""" 用OpenCV和深度学习对面部进行编码 """
""" 该脚本用来进行面部编码（128维向量） """


# pip install dlib
# pip install face_recognition
# pip install imutils

# import the necessary packages
from imutils import paths
import face_recognition
# argparse处理运行时传递的命令行参数
import argparse
# Create portable serialized representations of Python objects.
import pickle
import cv2
import os

# 首先利用argparse分析命令行参数，在命令行上执行Python程序时，可以在终端中给脚本提供格外的信息
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to input directory of faces + images")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())
# --dataset：数据集的路径（利用search_bing_api.py创建的数据集）；
# --encodings：面部编码将被写到该参数所指的文件中；
# --detection-method：首先需要检测到图像中的面部，才能对其进行编码。两种面部检测方法为hog或cnn，因此该参数只接受这两个值。


# 现在参数已经定义好了，我们可以获得数据集文件的路径了（同时进行两个初始化）
# grab the paths to the input images in our dataset
print("[INFO] quantifying faces...")
# 用输入数据集的路径，建立了一个列表imagePaths。
imagePaths = list(paths.list_images(args["dataset"]))

# 我们还需要在循环开始之前初始化两个列表，分别是knownEncodings和knownNames。这两个列表分别包含面部编码数据和数据集中相应人物的名字
# initialize the list of known encodings and known names
knownEncodings = []
knownNames = []

# 依次循环侏罗纪公园中的每个角色
# 这段代码会循环218次，处理数据集中的218张面部图像
# 在所有图像路径中进行循环
# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
	# extract the person name from the image path
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
    # 从imagePath中提取人物的名字（因为子目录名就是人物名）
	name = imagePath.split(os.path.sep)[-2]

    # 然后将imagePath传递给cv2.imread，读取图像保存到image中
	# load the input image and convert it from RGB (OpenCV ordering)
	# to dlib ordering (RGB)
	image = cv2.imread(imagePath)
    # OpenCV中的颜色通道排列顺序为BGR，但dlib要求的顺序为RGB。由于face_recognition模块使用了dlib，因此在继续下一步之前，转换了颜色空间，并将转换后的新图像保存在rgb中。
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)




    # 定位面部位置并计算编码
    # 每次循环都会检测一个面部图像（或者一张图像中有多个面部，我们假设这些面部都属于同一个人，但如果你使用自己的图像的话，这个假设有可能不成立，所以一定要注意）
	# detect the (x, y)-coordinates of the bounding boxes
	# corresponding to each face in the input image
    # 查找面部位置，返回一个包含了许多方框的列
    # 我们给face_recognition.face_locations方法传递了两个参数：rgb：RGB图像；model：cnn或hog（该值包含在命令行参数字典中，赋给了detection_method键）。CNN方法比较准确，但速度较慢；HOG比较快，但不太准确
	boxes = face_recognition.face_locations(rgb,
		model=args["detection_method"])

	# compute the facial embedding for the face
    # 我们要将rgb的面部的边界盒boxes转换成128个数字
    # 这个步骤就是将面部编码成向量，可以通过face_recognition.face_encodings方法实现
	encodings = face_recognition.face_encodings(rgb, boxes)

    # 接下来秩序将人物的encoding和name添加到恰当的列表中（knownEncodings或knownNames）。
	# loop over the encodings
	for encoding in encodings:
		# add each encoding + name to our set of known names and
		# encodings
		knownEncodings.append(encoding)
		knownNames.append(name)

# 提取这些编码encodings的目的就是要在另一个脚本中利用它们进行面部识别
# dump the facial encodings + names to disk
print("[INFO] serializing encodings...")
# 构建了一个字典，它包含encodings和names两个键
data = {"encodings": knownEncodings, "names": knownNames}
# 将名字和编码保存到硬盘中，供以后使用
f = open(args["encodings"], "wb")
f.write(pickle.dumps(data))
f.close()

# 要创建面部嵌入，可以从终端执行以下命令
# python encode_faces.py --dataset dataset --encodings encodings.pickle
# 在我的Macbook Pro上（没有GPU），编码218张图像需要21分20秒。

# 如果你有GPU并且编译dlib时选择了支持GPU，那么速度应该会快得多
# 安装有GPU支持的dlib（可选）
# $ workon <your env name here> # optional
# $ git clone https://github.com/davisking/dlib.git
# $ cd dlib
# $ mkdir build
# $ cd build
# $ cmake .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1
# $ cmake --build .
# $ cd ..
# $ python setup.py install --yes USE_AVX_INSTRUCTIONS --yes DLIB_USE_CUDA