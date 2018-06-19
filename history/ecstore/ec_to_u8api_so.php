<?php
/*window下测试:开启 php.ini中的 extension=php_soap.dll*/
/*linux下测试:安装php-soap,修改php.ini,增加soap.extension='/usr/lib64/php/modules/soap.so'*/

//一统项目调用U8生成销售订单, 接口测试
$json = <<<u8api
	{"Office":"深圳办事处"
	,"Businessdate":"1496657804"
	,"OrderBy":"0118034"
	,"Memo":"湖南岳阳市岳阳县1234567890"
	,"B2BDocNo":"170605181664332"
	,"PaymentStatus":"未支付"
	,"MonCutomer":"否"
	,"Sender":"否"
	,"Pmtname":"首批100个打9折,鸡汁首批20个打7折,一统原创200ml本味鲜首批打折,1.96蒸鱼豉油首批打折"
	,"ItemCode":"0302001"
	,"Qty":40
	,"Amount":5877.6
	,"B2BLineNo":"229"}
u8api;
//"Price":146.94  不传入单价
$json = '{ "orders":[ '.$json;
$json .= " ]}";
try{
	$wsdl ="http://web.kingzest.com/webservices/WebService.asmx?wsdl";
	$client = new SoapClient($wsdl);
	$output = $client->AddInSt($json);
	$response_datas=json_decode($output,true);
	var_dump($response_datas);
} catch (Exception $ex){
	echo $ex->getMessage();
}
