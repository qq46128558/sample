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
  'method' => 'b2c.delivery.create',
  'order_bn'=>'170505143814430',//订单号
  'delivery_bn'=>'X170505143814430',//发货单号
  'ship_distinct'=>'蝶山区',//收货人所在地区
  'logi_name'=>'顺丰速运',//物流公司
  'ship_name'=>'Peter',//收货人
  'ship_states'=>'广西',//收货人所在省份
  'ship_city'=>'梧州市',//收货人所在城市
  'ship_addr'=>'桂林路001号2号楼306',//收货地址
  'ship_zip'=>'519001',//邮政编码
  'ship_mobile'=>'13928010001',//收货人手机
  'memo'=>'周末不收货',//订单备注
  'items'=>'[{"product_bn":"P4CB2BB43BEBED","product_name":"CLINIQUE 倩碧 眼部护理水凝霜 15ml","number":"1","batch_name":"39001"}]',
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

//var_dump(json_decode($params['items']));
