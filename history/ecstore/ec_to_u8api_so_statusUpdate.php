<?php
/*window下测试:开启 php.ini中的 extension=php_soap.dll*/
/*linux下测试:安装php-soap,修改php.ini,增加soap.extension='/usr/lib64/php/modules/soap.so'*/

//一统项目调用U8修改销售订单状态, 接口测试
try{
	$wsdl ="http://web.kingzest.com/webserviceshx/WebService.asmx?wsdl";
	$client = new SoapClient($wsdl);
	$output = $client->changestatus('170606162017027','部分付款','是');
	var_dump($output);
} catch (Exception $ex){
	echo $ex->getMessage();
}
