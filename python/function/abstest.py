def my_abs(x):
    # 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
    # 数据类型检查可以用内置函数isinstance()实现
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type.')
    if x>0:
        return x
    else:
        return -x