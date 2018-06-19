<?php
/* 单独使用BBC Predis的示例
 * 尚未找到windows版的地区存在哪里, linux的存在syslogistics:areaKvdata
 */

require_once __DIR__.'/../../b2b2c/vendor/predis/predis/autoload.php';
$server=array(
	'scheme'=>'tcp',
	'host'=>'127.0.0.1',
	'port'=>'6379',
	'database'=>0,
);
$client=new Predis\Client($server);
$client->set('myname','peter');
echo "ping: ".$client->ping()."<br>";
var_dump($client->keys('*'));
echo "type of 'syslogistics:areaFileContents': ".$client->type('syslogistics:areaFileContents')."<br>";
echo 'myname: '.$client->get('myname').'<br>';
echo 'system:net.handshake exists: '.$client->exists('system:net.handshake');
