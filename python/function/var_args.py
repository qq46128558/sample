#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
# 设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
# 当不按顺序提供部分默认参数时，需要把参数名写上
def enroll(name,gender,age=6,city='Beijing'):
    print(name)
    print(gender)
    print(age)
    print(city)
enroll('Sarah','F',city='Tianjin')

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！L=[]是可变对象
def add_end(L=None):
    if L is None:
        L=[]
    L.append('End')
    return L
print('01.',add_end())
print('02.',add_end())
# 由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*number):
    sum=0
    for n in number:
        sum+=n**2
    return sum
print('03.',calc(1,2,3))
# 如果已经有一个list或者tuple，要调用一个可变参数怎么办
# 以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
num=[1,2,3]
print('04.',calc(*num))

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('04.',kw)
person('Bob',35,city='Beijing',gender='M')
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra={'city':'Zhuhai','job':'Engineer'}
person('Jack',24,**extra)
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person2(name,age,*,city,job):
    print('05.',name,age,city,job)
person2('Tracy',24,city='Shanghai',job='Doctor')
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person3(name,age,*args,city,job):
    print('06.',name,age,args,city,job)
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
person3('Dick',65,'A','B','C',city='Hangzhou',job='Painter')
# 命名关键字参数可以有缺省值，从而简化调用
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a,b,c=0,*args,**kw):
    print('07.','a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)

args=(1,2,3)
def f2(a,b,c=0,*,d,**kw):
    print('08.','a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
f2(*args,**kw)
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

# *args是可变参数，args接收的是一个tuple；
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# **kw是关键字参数，kw接收的是一个dict。
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。