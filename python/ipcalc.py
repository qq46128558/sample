#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'根据IP及子网掩码计算起始IP段'

__author__='peter'

import re

def calc(value=None):
    value=input('Please input IP/N:') if value==None else value
    # value="192.168.9.10/21"
    # 250~255|200~249|100~199|10~99|0~9
    re_ip=r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])'
    # 此处有疑问,未知最后的[0-9]为何能匹配到两位数字中的一位,所以加上$
    re_mark=r'(3[0-2]|[1-2][0-9]|[0-9]$)'
    # print(re.match(re_mark,value))
    re_value="(%s\.%s\.%s\.%s)/%s"%(re_ip,re_ip,re_ip,re_ip,re_mark)
    # 校验输入的ip与子网掩码的格式是否正确
    r=re.match(re_value,value)
    if r==None:
        print('What you input IP/N(%s) was illegal.'%value)
        return
    # 校验通过,分开保存ip与子网掩码
    ip=r.group(1)
    mark=r.group(6)
    # 将IP转成二进制
    list_ip=ip.split('.')
    list_ip2=[bin(int(x)) for x in list_ip]
    # 将二进制转成字符串>>再去掉0b>>再补0
    list_ip2=[(8+2-len(x))*'0'+str(x)[2:] for x in list_ip2]
    # 将掩码转成二进制
    n1=int(mark)
    list_mark2=['0'*8]*4
    for x in range(int(int(mark)/8)+1):
        if (n1>8):
            list_mark2[x]='1'*8
        else:
            list_mark2[x]='1'*n1+'0'*(8-n1)
        n1=n1-8
        # 转换成1结束,退出循环
        if n1<=0:
            break
    list_mark=[int(x,2) for x in list_mark2]

    # 31/32掩码特殊处理
    if int(mark)==31:
        list_first=[int(x) for x in list_ip]
        list_last=list_first[:]
        list_last[-1]=int(list_last[-1])+1
        quantity='two hosts'
        list_net=[]
        list_board=[]
    elif int(mark)==32:
        list_first=[int(x) for x in list_ip]
        list_last=[]
        quantity='one host'
        list_net=[]
        list_board=[]
    # 其他掩码
    else:
        # IP与掩码的二制进行与运算,得到网络地址
        list_net2=['']*4
        for x in range(4):
            n1=0
            while n1<8:
                if list_ip2[x][n1:n1+1]==list_mark2[x][n1:n1+1]=='1':
                    list_net2[x]+='1'
                else:
                    list_net2[x]+='0'
                n1+=1
        list_net=[int(x,2) for x in list_net2]

        #网络地址主机位全为1(32-掩码位)为广播地址
        s1=''.join(str(x) for x in list_net2)
        s1=s1[0:int(mark)]+'1'*(32-int(mark))
        list_board2=re.split(r'(\d{8})',s1)
        while '' in list_board2:
            list_board2.remove('')
        list_board=[int(x,2) for x in list_board2]

        # 第一个可用与最后可用
        list_first=list_net[:]
        list_last=list_board[:]
        # 网络地址最后位+1
        list_first[-1]=int(list_net[-1])+1
        # 广播地址最后位-1
        list_last[-1]=int(list_board[-1])-1

        # 计算可用地址
        quantity=(int(list_last[0])-int(list_first[0])+1)*(int(list_last[1])-int(list_first[1])+1)*(int(list_last[2])-int(list_first[2])+1)
        quantity=((int(list_last[-1])-int(list_first[-1])+1)) if quantity==1 else quantity*256-2

    if __name__=='__main__':
        print('可用地址',quantity)
        print('掩码','.'.join(str(x) for x in list_mark))
        print('网络','.'.join(str(x) for x in list_net))
        print('第一个可用','.'.join(str(x) for x in list_first))
        print('最后可用','.'.join(str(x) for x in list_last))
        print('广播','.'.join(str(x) for x in list_board))
    return (ip,mark,quantity,list_mark,list_net,list_first,list_last,list_board)

if __name__=='__main__':
    calc()