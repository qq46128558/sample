#!/usr/bin/env python3


""" 识别图像中的面部 """
# 使用了Adam Geitgey的深度学习Python模块face_recognition
# 已经给数据集中的每张图像建好了128维面部嵌入，我们可以用OpenCV、Python和深度学习进行面部识别了

# USAGE
# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png 

# import the necessary packages
# face_recognition模块完成主要工作
import face_recognition
# argparse处理运行时传递的命令行参数
import argparse
import pickle
# OpenCV负责加载图像、转换图像，并显示处理之后的图像
import cv2
import logging


logging.basicConfig(level=logging.INFO)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
# --encodings：包含面部编码的pickle文件的路径；
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
# --image：需要进行面部识别的图像；
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
# --detection-method：这个选项应该很熟悉了。可以根据系统的能力，选择hog或cnn之一。追求速度的话就选择hog，追求准确度就选择cnn。
# 注意：在树莓派上必须选择hog，因为内存容量不足以运行CNN方法。
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())


# 加载计算好的编码和面部名称，然后为输入图像构建128维面部编码
# load the known faces and embeddings
print("[INFO] loading encodings...")
# 从硬盘加载pickle过的编码和名字数据
data = pickle.loads(open(args["encodings"], "rb").read())

# load the input image and convert it from BGR to RGB
# 加载输入图像image，并转换其颜色通道顺序（同encode_faces.py脚本一样），保存到rgb中
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# detect the (x, y)-coordinates of the bounding boxes corresponding
# to each face in the input image, then compute the facial embeddings
# for each face
print("[INFO] recognizing faces...")
# 继续检测输入图像中的所有面部，并计算它们的128维encodings
# （这些代码也应该很熟悉了）encode_faces.py
boxes = face_recognition.face_locations(rgb,
	model=args["detection_method"])
encodings = face_recognition.face_encodings(rgb, boxes)
# boxes encodings => boxes names

# initialize the list of names for each face detected
# 初始化一个列表names，用来保存每个检测的面部
names = []

# loop over the facial embeddings
# 遍历面部编码encodings列表
# 开始遍历根据输入图像计算出的面部编码(有可能多个人脸)
for encoding in encodings:
	# attempt to match each face in the input image to our known
	# encodings
	# 见证面部识别的奇迹
	# 利用face_recognition.compare_faces将输入图像中的每个面部（encoding）对应到已知的编码数据集（保存在data["encodings"]中）上
	# 该函数会返回一个True/False值的列表，每个值对应于数据集中的一张图像
	# 对于我们的侏罗纪公园的例子，数据集中有218张图像，因此返回的列表将包含218个布尔值
	matches = face_recognition.compare_faces(data["encodings"],
		encoding)
	# compare_faces函数内部会计算待判别图像的嵌入和数据集中所有面部的嵌入之间的欧几里得距离
	# 如果距离位于容许范围内（容许范围越小，面部识别系统就越严格），则返回True，表明面部吻合。否则，如果距离大于容许范围，则返回False表示面部不吻合。

	""" 本质上我们用了个更”炫酷“的k-NN模型进行分类。具体的实现细节可以参考compare_faces的实现（https://github.com/ageitgey/face_recognition/blob/master/face_recognition/api.py#L213） """
	
	# 最终，name变量会的值就是人的名字。如果没有任何”投票“，则保持"Unknown"不变
	name = "Unknown"

	# 根据matches列表，可以计算每个名字的”投票“数目（与每个名字关联的True值的数目），计票之后选择最适合的人的名字：
	# check to see if we have found a match
	# 如果matches中包含任何True的投票，则需要确定True值在matches中的索引位置
	if True in matches:
		# find the indexes of all matched faces then initialize a
		# dictionary to count the total number of times each face
		# was matched
		# 通过建立一个简单的matchedIdxs列表实现:确定True值在matches中的索引位置
		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		# sample: [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75]

		# 初始化一个名为counts的字典，其键为角色的名字，值是投票的数量
		counts = {}

		# loop over the matched indexes and maintain a count for
		# each recognized face face
		# 遍历matchedIdxs，统计每个相关的名字，并在counts增加相应的计数值
		for i in matchedIdxs:
			name = data["names"][i]
			counts[name] = counts.get(name, 0) + 1
			# sample:{'ian_malcolm': 40}

		logging.info(counts)
		# determine the recognized face with the largest number of
		# votes (note: in the event of an unlikely tie Python will
		# select first entry in the dictionary)
		# 取出counts中投票最高的名字
		name = max(counts, key=counts.get)
	
	# update the list of names
	names.append(name)

# 循环每个人的边界盒和名字，然后将名字画在输出图像上以供展示之用
# loop over the recognized faces
# 开始循环检测到的面部边界盒boxes和预测的names
# 我们调用了zip(boxes, names)以创建一个容易进行循环的对象，每次迭代将得到一个二元组，从中可以提取边界盒坐标和名字
for ((top, right, bottom, left), name) in zip(boxes, names):
	# draw the predicted face name on the image
	# 利用边界盒坐标画一个绿色方框
	cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
	# 利用坐标计算了人名文本的显示位置,如果边界盒位于图像顶端，则将文本移到边界盒下方
	y = top - 15 if top - 15 > 15 else top + 15
	# 并将人名的文本画在图像上
	cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
		0.75, (0, 255, 0), 2)

# show the output image
# 显示图像，直到按下任意键为止
cv2.imshow("Image", image)
cv2.waitKey(0)

# 运行该脚本，同时至少提供两个命令行参数。如果选择HoG方式，别忘了传递--detection-method hog（否则默认会使用深度学习检测方式）
# python recognize_faces_image.py --encodings encodings.pickle --image examples/mmexport1506238138243.jpg