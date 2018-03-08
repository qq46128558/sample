<?php
/**
 * 获取公众号的自动回复规则
 * 
 * @version 1.0
 * 
 */

 
require_once './https_method.php';
$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/cgi-bin/get_current_autoreply_info?access_token=$access_token";
$value=https_get($url);

echo $value;