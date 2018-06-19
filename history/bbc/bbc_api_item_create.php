<?php
/*商品添加、编辑,无Oauth认证*/
error_reporting(E_ALL & ~E_NOTICE);

//Unicode解码函数
function replace_unicode_escape_sequence($match) {
    return mb_convert_encoding(pack('H*', $match[1]), 'UTF-8', 'UCS-2BE');
}

function unicode_decode($str) {
 return preg_replace_callback('/\\\u([0-9a-f]{4})/i', 'replace_unicode_escape_sequence', $str); 
}
/*在类中的写法
function unicode_decode($str) { 
  return preg_replace_callback('/\\\u([0-9a-f]{4})/i', 
    function($match){
      return mb_convert_encoding(pack('H*', $match[1]), 'UTF-8', 'UCS-2BE');
    }, $str);  
}
*/


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
	'method'=>'item.create',
	'format'=>'json', //返回数据是json格式的，目前只支持json
	'v'=>'v1', //标识该接口的版本
  'timestamp'=>time(),
  'sign_type'=>'MD5',
  'shop_id'=>2,
  'cat_id'=>24,
  'brand_id'=>6,
  'shop_cat_id'=>'16,',
  'title'=>'XXX我的电脑'.microtime(),
  'weight'=>2,
  'price'=>4499,
  'dlytmpl_id'=>12,
  'nospec'=>1,
  'store'=>'99', 
  'approve_status'=>'onsale', //上架
  // 'list_time'=>1510119694,
  'sku'=>'{"store":99,}',
);
$token='';
$params['sign'] = strtoupper(md5(strtoupper(md5(assemble($params))).$token));
//此处结尾是topapi
$url = "192.168.239.138/index.php/api";
$output = curl($url,$params);
echo unicode_decode($output);

