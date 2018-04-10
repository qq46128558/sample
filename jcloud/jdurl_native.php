<?php
$app_key="5EC3009052005867E016BE59E6AA2D90";
$redirect_uri="urn:ietf:wg:oauth:2.0:oob";

$url="https://oauth.jd.com/oauth/authorize?";
$url.="client_id=".$app_key;
$url.="&response_type=code";
$url.="&redirect_uri=".$redirect_uri;
$url.="&scope=read";
$url.="&state=0";
// view 可选 移动端授权，取值为wap；非移动端授权，无需传值

echo $url;

// Native Application授权流程，无法获取Refresh token，如果超过授权时效，需要重新授权
