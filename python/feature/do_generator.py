#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g=(x*x for x in range(1,11))
print('01.',g)
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
print('02.',next(g),next(g),next(g))
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
# 也可以使用for循环，因为generator也是可迭代对象
l=[]
for n in g:
    l.append(n)
print('03.',l)

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
def fib(max):
    n,a,b=0,0,1
    while n<max:
        n+=1
        print(n,b)
        a,b=b,a+b
    return 'Done'
print('04.',fib(6))
''' 赋值语句
a, b = b, a + b
相当于：
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1] '''

# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib2(max):
    n,a,b=0,0,1
    while n<max:
        n+=1
        yield b
        a,b=b,a+b
    return 'Done'
print('05.',fib2(6))
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# 用next()函数不断获得下一个返回值
# 把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g=fib2(6)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print('06.','Generator return value:',e.value)
        break

# 杨辉三角的实现
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

# 改进版
def triangles():
    l=[1]
    yield l
    while True:
        # 用range取list的序号,通过序号取list的值
        l=[l[i]+l[i+1] for i in range(len(l)-1)]
        # 开始位置插入1
        l.insert(0,1)
        # 结束位置插入1
        l.insert(len(l),1)
        yield l

# 我的原始版
def triangles2():
    l=[1]
    l2=[1]
    while True:
        yield l2
        i=0
        j=len(l)
        l2=[1]
        while i<j:
            i+=1
            if j==1:
                l2.append(l[i-1])
            elif i<j:
                l2.append(l[i]+l[i-1])
        if j!=1:
            l2.append(1)
        l=l2
        

n=0
for t in triangles():
    print(t)
    n+=1
    if n==10:
        break
# generator函数的“调用”实际返回一个generator对象
