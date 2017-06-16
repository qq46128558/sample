<?php
error_reporting(E_ALL & ~E_NOTICE);

//Unicode解码函数
function replace_unicode_escape_sequence($match) {
    return mb_convert_encoding(pack('H*', $match[1]), 'UTF-8', 'UCS-2BE');
}

function unicode_decode($str) {
 return preg_replace_callback('/\\\u([0-9a-f]{4})/i', 'replace_unicode_escape_sequence', $str); 
}


function assemble($params){
  if(!is_array($params)){
  return null;
  }
  ksort($params,2);
  foreach ($params as $key => $value) {
  if(is_null($value)){
  continue;
  }
  if(is_bool($value)){
  $value = ($value) ? 1 :0 ;
  }
  $sign .= $key . (is_array($value) ? assemble($value) : $value) ;
  }
  return $sign;
}

function curl($url,$post_data){
  $ch = curl_init();
  curl_setopt($ch ,CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  //POST数据
  curl_setopt($ch, CURLOPT_POST, 1);
  //POST的变量
  curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
  $output = curl_exec($ch);
  //打印获得的数据
  return $output;
}

$sysParams['method']='api.test';
$sysParams['timestamp']=time();
$sysParams['format']='json';
$sysParams['v']='v1';
$sysParams['sign_type']='MD5';

$apiParams=array();
$apiParams['fields']='*';
$apiParams['test_id']=2;
$params = array_merge($sysParams, $apiParams);

// $token='2ed6c12c7b8a1a2c84b064ebe47263152c0b655355470714862bcc8dbdd949b2';
$token='';
$params['sign'] = strtoupper(md5(strtoupper(md5(assemble($params))).$token));

//此处结尾是api
$url = "192.168.239.138/index.php/api";
$output = curl($url,$params);
echo unicode_decode($output);
