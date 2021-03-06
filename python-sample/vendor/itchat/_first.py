#!/usr/bin/env python3

'微信远程控制电脑'

import itchat
import os
import time
import cv2

sendMsg=u"{消息助手}:暂时无法回复"
usageMsg=u"使用方法:\n" \
	 	 u"1.运行CMD命令:cmd xxx (xxx为命令)\n" \
		 u"-例如关机命令:\n" \
		 u"cmd shutdown -s -t 0 \n" \
		 u"2.获取当前电脑用户：cap\n" \
		 u"3.启用消息助手(默认关闭)：ast\n" \
		 u"4.关闭消息助手：astc"
# 消息助手开关
flag=0
nowTime=time.localtime()
filename = str(nowTime.tm_mday)+str(nowTime.tm_hour)+str(nowTime.tm_min)+str(nowTime.tm_sec)+".txt"


@itchat.msg_register('Text')
def text_reply(msg):
	global flag
	message=msg['Text']
	fromName=msg['FromUserName']
	toName=msg['ToUserName']

	# filehelper 文件传输助手
	if toName=="filehelper":
		if message=="cap":
			cap=cv2.VideoCapture(0)
			ret,img=cap.read()
			cv2.imwrite("weixinTemp.jpg",img)
			itchat.send('@img@%s'%u'weixinTemp.jpg','filehelper')
			cap.release()
		if message[0:3]=="cmd":
			os.system(message.strip(message[0:3]).strip(' '))
		if message=="ast":
			flag=1
			itchat.send("消息助手已开启", "filehelper")
		if message=="astc":
			flag=0
			itchat.send("消息助手已关闭", "filehelper")
	elif flag==1:
		itchat.send(sendMsg, fromName)
		myfile=open(filename,'a')
		myfile.write(message)
		myfile.write("\n")
		myfile.flush()

if __name__=='__main__':
	itchat.auto_login()
	itchat.send(usageMsg, "filehelper")
	itchat.run()