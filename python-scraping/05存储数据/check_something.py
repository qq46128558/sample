from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from urllib.request import urlopen
import time
from email.utils import parseaddr,formataddr
from email.header import Header

password=input('please input email password:')
def sendMail(subject,body):
    msg=MIMEText(body)
    msg['Subject']=subject
    # 格式化一个邮件地址
    # name, addr=parseaddr(s)
    # formataddr((Header(name,'utf-8').encode(),addr))
    msg['From']=formataddr((Header("Peter",'utf-8').encode(),"dgw@yn-ce.com"))
    msg['To']="46128558@qq.com"
    s=smtplib.SMTP(host="smtp.exmail.qq.com",port=25)
    s.login("dgw@yn-ce.com",password)
    s.send_message(msg)
    s.quit()

html=urlopen("https://isitchristmas.com/")
bsObj=BeautifulSoup(html,'html.parser')

# print(bsObj.find("a",{"id":"answer"}).attrs['title'])
# print(bsObj.find("a",{"id":"answer"}))
# 中国用户在网站页面上看到的“NO”在源代码里是<noscript> 不是 </noscript>
# print(bsObj.find("a",{"id":"answer"}).find("noscript").get_text())
# while (bsObj.find("a",{"id":"answer"}).attrs['title']=='NO'):
while (bsObj.find("a",{"id":"answer"}).find("noscript").get_text()=='不是'):
    print("It is not Christmas yet.")
    time.sleep(3600)
    bsObj=BeautifulSoup(html,'html.parser')

sendMail("It's Christmas!","According to https://isitchristmas.com, it is Christmas!")
# 这个程序每小时检查一次 https://isitchristmas.com/ 网站（根据日期判断当天是不是圣诞节）。
    