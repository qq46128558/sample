#### 创建一个database
CREATE DATABASE `databasename`;

#### 创建一张table(示例)
CREATE TABLE `tablename`(id BIGINT(7) NOT NULL AUTO\_INCREMENT,title VARCHAR(200),content VARCHAR(10000),created TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,PRIMARY KEY(id));

#### 创建一个查询某字段前16个字符的智能索引
CREATE INDEX `indexname` ON `tablename`(`id`,`fieldname`(16));


#### CREATE TABLE 用到的关键字
~~~
PRIMARY KEY
AUTO_INCREMENT
NOT NULL
DEFAULT ''
UNSIGNED
)ENGINE MYISAM CHARSET UTF-8
~~~

