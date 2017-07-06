<?php
/* 参考示例代码
$objSoapClient = new SoapClient("http地址.asmx?wsdl");
$param=array("参数名"=>"参数值");
$out=$objSoapClient->入口方法名($param);
$data=$out->入口方法名Result;
var_dump($data);
*/
$objSoapClient = new SoapClient("http://121.33.215.93:8001/AsnRsnWhgoods.asmx?wsdl");
$param=array("key1"=>"value1");
$out=$objSoapClient->GetBillNoBySYS($param);
$data=$out->GetBillNoBySYSResult;
var_dump($data);
