#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
广度优先搜索
breadth-first search
广度优先搜索算法的思路是优先搜寻直接连接到起始页的所有链接（而不是找到一个链接
就纵向深入搜索）。如果这些链接不包含目标页面（你想要找的词条），就对第二层的链
接——连接到起始页的页面的所有链接——进行搜索。这个过程不断重复，直到达到搜索
深度限制（本例中使用的层数限制是 6 层）或者找到目标页面为止。
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='mysql',charset='utf8')
cur=conn.cursor()
cur.execute("USE wikipedia")

class SolutionFound(RuntimeError):
    def __init__(self,message):
        self.message=message

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId=%s",(fromPageId))
    if cur.rowcount==0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

# 这里函数 getLinks 和 constructDict 是辅助函数，用来从数据库里获取给定页面的链接，然后把链接转换成字典。
def constructDict(currentPageId):
    links=getLinks(currentPageId)
    if links:
        return dict(zip(links,[{}]*len(links)))
    return {}

# 主函数 searchDepth 会递归地执行，同时构建和搜索链接树，一次搜索一层。
# 链接树要么为空，要么包含多个链接
def searchDepth(targetPageId,currentPageId,linkTree,depth):
    # 如果递归限制已经到达（即程序已经调用过很多次），就停止搜索，返回结果
    if depth==0:
        # 停止递归,返回结果
        return linkTree
    # 如果函数获取的链接字典是空的，就对当前页面的链接进行搜索
    if not linkTree:
        linkTree=constructDict(currentPageId)
        # 如果当前页面也没链接，就返回空链接字典
        if not linkTree:
            # 若此节点页面无链接,则跳过此节点
            return {}
    # 如果当前页面包含我们搜索的页面链接,就把页面 ID 复制到递归的栈顶
    if targetPageId in linkTree.keys():
        print("TARGET "+str(targetPageId)+ " FOUND!")
        # 递归过程中的每个栈都会打印当前页面 ID，然后抛出异常显示页面已经找到，最终打印在屏幕上的就是一个完整的页面 ID 路径列表。
        # 然后抛出一个异常，显示页面已经找到
        raise SolutionFound("PAGE: "+str(currentPageId))
        
    for branchKey,branchValue in linkTree.items():
        try:
            # 递归建立链接树
            # 如果链接没找到，把递归限制减一，然后调用函数搜索下一层链接
            linkTree[branchKey]=searchDepth(targetPageId,branchKey,branchValue,depth-1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE: "+str(currentPageId))
    return linkTree

try:
    searchDepth(5337,1,{},4)
    print("No solution found")
except SolutionFound as e:
    print(e.message)
