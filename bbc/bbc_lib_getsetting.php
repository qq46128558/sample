<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';


// base_setting 表操作
// 设置
// app::get('system')->setConf('setSmsSign',array('sign'=>'拉普达'));

// 读取
$setSmsSign=app::get('system')->getConf('setSmsSign');
var_dump($setSmsSign);


// php配置文件
// 读取
$data=config::get('database.connections.default.host');
var_dump($data);

// 设置
// 在程序运行时设置的配置值只在本次请求中有效，不会对以后的请求造成影响。
$result=config::set('database.connections.default.host','192.168.239.138');
var_dump($result);
$data=config::get('database.connections.default.host');
var_dump($data);
