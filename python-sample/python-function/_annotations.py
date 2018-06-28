#!/usr/bin/env python3

'函数注释-只能是类型的注释'

def print_str(s:str) -> bool:
    print(s)
    return True if s == '' else False
print(print_str.__annotations__)
# {'return': <class 'bool'>, 's': <class 'str'>}
result = print_str('python')
# python
print(result)
# False
result = print_str('')
# 
print(result)
# True