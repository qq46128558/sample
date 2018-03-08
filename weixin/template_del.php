<?php
/**
 * 删除模板
 * 
 * @version 1.0
 * 
 */

require_once './https_method.php';
$json=<<<STR
{
    "template_id" : "KKFX3HJjRA0Z3CcVvOW4vawcbDnRORRpy4nO8CR8ahI"
}
STR;
$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/cgi-bin/template/del_private_template?access_token=$access_token";
$value=https_post($url,$json);

echo $value;