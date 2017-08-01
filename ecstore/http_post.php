<?php
$page_no=1;
$url="http://121.41.161.136/efast/efast_api_gz/webservice/web/index.php?app_act=efast_baison_gz_api/sku_stock_list_get&app_nick=openapi&app_key=cc59dc8f14c63d3d4a44&app_secret=a8e8e897e9cbdb16d2cc924fd0bce727&page_no=".$page_no;
$post_data=array();//推送的参数

$ch=curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_POST,1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
//调用接口
$output = curl_exec($ch);
var_dump($output);

curl_close($ch);
$response_datas=json_decode($output,true);
var_dump($response_datas);