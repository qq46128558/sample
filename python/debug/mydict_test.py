#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'编写单元测试'

# 为了编写单元测试，我们需要引入Python自带的unittest模块
import unittest
from mydict import Dict

# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
class TestDict(unittest.TestCase):
    # setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：
    def setUp(self):
        print('setUp running...')
    def tearDown(self):
        print('tearDown running...')

    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d=Dict(a=1,b='test')
        # 最常用的断言就是assertEqual()
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    
    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')
    
    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d=Dict()
        # 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
        with self.assertRaises(KeyError):
            value=d['empty']
    
    def test_attrerror(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            # 而通过d.empty访问不存在的key时，我们期待抛出AttributeError：
            value=d.empty
    
# 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__=="__main__":
    unittest.main()

# 另一种方法是在命令行通过参数-m unittest直接运行单元测试：
# $ python3 -m unittest mydict_test

# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
