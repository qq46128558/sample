## php命令行参数

#### php版本
	php -v

#### php的ini文件位置
	php --ini

#### 执行php代码
	php -r "echo 'abc';"

#### 检查php文件的语法
	php -l index.php



#### php.ini
~~~php
// post 表单数据的最大允许值
post_max_size 
// 上传文件最大允许值
upload_max_filesize 
~~~


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

// ucfirst — 将字符串的首字母转换为大写
string ucfirst ( string $str )

// ucwords — 将字符串中每个单词的首字母转换为大写
// 默认：$delimiters 空格符、制表符、换行符、回车符、水平线以及竖线
string ucwords ( string $str [, string $delimiters = " \t\r\n\f\v" ] )

// str_replace — 子字符串替换
mixed str_replace ( mixed $search , mixed $replace , mixed $subject [, int &$count ] )

// array_flip — 交换数组中的键和值
array array_flip ( array $array )

// substr — 返回字符串的子串
string substr ( string $string , int $start [, int $length ] )

// uniqid — 生成一个唯一ID
string uniqid ([ string $prefix = "" [, bool $more_entropy = false ]] )

// md5_file — 计算指定文件的 MD5 散列值
string md5_file ( string $filename [, bool $raw_output = FALSE ] )

// unlink — 删除文件
bool unlink ( string $filename [, resource $context ] )
~~~

#### PHP重写原则
- final修饰的类方法不可被子类重写
- PHP是否重写父类方法只会根据方法名是否一致判断（5.3以后重写父类方法参数个数必须一致）
- 重写时访问级别只可以等于或者宽松于父类 不可提升访问级别
	- 父类的public方法不能被子类重写为protected或者private，protected方法不能被重写为private，可以宽松er，不可以严格er
- parent::getPicturesrc($imageID); // 调用父类的方法


#### 修饰符
|修饰符|说明|
|-|-|
|final|不可重写|
|static|静态|
|public|所有可访问|
|protected|类内/子类可访问|
|private|类内可访问|


#### [PHP中的静态方法和非静态方法调用方式](https://blog.csdn.net/u010250863/article/details/59542688 "https://blog.csdn.net/u010250863/article/details/59542688")
- 非静态方法的调用方式
	- self::methodName() (方法中不含$this)
	- className::methodName() (方法中不含$this)
	- $obj->methodName()
- 静态方法内调用非静态方法
	- self::methodName() (方法中不含$this)
	- className::methodName() (方法中不含$this)
- 非静态属性是不能用className::propertyName,方式调用的
- 对象也不可以直接调用静态属性,静态属性属于类


#### json格式判断
~~~php
// 判断数据不是JSON格式
return is_null(json_decode($str));

// 判断数据是合法的json数据: (PHP版本大于5.3)
json_decode($string);
return (json_last_error() == JSON_ERROR_NONE);
//  json编解码所操作字符串必须是UTF8的
~~~


### 允许跨域请求
	// php控制器中设置
	// 允许任意域名发起的跨域请求
	header("Access-Control-Allow-Origin: *"); 
	//有一些请求还是会出错,再加这句,多个值用逗号隔开 设置允许跨域的header属性
	header('Access-Control-Allow-Headers: X-Requested-With,X_Requested_With'); 