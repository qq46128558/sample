<?php
error_reporting(E_ALL & ~E_NOTICE);
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

$params = array(
  'method' => 'b2c.order.search',
  'start_time' => '2016-01-01',
  'end_time' => '2018-01-01',
);

$token = "e19ee2eb76995e5a17cb6b4f315825fa0b2a3e4fccf6e5238f3ca4ae2ca7754a";

$v1=assemble($params);
echo "assemble:\n".$v1."\n";
$v2=md5($v1);
echo "md5:\n".$v2."\n";
$v3=strtoupper($v2).$token;
echo "token+:\n".$v3."\n";
$v4=md5($v3);
echo "md5:\n".$v4."\n";

$params['sign'] = strtoupper(md5(strtoupper(md5(assemble($params))).$token));
echo "final:\n".$params['sign']."\n";

$url = "192.168.239.138/index.php/api";
$output = curl($url,$params);
echo $output;
