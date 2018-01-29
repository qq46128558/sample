#####创建一个database
CREATE DATABASE `databasename`;

#####创建一张table(示例)
CREATE TABLE `tablename`(id BIGINT(7) NOT NULL AUTO\_INCREMENT,title VARCHAR(200),content VARCHAR(10000),created TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,PRIMARY KEY(id));

