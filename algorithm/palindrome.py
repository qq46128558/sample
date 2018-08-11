#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 回数是指从左向右读和从右向左读都是一样的数
def is_palindrome(n):
    return str(n)[:]==str(n)[::-1]

output=filter(is_palindrome,range(2017000,2029000)) # filter()函数返回的是一个Iterator
print(list(output))

# str(2017000)[::-1] 右边起每1位取1个
# 0007102
# str(2017000)[::-2] 右边起每2位取1个
# 0012
# str(2017000)[::-3] 右边起每3位取1个
# 072

