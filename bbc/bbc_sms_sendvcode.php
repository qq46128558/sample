<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

/*发送短信验证码*/
echo kernel::single('topc_passport')->sendVcode('13928016056','signup');

// app/topm/lib/passport.php (或 app/topc/lib/passport.php) 的 sendVcode()方法
// app/system/lib/data/user/vcode.php, send_sms()方法
// app/system/lib/messenger.php 
//     send($sendTo,$title,$contents,$config);
//     sendSms($mobile,$tmpl,$data);    

/*sendType类型
activation 激活(身份验证?)
reset 重置手机号或者邮箱
forgot 找回密码
unreset 重置手机号或者邮箱
signup //手机注册
depost_forgot //支付密码忘记密码
auth_shop //商家安全验证
findPw_shop //商家找回密码
depost_forgot //支付密码忘记密码
*/

/*调用邮件验证相关 都是BBC预置好的信息
$obj=kernel::single('topc_passport');
$result=$obj->sendEmailVcode('activation','46128558@qq.com');
var_dump($result);
*/
