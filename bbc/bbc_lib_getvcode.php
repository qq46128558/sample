<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

/*参考源码:app/system/lib/data/user/vcode.php*/
$account='peter';
$type='register';
$obj=kernel::single('system_data_user_vcode');

/*可选用代码*/
// 校验重复发送
// $vcodeData = $obj->checkVcode($account,$type);

//生成六成验证码
$vcode=$obj->randomkeys(6);
$vcodeData['account'] = $account;
$vcodeData['vcode'] = $vcode;
$vcodeData['count']  += 1;
$vcodeData['createtime'] = date('Ymd');
$vcodeData['lastmodify'] = time();$data['vcode'] = $vcode;
//1分钟失效
$data['expires'] = 1;
$key = $obj->getVcodeKey($account,$type);
cache::store('vcode')->put($key, $vcodeData, 1);
//显示验证码
echo $vcode;

/*可选用代码*/
//设置短信验证码设置缓存,缓存为一天,用于重复发送校验,带@的不控制重复
// $smsConfData['count'] = $vcodeData['count'];
// $smsConfData['createtime'] = $vcodeData['createtime'];
// $smsConfData['lastmodify'] = $vcodeData['lastmodify'];
// $smsConfkey = $obj->getSmsConfCountKey($account,$type);
// cache::store('vcode')->put($smsConfkey, $smsConfData, 1440);

