## 正则表达式检索
WHERE中用REGEXP

#### 基本字符匹配
	<!-- . 是正则表达式语言中的一个特殊字符，它表示匹配任意一个字符 -->
	SELECT title FROM yii2_menu WHERE title REGEXP '.改';

#### 进行OR匹配
	SELECT title FROM yii2_menu WHERE title REGEXP '修改|添加';

#### 匹配几个字符之一
	<!-- 包含 alle 或 ille 的城市 -->
	SELECT name, Population FROM city WHERE name REGEXP '[ai]lle';

#### 匹配范围
	<!-- 筛选名称中包含 alle  、blle 、clle 、… 、ille 的城市 -->
	SELECT name, Population FROM city WHERE name REGEXP '[a-i]lle';

#### 匹配特殊字符
	.、-、[ 和 ] 等，如果要匹配此类字符，必须用 \\ 作为前导， \\- 表示查找 -，\\[ 表示查找 [
	\\f	换页
	\\n	换行
	\\r	回车
	\\t	制表
	\\v	纵向制表

#### 匹配字符类
	<!-- MySQL 预定义了字符集用来匹配数字或字母字符等，称为 字符类 -->
~~~
[:alnum:]	任意的字母和数字（同[a-zA-Z0-9]）
[:alpha:]	任意字母（同[a-zA-Z）
[:blank:]	空格和制表（同[\\t]）
[:cntrl:]	ASCII控制字符（ASCII 0到31和127）
[:digit:]	任意数字（同[0-9]）
[:graph:]	与[:print:]相同，但不包含空格
[:lower:]	任意小写字母（同[a-z]）
[:print:]	任意可打印字符
[:punct:]	既不在[:alnum:]又不在[:cntrl:]中的任意字符
[:space:]	包括空格在内的任意空白字符（同[\\f\\n\\r\\t\\v]
[:upper:]	任意大写字母（同[A-Z]）
[:xdigit:]	任意十六进制数字（同[a-fA-F0-9]）
~~~

#### 匹配多个实例
	<!-- 筛选名称存在连续5位包含a-e的城市(不区分大小写) -->
	SELECT name, Population FROM city WHERE name REGEXP '[a-e]{5}';

#### 定位符
	<!-- 为了匹配特定位置的文本，需要使用如下定位符 -->
	^	文本的开始
	$	文本的结尾
	[[:<:]]	词的开始
	[[:>:]]	词的结尾
	<!-- 匹配名称以z开头的城市 -->
	SELECT name, Population FROM city WHERE name REGEXP '^[z]';
	

#### MySQL 仅支持多数正则表达式实现的一个很小的子集
|模式|描述
|-|-
|^|匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。
|$|匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。
|.|匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
|[…]|字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。
|[^…]|负值字符集合。匹配未包含的任意字符。例如， '[\^abc]' 可以匹配 "plain" 中的'p'。
|p1丨p2丨p3|(**因为markdown表格原因,此处用了棍丨**)匹配 p1 或 p2 或 p3。例如，'z丨food' 能匹配 "z" 或 "food"。'(z丨f)ood' 则匹配 "zood" 或 "food"。
|*|匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
|+|匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
|{n}|n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
|{n,m}|m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。