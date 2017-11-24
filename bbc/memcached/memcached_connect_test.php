<?php
require_once __DIR__.'/bootstrap/autoload.php';
require_once __DIR__.'/bootstrap/start.php';

//需要安装php-memcache56
$memcache_obj = new Memcache;
$result=$memcache_obj->connect('127.0.0.1', 11211);
if ($result){
        echo 'Connect succeed.';
        $memcache_obj->close();
}else{
        echo 'Connect failed.';
}