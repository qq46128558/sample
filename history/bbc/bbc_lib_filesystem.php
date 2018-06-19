<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

// filesystem 类, 可以操作文件, config::get读取配置文件值就是用这个类, 前提是配置文件是用return返回配置数组的
$files = kernel::single('base_filesystem');
// 授权文件
$certi=__DIR__.'/../../b2b2c/config/certi.php';
// require $certi;

// 判断文件存在
if ($files->exists($certi))
{
	// 读文件内容
	$content=$files->get($certi);
	// 引入文件
	$items=$files->getRequire($certi);
	
}
// 文件内容
var_dump($content);
// 引入文件成功
var_dump($items);
// 但读不到内容, 目前不知为什么, xdebug跟踪F11显示该值为: /* uninitialized */
// 直接引入文件,则可以读取,暂未解决
var_dump($certificate);


