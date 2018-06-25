<?php
$app_key="5EC3009052005867E016BE59E6AA2D90";
$app_secret="9eb78cd1d9ef4816a853ead79b59ce96";
$refresh_token="3cda3b41-061e-4710-b355-4097d24d2b4a";

$url='https://oauth.jd.com/oauth/token?';
$url.="client_id=$app_key";
$url.="&client_secret=$app_secret";
$url.="&response_type=code";
$url.="&grant_type=refresh_token";
$url.="&refresh_token=$refresh_token";
$url.="&scope=read";
$url.="&state=0";

$ch=curl_init();
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
//curl_setopt($ch,CURLOPT_POST,1);
curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,false);
//    curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,1);
curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,false);
curl_setopt($ch,CURLOPT_URL,$url);
//curl_setopt($ch,CURLOPT_POSTFIELDS,$postdata);
$output=curl_exec($ch);
curl_close($ch);
echo $output;

// { "access_token": "35edcec6-5906-4ce6-ad50-f553de8ff284", "code": 0, "expires_in": 86399, "refresh_token": "3cda3b41-061e-4710-b355-4097d24d2b4a", "time": "1523362921279", "token_type": "bearer", "uid": "2805439555", "user_nick": "" }