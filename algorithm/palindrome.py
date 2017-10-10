#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 回数是指从左向右读和从右向左读都是一样的数
def is_palindrome(n):
    return str(n)[:]==str(n)[::-1]

output=filter(is_palindrome,range(2017000,2029000)) # filter()函数返回的是一个Iterator
print(list(output))