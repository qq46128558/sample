<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

//配置连接的IP、端口、以及相应的数据库  
$server=array(
'host'=>'127.0.0.1',
'port'=>6379,
'password'=>'',
//'database'=>15
);  
try{
        $redis = new Predis\Client($server);
        echo $redis->ping();
}catch(Exception $ex){
        echo $ex->getMessage();
}