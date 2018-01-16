
<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

// 使用rpcCall内部直接调用接口
// url: xxx/index.php/api
$params=array('fields'=>'*');
$showapi=app::get('systrade')->rpcCall('trade.get.list',$params);
var_dump($showapi);
// url: xxx/index.php/topapi 暂未知如何调用