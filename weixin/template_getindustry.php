<?php
/**
 * 获取设置的行业信息
 * 
 * @version 1.0
 * 
 */

require_once './https_method.php';
$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/cgi-bin/template/get_industry?access_token=$access_token";
$value=https_get($url);

echo $value;