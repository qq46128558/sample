#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'使用模板'
# Web App不仅仅是处理逻辑，展示给用户的页面也非常重要。在函数中返回一个包含HTML的字符串，简单的页面还可以
# 由于在Python代码里拼字符串是不现实的，所以，模板技术出现了。
# 使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户

# MVC：Model-View-Controller，中文名“模型-视图-控制器”。
# Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；
# 包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
# MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。
# 上面的例子中，Model就是一个dict

from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password.',username=username)

if __name__=='__main__':
    app.run()

# Flask通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2，所以我们先直接安装jinja2：
''' pip install jinja2 '''
# 然后，开始编写jinja2模板
# 最后，一定要把模板放到正确的templates目录下，templates和app.py在同级目录下：

# 使用模板的另一大好处是，模板改起来很方便，而且，改完保存后，刷新浏览器就能看到最新的效果，这对于调试HTML、CSS和JavaScript的前端工程师来说实在是太重要了。

# 在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
# 比如循环输出页码：
''' {% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}
 '''
# 除了Jinja2，常见的模板还有：
# Mako：用<% ... %>和${xxx}的一个模板；
# Cheetah：也是用<% ... %>和${xxx}的一个模板；
# Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。

# 有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。