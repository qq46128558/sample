## 数据类型

### 数值类型
    1个字节8位: 1111 1111=255, 留1位负号:0111 1111=127
    如TINYINT:1字节 取值范围: -128~127
    TINYINT SMALLINT MEDIUMINT INTEGER BIGINT FLOAT DOUBLE DECIMAL(M,D)
    1       2        3         4       8      4     8      M+2/D+2

### 整形数值
~~~
TINYINT[(M)][UNSIGNED][ZEROFILL]
- M 表示每个值的位数，此处为显示的位数，并不是占用字节大小
- 当结合可选扩展属性ZEROFILL使用时， 默认补充的空格用零代替。例如，对于声明为INT(5)  ZEROFILL的列，值5检索为00005。
- 如果一个数值列指定为 ZEROFILL， MySQL自动为该列添加 UNSIGNED 属性

mysql> create table int_type(
    -> id TINYINT not null default 0,
    -> age TINYINT(4) not null default 0,
    -> distance TINYINT(4) ZEROFILL not null default 0,
    -> score TINYINT UNSIGNED not null default 0,
    -> ranking TINYINT ZEROFILL not null default 0
    -> )engine myisam charset utf8;
Query OK, 0 rows affected, 1 warning (0.06 sec)

mysql> desc int_type;
+----------+------------------------------+------+-----+---------+-------+
| Field    | Type                         | Null | Key | Default | Extra |
+----------+------------------------------+------+-----+---------+-------+
| id       | tinyint(4)                   | NO   |     | 0       |       |
| age      | tinyint(4)                   | NO   |     | 0       |       |
| distance | tinyint(4) unsigned zerofill | NO   |     | 0000    |       |
| score    | tinyint(3) unsigned          | NO   |     | 0       |       |
| ranking  | tinyint(3) unsigned zerofill | NO   |     | 000     |       |
+----------+------------------------------+------+-----+---------+-------+
~~~

### 浮点型数值
~~~
在MySQL中单精度值使用4个字节，双精度值使用8个字节
DOUBLE[(M,D)][UNSIGNED][ZEROFILL]
M：精度，代表“总位数”；
D：标度，代表小数位（小数点右边的位数）
~~~


### 布尔值
    MySQL 没有内置的 BOOLEAN 或 BOOL 数据类型，使用最小的整数类型，也就是 TINYINT(1) 来表示。

### 日期和时间类型
    DATETIME DATE TIMESTAMP TIME YEAR
    8        3    4         
    每个时间类型有一个有效值范围和一个"零"值，当指定不合法的MySQL不能表示的值时使用"零"值。
    包含两位数年份值的日期是不明确的，因为世纪是未知的，MySQL 使用如下规则解释两位数的年份值：
    1. 年份值在70~99之间转换为1970~1999
    2. 年份值在00~69之间转换为2000~2069

### 字符串类型
    CHAR VARCHAR BINARY VARBINARY TINYBLOB BLOB MEDIUMBLOB LONGBLOB TINYTEXT TEXT MEDIUMTEXT LONGTEXT ENUM SET
    - CHAR和VARCHAR类型声明时需要一个长度值，该值表示你想要想要存储的字符的最大数量
        - CHAR(30)可以容纳30个字符。 CHAR 列的宽度在创建表时已经固定下来了，如果插入记录该字段的宽度不足指定宽度，那么要在右侧自动填补 空格。检索CHAR值时，除非启用 PAD_CHAR_TO_FULL_LENGTH SQL模式，否则将删除尾部空格
    - BINARY 和 VARBINARY 类似于 CHAR 和 VARCHAR，不同的是它们包含二进制字符串而不要非二进制字符串
    - BLOB 是一个二进制大对象，可以容纳可变数量的数据
    - TEXT 长文本数据
    - ENUM 是一个字符串对象，它从一个允许值列表中选择了一个值，这些值在表创建时显式地列出了列规范中
        - CREATE TABLE: -> size enum('x-small', 'small', 'medium', 'large')
        - 在一列有有限的可能值集合的情况下，压缩数据存储。你指定为输入值的字符串被自动编码为数字。
        - 可读的查询和输出。在查询结果中，这些数字被转换回相应的字符串。
        - 假如向该表中插入一百万条 值为 'medium' 的ENUM记录，存储空间需要一百万字节。相比而言，如果以字符串 'medium' 存储，则需要六百万字节。
    - SET 是一个字符串对象，可以有0个或多个值，并且每一个值都必须从表创建时指定的允许值列表中选择
        - CREATE TABLE: SET('one', 'two') NOT NULL
        - SET 的列值由多个集合成员组成的，用逗号（，）分隔
        - 这样的话，SET成员值本身不应该包含逗号
        - 如果一条记录里已经包含 SET 的一个成员了，就不会重复保存该值

### 空间数据类型
~~~
MySQL支持许多包含各种几何和地理值的空间数据类型
GEOMETRY 任何类型的空间值
POINT 一个点(X-Y坐标)
LINESTRING 曲线(一个或多个POINT值)
POLYGON 多边形
GEOMETRYCOLLECTION GEOMETRY值得集合
MULTILINESTRING LINESTRING值得集合
MULTIPOINT POINT值得集合
MULTIPOLYGON POLYGON值得集合
~~~

### JSON 数据类型
~~~
MySQL 支持由 RFC 7159   规定的原生 JSON 数据类型，以更有效地存储和管理JSON文档。 本机JSON数据类型提供JSON文档的自动验证和最佳存储格式。 JSON 列不能有默认值
- CREATE TABLE myjson (jdoc JSON);
~~~