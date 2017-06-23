<?php
/*(商家)获取单笔交易信息, 需要Oauth认证, 未实现*/
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

$params = array(
  
	'method'=>'trade.shop.get',
	'format'=>'json', //返回数据是json格式的，目前只支持json
	'v'=>'v1', //标识该接口的版本
	'shop_id'=>3,
  'tid'=>'1601261431290002',
  'fields'=>'*',
  'timestamp'=>time(),
  'sign_method'=>'md5',
  'sign_type'=>"MD5", 
  // 'oid'=>'',

  /*
  'client_id'=>'nk2l73rt',
  // 'client_id'=>'j22imnvy',
  'ApiId'=>'qwddqhx2',
  'RequestId'=>'4dlzcqpdfbb6jkor',
  'ApiMethod'=>'trade.shop.get',
  'Key'=>'nk2l73rt',
  */

  /*
  'method'=>'open.oauth.login',
  'format'=>'json',
  'v'=>'v1',
  'loginname'=>'onexbbc',
  'password'=>'demo123',
  'timestamp'=>time(),
  'sign_type'=>'MD5',
  'oauth_type'=>'seller',
  */
  
);

// $token='2ed6c12c7b8a1a2c84b064ebe47263152c0b655355470714862bcc8dbdd949b2';
$token='';
$params['sign'] = strtoupper(md5(strtoupper(md5(assemble($params))).$token));
//echo $params['sign'];
//此处结尾是api
$url = "192.168.239.138/index.php/api";
// $url="192.168.239.138:8080/api/systrade/"
$output = curl($url,$params);
echo unicode_decode($output);


/*资料记录
app/topdev/controller/apis.php
app/topdev/view/apis/test.html

app/systrade/api/getTradeInfoByShop.php
config/apis.php

app/system/middleware/checkApiSystemParams.php

app/base/lib/rpc/validate.php
*/

