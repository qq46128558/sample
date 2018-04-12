<?php
$app_key="5EC3009052005867E016BE59E6AA2D90";
$redirect_uri="http://47.106.126.78/test/jdcode.php";
$domain=urlencode("http://www.tlwok.com/");

$url="http://auth.jcloud.com/oauth/authorize?";
$url.="response_type=code";
$url.="&state=myststeid";
$url.="&client_id=".$app_key;
$url.="&redirect_uri=".$redirect_uri;
$url.="&scope=read";
$url.="&domain=$domain";
// view 可选 移动端授权，该值固定为wap；非移动端授权，无需传值

echo $url;

// http://jos.jd.com/doc/channel.htm?id=152