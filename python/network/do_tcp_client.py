#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'TCP编程'
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1',9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
# 我们需要打开两个命令行窗口，一个运行服务器程序，另一个运行客户端程序，就可以看到效果了：
# 需要注意的是，客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序。
