import smtplib
from email.mime.text import MIMEText

# MIME（Multipurpose Internet MailExtensions，多用途互联网邮件扩展类型）
msg=MIMEText("The body of the email is here")
msg['Subject']="An Email Alert"
msg['From']="dgw@yn-ce.com"
msg['To']="46128558@qq.com"

s=smtplib.SMTP(host='smtp.exmail.qq.com',port=25)
s.login("dgw@yn-ce.com",input("please input email password:"))
s.send_message(msg)
s.quit()
