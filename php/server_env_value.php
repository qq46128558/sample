<?php
$arrServer=array(
	array(
		'name'=>'$_SERVER[\'argv\']',
		'desc'=>'传递给该脚本的参数',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'argc\']',
		'desc'=>'传递给程序的命令行参数的个数',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'AUTH_TYPE\']',
		'desc'=>'当 PHP 运行在 Apache 模块方式下，并且正在使用 HTTP 认证功能，这个变量便是认证的类型',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'DOCUMENT_ROOT\']',
		'desc'=>'当前运行脚本所在的文档根目录',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'GATEWAY_INTERFACE\']',
		'desc'=>'CGI 规范的版本',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'HTTP_ACCEPT_LANGUAGE\']',
		'desc'=>'浏览器语言',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'HTTP_ACCEPT\']',
		'desc'=>'当前请求的 Accept: 头部的内容',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'HTTP_ACCEPT_CHARSET\']',
		'desc'=>'当前请求的 Accept-Charset: 头部的内容',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'HTTP_ACCEPT_ENCODING\']',
		'desc'=>'当前请求的 Accept-Encoding: 头部的内容',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'HTTP_CONNECTION\']',
		'desc'=>'当前请求的 Connection: 头部的内容。例如：“Keep-Alive”',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'HTTP_HOST\']',
		'desc'=>'当前请求的 Host: 头部的内容',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'HTTP_REFERER\']',
		'desc'=>'链接到当前页面的前一页面的 URL 地址',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'HTTP_USER_AGENT\']',
		'desc'=>'当前请求的 User_Agent: 头部的内容',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'HTTPS\']',
		'desc'=>'如果通过https访问,则被设为一个非空的值(on)，否则返回off',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'PATH_TRANSLATED\']',
		'desc'=>'当前脚本所在文件系统（不是文档根目录）的基本路径',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'PHP_SELF\']',
		'desc'=>'正在执行脚本的文件名',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'PHP_AUTH_USER\']',
		'desc'=>'当 PHP 运行在 Apache 模块方式下，并且正在使用 HTTP 认证功能，这个变量便是用户输入的用户名',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'PHP_AUTH_PW\']',
		'desc'=>'当 PHP 运行在 Apache 模块方式下，并且正在使用 HTTP 认证功能，这个变量便是用户输入的密码',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'QUERY_STRING\']',
		'desc'=>'查询(query)的字符串',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'REMOTE_ADDR\']',
		'desc'=>'当前用户 IP',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'REMOTE_HOST\']',
		'desc'=>'当前用户主机名',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'REMOTE_PORT\']',
		'desc'=>'端口',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'REQUEST_URI\']',
		'desc'=>'URL',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'REQUEST_METHOD\']',
		'desc'=>'访问页面时的请求方法',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'SCRIPT_FILENAME\']',
		'desc'=>'当前执行脚本的绝对路径名',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'SCRIPT_NAME\']',
		'desc'=>'包含当前脚本的路径。这在页面需要指向自己时非常有用',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'SERVER_NAME\']',
		'desc'=>'服务器主机的名称',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'SERVER_SOFTWARE\']',
		'desc'=>'服务器标识的字串',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'SERVER_PROTOCOL\']',
		'desc'=>'请求页面时通信协议的名称和版本',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'SERVER_ADMIN\']',
		'desc'=>'管理员信息',
		'display'=>'N',
	),
	array(
		'name'=>'$_SERVER[\'SERVER_PORT\']',
		'desc'=>'服务器所使用的端口',
		'display'=>'Y',
	),
	array(
		'name'=>'$_SERVER[\'SERVER_SIGNATURE\']',
		'desc'=>'包含服务器版本和虚拟主机名的字符串',
		'display'=>'N',
	),
	/*
	array(
		'name'=>'',
		'desc'=>'',
		'display'=>'Y',
	),
	*/
);

foreach ($arrServer as $value){
	$a='';
	if ($value['display']=='Y')
		eval("\$a=".$value['name'].";");
	//$a=$_SERVER['HTTP_ACCEPT_LANGUAGE'];
	echo $value['name']."(".$value['desc']."):".$a."<br>";
}