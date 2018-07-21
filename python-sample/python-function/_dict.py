''' dict() 函数 '''

# dict的值转tuple
print(tuple({'comment':'好评','date':'2018-07-21','rate':5,'city':'珠海','nickname':'Peter'}.values()))
# ('好评', '2018-07-21', 5, '珠海', 'Peter')

# 使用字典进行分支处理
def fn1():
    print("fn1")
def fn2():
    print("fn2")
def fn3():
    print("fn3")
f=dict(keya=fn1,keyb=fn2,keyc=fn3)
f['keyb']()
# fn2

# 创建空字典
print(dict())
# {}

# 传入关键字
print(dict(a='a', b='b', t='t'))
# {'t': 't', 'a': 'a', 'b': 'b'}

# 映射函数方式来构造字典
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
# {'three': 3, 'one': 1, 'two': 2}

# 可迭代对象方式来构造字典
print(dict([('one', 1), ('two', 2), ('three', 3)]))
# {'three': 3, 'one': 1, 'two': 2}
