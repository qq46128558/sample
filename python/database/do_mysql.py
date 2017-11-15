#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用MySQL'

# MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
# 此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。

# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
''' $ pip install mysql-connector-python --allow-external mysql-connector-python '''
# 如果上面的命令安装失败，可以试试另一个驱动：
''' $ pip install mysql-connector '''

''' MySqlDB官网只支持Python3.4，这里Python3.5使用第三方库PyMysql连接Mysql数据库。 '''
# pip install pymysql

import pymysql
from datetime import datetime
# password=input('Password: ')
password='ec_admin@123'
conn=pymysql.connect(user='ec_admin',password=password,database='test',host='192.168.239.138',port=3306)
cursor=conn.cursor()
# 创建user表:
cursor.execute("select 1 from information_schema.tables where table_schema='test' and table_name='user'")
value=cursor.fetchall()
if not value:
    cursor.execute("create table if not exists user(id int(10) primary key auto_increment, name varchar(20))")
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert user (name) values (%s)',[str(datetime.now().timestamp())])
value=cursor.rowcount
print('01.',value)
# 提交事务:
conn.commit()
# 运行查询:
cursor.execute('select * from user where id=%s',(1,))
value=cursor.fetchall()
print('02.',value)

# 关闭Cursor和Connection:
cursor.close()
conn.close()


# 执行INSERT等操作后要调用commit()提交事务；
# MySQL的SQL占位符是%s。


