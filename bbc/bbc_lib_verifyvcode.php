<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

/*参考源码:app/system/lib/data/user/vcode.php*/
$account='peter';
$type='register';
$obj=kernel::single('system_data_user_vcode');

//校验验证码
$result=$obj->verify('525640',$account,$type);
//成功返回数组,失败返回false
var_dump($result);
