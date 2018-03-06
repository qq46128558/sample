import hashlib

list1=['2','3','1']
list1.sort()
# print(list)
sha1=hashlib.sha1()
map(sha1.update,list1)
hashcode=sha1.hexdigest()
print(hashcode)

sha1_temp=hashlib.sha1()
sha1_temp.update('1'.encode('utf-8'))
sha1_temp.update('2'.encode('utf-8'))
sha1_temp.update('3'.encode('utf-8'))
print(sha1_temp.hexdigest())

# 未验证成功
