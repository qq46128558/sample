import hashlib

list=['a','b','c']
list.sort()
print(list)
sha1=hashlib.sha1()
map(sha1.update,list)
hashcode=sha1.hexdigest()
print(hashcode)

sha2=hashlib.sha1()
sha2.update('abc'.encode('utf-8'))
print(sha2.hexdigest())

# 未验证成功
