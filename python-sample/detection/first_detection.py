#!/usr/bin/env python3

""" 10行代码实现目标检测 """
# https://github.com/OlafenwaMoses/ImageAI

""" Ⅰ. Tensorflow：pip install tensorflow
II. NumPy：pip install numpy
III. SciPy：pip install scipy
IV. OpenCV：pip install opencv-python
Ⅴ. Pillow：pip install pillow
Ⅵ. Matplotlib： pip install matplotlib
Ⅶ. H5py：pip install h5py
Ⅷ. Keras：pip install keras """

# ImageAI：pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl
# 通过此链接下载用于目标检测的 RetinaNet 模型文件。(146M)
# https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5

from imageai.Detection import ObjectDetection
import os

execution_path=os.getcwd()

detector=ObjectDetection()
# 将模型的类型设置为 RetinaNet
detector.setModelTypeAsRetinaNet()
# 将模型路径设置为 RetinaNet 模型的路径
detector.setModelPath(os.path.join(execution_path,"resnet50_coco_best_v2.0.1.h5"))
# 将模型加载到的目标检测类 
detector.loadModel()
imagename="IMG_20171001_100747.jpg"
# 调用目标检测函数，解析输入的和输出的图像路径
detections=detector.detectObjectsFromImage(input_image=os.path.join(execution_path,imagename),output_image_path=os.path.join(execution_path,'_new'.join(os.path.splitext(imagename))))

for eachObject in detections:
    # 打印出所检测到的每个目标的名称及其概率值
    print(eachObject["name"]+":"+eachObject["percentage_probability"])

# ImageAI 支持许多强大的目标检测过程。其中之一就是能够提取图像中检测到的每个目标。如下所示，通过简单地解析将 extra_detected_objects = True 变为 detectObjectsFromImage 函数，目标检测类将为图像目标创建一个新的文件夹，提取每张图像，并将每张图像保存到新创建的文件夹中，同时返回一个包含每张图像路径的额外数组。
# detections, extracted_images = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"), extract_detected_objects=True)

# ImageAI 还提供了更多功能，可用于定制和生产功能部署所需的目标检测任务。一些支持的功能如下
# - Adjusting Minimum Probability：默认情况下，检测概率低于 50% 的对象将不会显示或报告。你可以增加高确定性目标的检测概率，或者在需要检测所有可能对象的情况下降低该概率值。
# - Custom Objects Detection：使用所提供的 CustomObject 类，如此检测类函数将打印出一个或几个唯一目标的检测结果。
# - Detection Speed：通过将检测速度设置为“fast”、“faster”和“fastest”，以便缩短目标检测所需的时间。
# - Input Types：你可以指定并解析图像的文件路径，Numpy 数组或图像文件流作为输入图像
# - Output Types：你可以指定 detectObjectsFromImage 函数所返回的图像格式，可以是以文件或 Numpy 数组的形式。 