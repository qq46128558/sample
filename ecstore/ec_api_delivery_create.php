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
  'task'=>time(), //对应表sdb_apiactionlog_apilog的日志编号
  'method' => 'b2c.delivery.create',
  'order_bn'=>'170503105491428',//订单号
  'delivery_bn'=>'170503105491428',//配送流水号,发货单号
  'delivery'=>'快递',
  'ship_distinct'=>'蝶山区',//收货人所在地区
  'money'=>0,//配送费用
  'is_protect'=>0,//是否保价 布尔型会sign error
  'logi_no'=>'123457',//物流单号
  'logi_name'=>'顺丰速运',//物流公司
  'ship_name'=>'Jason',//收货人
  'ship_states'=>'广西',//收货人所在省份
  'ship_city'=>'梧州市',//收货人所在城市
  'ship_addr'=>'桂林路001号2号楼306',//收货地址
  'ship_zip'=>'519001',//邮政编码
  'ship_tel'=>'021-66666666',//收货人电话
  'ship_mobile'=>'13928010001',//收货人手机
  'ship_email'=>'uuu@163.com',//收货人邮箱
  'memo'=>'周末不收货',//订单备注
  'member_id'=>'peter',//会员
  't_begin'=>time(),
  'buyer_uname'=>'John',//购买人 操作员
  'status'=>'succ',
  'items'=>'[{"product_bn":"P4CB2BB85A40AD","product_name":"芳草集 甘草排毒保湿面膜120G","number":"2","batch_name":"36999"},{"product_bn":"P58DA027EC92E9","product_name":"图片测试","number":"9","batch_name":"37000"}]',
);

$token = "e19ee2eb76995e5a17cb6b4f315825fa0b2a3e4fccf6e5238f3ca4ae2ca7754a";
/*
$v1=assemble($params);
echo "assemble:\n".$v1."\n";
$v2=md5($v1);
echo "md5:\n".$v2."\n";
$v3=strtoupper($v2).$token;
echo "token+:\n".$v3."\n";
$v4=md5($v3);
echo "md5:\n".$v4."\n";
*/

$params['sign'] = strtoupper(md5(strtoupper(md5(assemble($params))).$token));
//echo "final:\n".$params['sign']."\n";

$url = "192.168.239.138/index.php/api";
$output = curl($url,$params);
echo $output;


//需要调第二个接口:订单发货状态更新接口
$params = array(
  'task'=>time()+1, //对应表sdb_apiactionlog_apilog的日志编号
  'method' => 'b2c.order.ship_status_update',
  'order_bn'=>'170503105491428',
  'ship_status'=>1, //0(未发货) 1(已发货) 2(部分发货) 3(部分退货) 4(已退货)
  
);
$params['sign'] = strtoupper(md5(strtoupper(md5(assemble($params))).$token));
$url = "192.168.239.138/index.php/api";
$output = curl($url,$params);
echo $output;


//var_dump(json_decode($params['items']));
