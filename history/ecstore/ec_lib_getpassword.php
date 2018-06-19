<?php
define('ROOT_DIR',realpath(__DIR__.'/../../ecstore/'));
require_once ROOT_DIR.'/app/base/kernel.php';
require_once ROOT_DIR.'/app/base/autoload.php';
require_once ROOT_DIR.'/config/config.php';
require_once ROOT_DIR.'/app/base/ego/ego.php';
require_once ROOT_DIR.'/config/mapper.php';
require_once ROOT_DIR.'/app/base/defined.php';
error_reporting(E_ALL ^ E_NOTICE);

// ecstore密码机制
// 三个参数组合：密码先MD5加密+用户名+注册时间
$string_md5 = md5(md5('123456').'admin'.'1487124231');
$front_string = substr($string_md5,0,31);//截取了一位
$end_string = 's'.$front_string;

var_dump($end_string);
// seaa0fe00d9f94137ff6b4959433f1f7