<?php
/**
 * 获取用户基本信息(UnionID机制)
 * 
 * @version 1.0
 * 
 * 返回的: unionid	只有在用户将公众号绑定到微信开放平台帐号后，才会出现该字段。
 * 
 */

 
require_once './https_method.php';

$access_token=file_get_contents('./t_token.txt');
$openid='o0ZAd1V-_YTIf2SXA3prYu_X6Cr0';
$url="https://api.weixin.qq.com/cgi-bin/user/info?access_token=$access_token&openid=$openid&lang=zh_CN";
$value=https_get($url);

echo $value;