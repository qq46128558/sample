import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response=urlopen("https://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson=json.loads(response)
    return responseJson.get("country_code")

# Python 使用了一种更加灵活的方式，把 JSON 转换成字典，JSON 数组转换成列表,JSON 字符串转换成 Python 字符串
print(getCountry('221.4.217.74'))