''' dict() 函数用于创建一个字典。 '''

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