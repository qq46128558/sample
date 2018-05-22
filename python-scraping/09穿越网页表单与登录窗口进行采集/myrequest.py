import requests

# 用open函数打开的python文件对象
# files={'uploadFile':open('./xx.jpg','rb')}

params={'firstname':'Ryan','lastname':'Mitchell'}
r=requests.post("http://pythonscraping.com/files/processing.php",data=params)
print(r.text)
