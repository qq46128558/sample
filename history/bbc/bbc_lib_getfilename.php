<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

//查看类所属文件
$obj=new ReflectionClass('shopAuth');
echo $obj->getFilename();