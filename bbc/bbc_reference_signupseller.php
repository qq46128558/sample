<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';


$params['login_account']='account1';
$params['login_password']='admin123';
$params['psw_confirm']='admin123';
$params['name']='测试账号1';
$params['mobile']='13928010001';
$params['email']='account1@yn-ce.com';
$result=shopAuth::signupSeller($params);
var_dump($result);

// 就写这两个表
// sysshop_account
// sysshop_seller
