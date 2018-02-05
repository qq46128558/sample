#### 将时间戳转换为日期时间
    SELECT FROM_UNIXTIME(`timestamp`);

#### 基本查询
    SELECT * FROM `tablename` WHERE `condition`;

#### like查询
    SELECT * FROM `tablename` WHERE `fieldname` LIKE "%`string`%";

#### 计算字段长度
    SELECT LENGTH("中文ABC");
一个汉字算三个字符,一个数字或字母算一个字符
