#!/usr/bin/env python3

'获取微信好友'

# 登陆微信，获取朋友信息的库
import itchat
import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)

# 登陆微信网页版(使用手机扫描二维码就可以登录)
itchat.login()
# 获取当前微信好友信息
# 返回的 friends 是一个集合，第一个元素是当前用户，也就是你自己，集合中的每一个元素都是一个字典结构，可以注意到这里有Sex、City、Province、NickName、Signature等
friends=itchat.get_friends(update=True)[0:]
logging.info(friends[1])
# INFO:root:{'MemberList': <ContactList: []>, 'UserName': '@0408ddab35d6c2a930694b46a381ec5de1e0ee912e8ead185767fb1a8ed65db5', 'City': '珠海', 'DisplayName': '', 'PYQuanPin': 'Peter', 'RemarkPYInitial': '', 'Province': '广东', 'KeyWord': '', 'RemarkName': '', 'PYInitial': 'PETER', 'EncryChatRoomId': '', 'Alias': '', 'Signature': '长路漫漫', 'NickName': 'Peter', 'RemarkPYQuanPin': '', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=860141&username=@0408ddab35d6c2a930694b46a381ec5de1e0ee912e8ead185767fb1a8ed65db5&skey=@crypt_a16a63ce_e48e83ced69b6379c18e1e7dc9ae43cb', 'UniFriend': 0, 'Sex': 1, 'AppAccountFlag': 0, 'VerifyFlag': 0, 'ChatRoomId': 0, 'HideInputBarFlag': 0, 'AttrStatus': 102437, 'SnsFlag': 17, 'MemberCount': 0, 'OwnerUin': 0, 'ContactFlag': 1, 'Uin': 1957910301, 'StarFriend': 0, 'Statues': 0, 'WebWxPluginSwitch': 0, 'HeadImgFlag': 1, 'IsOwner': 0}

# INFO:root:{'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@a03f5d71587d3c17508133d576f6a21d92b98bf1900dcd98604c2c9281111e8d', 'NickName': 'Linda贤\u0f3b', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=688987043&username=@a03f5d71587d3c17508133d576f6a21d92b98bf1900dcd98604c2c9281111e8d&skey=@crypt_a16a63ce_0cefbcd37ffa83d57e30613988dfe8b7', 'ContactFlag': 2051, 'MemberCount': 0, 'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 2, 'Signature': '慈悲为本，为善心安；先做人，后做事；先知礼，后让人。', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'LINDAX?', 'PYQuanPin': 'Lindaxian?', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 33666149, 'Province': '广东', 'City': '珠海', 'Alias': '', 'SnsFlag': 17, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}

columns=[]
for key in friends[1]:
    columns.append(key)
df=pd.DataFrame(columns=columns)
logging.info(columns)
# 自己：INFO:root:['MemberList', 'UserName', 'City', 'DisplayName', 'PYQuanPin', 'RemarkPYInitial', 'Province', 'KeyWord', 'RemarkName', 'PYInitial', 'EncryChatRoomId', 'Alias', 'Signature', 'NickName', 'RemarkPYQuanPin', 'HeadImgUrl', 'UniFriend', 'Sex', 'AppAccountFlag', 'VerifyFlag', 'ChatRoomId', 'HideInputBarFlag', 'AttrStatus', 'SnsFlag', 'MemberCount', 'OwnerUin', 'ContactFlag', 'Uin', 'StarFriend', 'Statues', 'WebWxPluginSwitch', 'HeadImgFlag', 'IsOwner']
# 其他：INFO:root:['MemberList', 'Uin', 'UserName', 'NickName', 'HeadImgUrl', 'ContactFlag', 'MemberCount', 'RemarkName', 'HideInputBarFlag', 'Sex', 'Signature', 'VerifyFlag', 'OwnerUin', 'PYInitial', 'PYQuanPin', 'RemarkPYInitial', 'RemarkPYQuanPin', 'StarFriend', 'AppAccountFlag', 'Statues', 'AttrStatus', 'Province', 'City', 'Alias', 'SnsFlag', 'UniFriend', 'DisplayName', 'ChatRoomId', 'KeyWord', 'EncryChatRoomId', 'IsOwner']

for friend in friends[1:]:
    dict={}
    for key in columns:
        # 需要从1开始，0为是自己，部分key不同，会报错：KeyError: 'WebWxPluginSwitch'
        dict[key]=friend[key]
    df=df.append(dict,ignore_index=True)

# 用gb18030有些会乱码问号???
df.to_csv('friends.csv',index=False,encoding='gb18030')
