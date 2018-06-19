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

$params = array(
  'method' => 'b2c.order.search',
  'start_time' => '2014-01-01',
  'end_time' => '2018-01-01',
  );
  $token = "c0d5c21bb4a06c5bb1bd35755f08ec281699b93a362400f10d90290988707a3c";
  $params['sign'] = strtoupper(md5(strtoupper(md5(assemble($params))).$token));

var_dump($params['sign']);

