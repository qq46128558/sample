#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用SQLAlchemy'
# ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。
# 在Python中，最有名的ORM框架是SQLAlchemy。

# 首先通过pip安装SQLAlchemy：
''' $ pip install sqlalchemy '''

# 然后，利用上次我们在MySQL的test数据库中创建的user表，用SQLAlchemy来试试：
# 第一步，导入SQLAlchemy，并初始化DBSession：
# 导入:
from sqlalchemy import Column,String,INTEGER,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 创建对象的基类:
Base=declarative_base()

# 定义User对象
class User(Base):
    # 表的名字:
    __tablename__='user'
    # 表的结构: 
    id=Column(INTEGER,primary_key=True)
    name=Column(String(20))

# 初始化数据库连接:
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine=create_engine('mysql+pymysql://ec_admin:ec_admin@123@192.168.239.138:3306/test')
# 创建DBSession类型:
DBSession=sessionmaker(bind=engine)
# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class

# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
# 创建session对象:
session=DBSession()
# 创建新User对象:
new_user=User(name=str(datetime.now().timestamp()))
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()

# 如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user=session.query(User).filter(User.id==5).one()
# 打印类型和对象的name属性:
print('01.',type(user))
print('02.',user.name)

# 关闭session:
session.close()
# 关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。

# ORM就是把数据库表的行与相应的对象建立关联，互相转换。

# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
# 例如，如果一个User拥有多个Book，就可以定义一对多关系如下：
# class User(Base):
#     __tablename__ = 'user'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
    ''' books = relationship('Book') '''

# class Book(Base):
#     __tablename__ = 'book'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
    ''' user_id = Column(String(20), ForeignKey('user.id')) '''
# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。

# ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。

# 正确使用ORM的前提是了解关系数据库的原理。
