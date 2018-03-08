<?php
/**
 * 获取模板列表
 * 
 * @version 1.0
 * 
 */

require_once './https_method.php';
$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=$access_token";
$value=https_get($url);

echo $value;