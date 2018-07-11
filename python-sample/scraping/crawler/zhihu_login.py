#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://github.com/xchaoinfo/fuck-login/tree/master/001%20zhihu
Required
- requests (必须)
- pillow (可选)
Info
- author : "xchaoinfo"
- email  : "xchaoinfo@qq.com"
- date   : "2016.2.4"
Update
- name   : "wangmengcn"
- email  : "eclipse_sv@163.com"
- date   : "2016.4.21"
@xchaoinfo xchaoinfo 解决知乎升级导致登录失败的问题
'''
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass


# 构造 Request headers
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


def get_xsrf():
    '''_xsrf 是一个动态变化的参数'''
    index_url = 'https://www.zhihu.com'
    # 获取登录时需要用到的_xsrf
    index_page = session.get(index_url, headers=headers)
    html = index_page.text

    # edit by peter 2018-01-04 ?的作用是采用非贪婪匹配
    pattern = r'name="_xsrf" value="(.*?)"'

    # 这里的_xsrf 返回的是一个list
    _xsrf = re.findall(pattern, html)
    # edit by peter 2018-01-04
    # UnicodeEncodeError: 'gbk' codec can't encode character '\u200b' in position 23067: illegal multibyte sequence
    # https://www.crifan.com/unicodeencodeerror_gbk_codec_can_not_encode_character_in_position_illegal_multibyte_sequence/
    # 往往最大的可能就是，本身Unicode类型的字符中，包含了一些无法转换为GBK编码的一些字符
    # print(html.encode('GBK','ignore'))
    # 将html输出到文件进行_xsrf问题排查
    # with open('html_output.txt','wb') as f:
    #     f.write(html.encode('GBK','ignore'))
    # print(_xsrf)
    # exit()
    if _xsrf==[]:
        pattern=r'xsrf&quot;:&quot;(.{32})'
        _xsrf=re.findall(pattern,html)
        # print(_xsrf[0].encode('GBK','ignore'))
        # exit()
    return _xsrf[0]
    # return '66cb7121-b5d0-46c2-8e9f-a3ba0eeeb7a8'


# 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False


def login(secret, account):
    _xsrf = get_xsrf()
    headers["X-Xsrftoken"] = _xsrf
    headers["X-Requested-With"] = "XMLHttpRequest"
    # 通过输入的用户名判断是否是手机号
    if re.match(r"^1\d{10}$", account):
        print("手机号登录 \n")
        post_url = 'https://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': _xsrf,
            'password': secret,
            'phone_num': account
        }
    else:
        if "@" in account:
            print("邮箱登录 \n")
        else:
            print("你的账号输入有问题，请重新登录")
            return 0
        post_url = 'https://www.zhihu.com/login/email'
        postdata = {
            '_xsrf': _xsrf,
            'password': secret,
            'email': account
        }
    # 不需要验证码直接登录成功
    login_page = session.post(post_url, data=postdata, headers=headers)
    login_code = login_page.json()
    if login_code['r'] == 1:
        # 不输入验证码登录失败
        # 使用需要输入验证码的方式登录
        postdata["captcha"] = get_captcha()
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = login_page.json()
        print(login_code['msg'])
    # 保存 cookies 到文件，
    # 下次可以使用 cookie 直接登录，不需要输入账号和密码
    session.cookies.save()

try:
    input = raw_input
except:
    pass


if __name__ == '__main__':
    if isLogin():
        print('您已经登录')
        url = "https://www.zhihu.com/logout"
        logout_code = session.get(url, headers=headers, allow_redirects=False).status_code
        print(logout_code)
    else:
        # account = input('请输入你的用户名\n>  ')
        account='46128558@qq.com'
        # secret = input("请输入你的密码\n>  ")
        secret='******'
        login(secret, account)