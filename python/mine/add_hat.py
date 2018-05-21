#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 安装numpy
# 安装opencv_python-3.4.1+contrib-cp35-cp35m-win_amd64.whl
# 安装cmake
# 安装dlib

import numpy as np
import cv2
import dlib

# 给img中的头像加上圣诞帽,人脸最好为正脸
def add_hat(img,hat_img):
    # 分离rgba通道，合成rgb三通道帽子图，a通道后面做mask用
    r,g,b,a=cv2.split(hat_img)
    rgb_hat=cv2.merge((r,g,b))
    cv2.imwrite("hat_alpha.jpg",a)
    # ------------------------- 用dlib的人脸检测代替OpenCV的人脸检测-----------------------
    # # 灰度变换
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    # # 用opencv自带的人脸检测器检测人脸
    # face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")                       
    # faces = face_cascade.detectMultiScale(gray,1.05,3,cv2.CASCADE_SCALE_IMAGE,(50,50))

    # ------------------------- 用dlib的人脸检测代替OpenCV的人脸检测-----------------------
    # dlib人脸关键点检测器
    predictor_path="shape_predictor_5_face_landmarks.dat"
    predictor=dlib.shape_predictor(predictor_path)
    # dlib正脸检测器
    detector=dlib.get_frontal_face_detector()
    # 正脸检测
    dets=detector(img,1)
    # 如果检测到人脸
    if len(dets)>0:
        

# 读取帽子图，第二个参数-1表示读取为rgba通道，否则为rgb通道
hat_img=cv2.imread("hat2.png",-1)

output=add_hat("",hat_img)

