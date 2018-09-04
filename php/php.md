## php命令行参数

#### php版本
	php -v

#### php的ini文件位置
	php --ini

#### 执行php代码
	php -r "echo 'abc';"

#### 检查php文件的语法
	php -l index.php

#### 项目应用记录
~~~php
// array_push — 将一个或多个单元压入数组的末尾（入栈）
array_push($behaviors['verbFilter']['actions']['index'],'POST');

// debug_backtrace — 产生一条回溯跟踪(backtrace)
// 2: exlude ["object"] AND ["args"], 2: 限制返回堆栈帧的数量
$backtrace=debug_backtrace(2,2);
// array(0=>array('file'=>'/data/www/yii/api/modules/tp/controllers/TestController.php','line'=>50,'function'=>'responseSuccess','class'=>'common\\core\\PubFunction','type'=>'::',),1=>array('function'=>'actionFormat','class'=>'api\\modules\\tp\\controllers\\TestController','type'=>'->',),)",

// long2ip — 将长整型转化为字符串形式带点的互联网标准格式地址（IPV4）
// ip2long — 将 IPV4 的字符串互联网协议转换成长整型数字

// 得到一个对象是哪个类的实例
get_class(obj);

// 得到一个对象的类型
gettype(1);

~~~