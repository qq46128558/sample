<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';


$qb=app::get('base')->database()->createQueryBuilder();
$qb->select('shop_id,shop_name,shop_type')
    ->from('sysshop_shop')
    ->orderBy('shop_type','asc')
    // ->addOrderBy('shop_name','ASC NULLS FIRST'); //未执行成功
    ->addOrderBy('shop_id','asc');
$result=$qb->execute()->fetchAll();
var_dump($result);