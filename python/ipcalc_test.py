#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipcalc
import logging

logging.basicConfig(level=logging.INFO)

def unit_test(value,quantity,mark,net,first,last,board):
    result=ipcalc.calc(value)
    # print(result)
    if result[2]!=quantity:
        logging.info('%s可用地址有误,计算值:%s,正确值:%s'%(value,result[2],quantity))
    if result[3]!=mark:
        logging.info('%s掩码有误,计算值:%s,正确值:%s'%(value,result[3],mark))
    if result[4]!=net:
        logging.info('%s网络有误,计算值:%s,正确值:%s'%(value,result[4],net))
    if result[5]!=first:
        logging.info('%s第一个可用有误,计算值:%s,正确值:%s'%(value,result[5],first))
    if result[6]!=last:
        logging.info('%s最后可用有误,计算值:%s,正确值:%s'%(value,result[6],last))
    if result[7]!=board:
        logging.info('%s广播有误,计算值:%s,正确值:%s'%(value,result[7],board))

# 基本测试
unit_test('192.168.10.62/0',4294967294,[0,0,0,0],[0,0,0,0],[0,0,0,1],[255,255,255,254],[255,255,255,255])
unit_test('192.168.10.62/21',2046,[255,255,248,0],[192,168,8,0],[192,168,8,1],[192,168,15,254],[192,168,15,255])
unit_test('192.168.10.62/24',254,[255,255,255,0],[192,168,10,0],[192,168,10,1],[192,168,10,254],[192,168,10,255])
unit_test('192.168.10.62/29',6,[255,255,255,248],[192,168,10,56],[192,168,10,57],[192,168,10,62],[192,168,10,63])
unit_test('192.168.10.62/31','two hosts',[255,255,255,254],[],[192,168,10,62],[192,168,10,63],[])
unit_test('192.168.10.62/32','one host',[255,255,255,255],[],[192,168,10,62],[],[])

