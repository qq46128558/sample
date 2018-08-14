

#### SELECT 显示加锁
~~~
#共享锁，其它事务可读，不可更新  
SELECT ... LOCK IN SHARE MODE
#排它锁，其它事务不可读写
SELECT ... FOR UPDATE  

#上面的2种语句只有在事务之中才能生效
SET AUTOCOMMIT=0;   
BEGIN WORK;   
    a = SELECT num FROM table1 WHERE id=2 FOR UPDATE; 
    UPDATE table1 SET num = a.num + 1 WHERE id=2;   
COMMIT WORK;  
~~~


#### 将时间戳转换为日期时间
    SELECT FROM_UNIXTIME(`timestamp`);

#### 查询当前时间戳
	SELECT UNIX_TIMESTAMP();
	
#### 基本查询
    SELECT * FROM `tablename` WHERE `condition`;

#### like查询
    SELECT * FROM `tablename` WHERE `fieldname` LIKE "%`string`%";

#### 计算字段长度
    SELECT LENGTH("中文ABC");
一个汉字算三个字符,一个数字或字母算一个字符


#### 限制结果
	SELECT * FROM `tablename` LIMIT `偏移量`,`记录数`;
	SELECT * FROM `tablename` LIMIT `记录数` OFFSET `偏移量`;
	SELECT * FROM `tablename` ORDER BY `field` DESC	LIMIT 1;
	
#### 通配符
	<!-- % 多个任意字符 _ 单个任意字符 -->
	SELECT `field` FROM `tablename` WHERE `field` LIKE 'XXX%';
	SELECT `field` FROM `tablename` WHERE `field` LIKE 'XXX_';

#### WHERE子句操作符
	= <> != < <= > >= BETWEEN

#### WHERE子句关键字
	IS NULL	AND	OR	IN	NOT	LIKE REGEXP