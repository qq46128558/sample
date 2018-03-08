<?php
/**
 * 设置所属行业
 * 
 * @version 1.0
 * 
 */

require_once './https_method.php';
$json=<<<STR
{
    "industry_id1":"1",
    "industry_id2":"4"
}
STR;
$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token=$access_token";
$value=https_post($url,$json);

echo $value;