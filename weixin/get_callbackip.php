<?php
/**
 * 使用公众平台接口，获取到微信回调服务器的IP
 * 用于在服务上ping 测试，检查服务器到微信回调用服务器的网络质量情况 
 * access_token 从文件中获取, 如过期则执行 get_access_token.php获取
 * @version 1.0
 */


$access_token=file_get_contents('./token.txt');
// $access_token="";
$url="https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=$access_token";

$ch=curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);

$data=json_decode(curl_exec($ch),1);
var_dump($data);
curl_close($ch);