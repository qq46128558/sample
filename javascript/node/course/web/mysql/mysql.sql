-- 检查编码
show variables like '%char%';

-- 显示数据库,显示表
show databases;
show tables;

-- 时间戳(10位)转时间
select from_unixtime(1111111111);

-- 授权用户
-- grant命令是创建MySQL的用户名和口令，均为www，并赋予操作test数据库的所有权限。
grant all privileges on test.* to 'www'@'%' identified by 'www';

-- 选择数据库
-- use命令把当前数据库切换为test。
use test;

-- 创建数据表
create table pets (
    id varchar(50) not null,
    name varchar(100) not null,
    gender bool not null,
    birth varchar(10) not null,
    createdAt bigint not null,
    updatedAt bigint not null,
    version bigint not null,
    primary key (id)
) engine=innodb;

-- 创建数据库并授权
create database nodejs;
grant all privileges on nodejs.* to 'www'@'%' identified by 'www';