<?php

//Unicode解码函数
function replace_unicode_escape_sequence($match) {
    return mb_convert_encoding(pack('H*', $match[1]), 'UTF-8', 'UCS-2BE');
}
function unicode_decode($str) {
 return preg_replace_callback('/\\\u([0-9a-f]{4})/i', 'replace_unicode_escape_sequence', $str); 
}

$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, 'http://192.168.239.136/apply/dev/main/submit');
curl_setopt($curl, CURLOPT_HEADER, 0);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER,0);
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST,2);
// $headers = array();
// $headers[] = 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36';
// curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
curl_setopt($curl,CURLOPT_POST,1);
$postData=array(
    "activityId"=>'5aa64336f8990b4d9c82fdcb',
    "user"=>'{"userId":"oRnBdwv0rXOiUWFt_UvC1ZyMBJuo","nickName":"Peter","headImgUrl":"http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJ4gfafuPCFibAfhWc5d41EI4ad6KWfP4IGbIzouLYJhUqQufsS1brmNZSsCEEoTPica5Ywic9F5dLTQ/132"}',
    "data"=>'{"name":"guiwen","phone":"13928016056","product":"蟹宝盒","area":"珠海"}',
    "mobile"=>"13928016056",
    "shareUserId"=>"",
);
curl_setopt($curl, CURLOPT_POSTFIELDS, $postData);

$data = curl_exec($curl);
curl_close($curl);
echo unicode_decode($data);

