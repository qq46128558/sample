<?php
$app_key="5EC3009052005867E016BE59E6AA2D90";
$redirect_uri="http://47.106.126.78/test/jdcode.php";

$url="https://oauth.jd.com/oauth/authorize?";
$url.="response_type=code";
$url.="&client_id=".$app_key;
$url.="&redirect_uri=".$redirect_uri;
$url.="&state=0";
$url.="&scope=read";
// view 可选 移动端授权，该值固定为wap；非移动端授权，无需传值

echo $url;

// http://jos.jd.com/doc/channel.htm?id=152