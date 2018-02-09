
''' zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。 '''

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
# 打包为元组的列表
zipped = zip(a,b)     
''' [(1, 4), (2, 5), (3, 6)] '''
# <zip object at 0x000000000104C848>
print("zipped")
while True:
    try:
        print(next(zipped))
    except StopIteration:
        break


# 元素个数与最短的列表一致
zip1=zip(a,c)
''' [(1, 4), (2, 5), (3, 6)] '''
print("zip1")
while True:
    try:
        print(next(zip1))
    except StopIteration:
        break

# 与 zip 相反，可理解为解压，返回二维矩阵式
zip2=zip(*zip(a,b))
''' [(1, 2, 3), (4, 5, 6)] '''
print("zip2")
while True:
    try:
        print(next(zip2))
    except StopIteration:
        break