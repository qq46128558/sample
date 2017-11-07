#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'图形界面'
# Python支持多种图形界面的第三方库，包括：
# Tk
# wxWidgets
# Qt
# GTK
# 等等。
# 但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。本章简单介绍如何使用Tkinter进行GUI编程。

from tkinter import *
import tkinter.messagebox as messagebox

# 从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        # pack()方法把Widget加入到父容器中，并实现布局。
        self.pack()
        # 在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel=Label(self,text="Welcome back.")
        # pack()方法把Widget加入到父容器中，并实现布局。
        self.helloLabel.pack()
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.afterButton=Button(self,text="Welcome",command=self.welcome)
        self.afterButton.pack()
        self.quitButton=Button(self,text="Quit",command=self.quit)
        self.quitButton.pack()
    def welcome(self):
        name=self.nameInput.get() or ' back'
        messagebox.showinfo('Message','Welcome %s'%name)

# 在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
# pack()是最简单的布局，grid()可以实现更复杂的布局。
app=Application()
# 设置窗口标题:
app.master.title('GUI Welcome Back')
# 主消息循环:
app.mainloop()
# GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理。
# 当用户点击按钮时，触发hello()，通过self.nameInput.get()获得用户输入的文本后，使用tkMessageBox.showinfo()可以弹出消息对话框。

# Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。
