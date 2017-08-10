<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

/*发送短信验证码*/
echo kernel::single('topc_passport')->sendVcode('13928016056','signup');

/*sendType类型
activation
reset
forgot
unreset
signup //手机注册
depost_forgot //支付密码忘记密码
*/

/*调用邮件验证相关 都是BBC预置好的信息
$obj=kernel::single('topc_passport');
$result=$obj->sendEmailVcode('activation','46128558@qq.com');
var_dump($result);
*/
