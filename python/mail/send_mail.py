#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'SMTP发送邮件'

# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
# 首先，我们来构造一个最简单的纯文本邮件：
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase

# 我们编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
def _format_addr(s):
    name, addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

# 输入Email地址和口令:
from_addr='dgw@yn-ce.com'
password=input('Password: ')
# 输入收件人地址:
to_addr='46128558@qq.com'
# 输入SMTP服务器地址:
smtp_server='smtp.exmail.qq.com'


# 发送附件
# 带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
msg=MIMEMultipart()
# 邮件正文是MIMEText:
# 发送图片, 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
msg.attach(MIMEText('<html><body>Hello, send by Python...</body><p><img src="cid:0"></p></html>','html','utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('d:/projects/www/sample/1353022505371.jpg','rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime=MIMEBase('image','jpg',filename='1353022505371.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition','attachment',filename='1353022505371.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)


# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
''' msg=MIMEText('Hello, send by Python...','plain','utf-8') '''

# 如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：
''' msg=MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8') '''

# 同时支持HTML和Plain格式
# msg = MIMEMultipart('alternative')
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))


msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
# msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['To']=_format_addr('Peter<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候...','utf-8').encode()


# 然后，通过SMTP发出去：
import smtplib
server=smtplib.SMTP(smtp_server,25) # SMTP协议默认端口是25
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
# 某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。
server.starttls()
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。
server.set_debuglevel(1)
# login()方法用来登录SMTP服务器
server.login(from_addr,password)
# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
# 如果一切顺利，就可以在收件人信箱中收到我们刚发送的Email：



# 使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。

# 构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：

# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage

# 你可以通过email.mime文档查看它们所在的包以及详细的用法。