<?php
/**
 * 获取素材列表
 * 使用测试号测试
 * @version 1.0
 */

function https_post($url,$postdata)
{
   $ch=curl_init();
   curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
   curl_setopt($ch,CURLOPT_POST,1);
   curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
   curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
   curl_setopt($ch,CURLOPT_URL,$url);
   curl_setopt($ch,CURLOPT_POSTFIELDS,$postdata);
   $output=curl_exec($ch);
   curl_close($ch);
   return $output;
}

$json=<<<STR
{
    "type":"image",
    "offset":0,
    "count":20
}
STR;

$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=$access_token";
$value=https_post($url,$json);

echo $value;