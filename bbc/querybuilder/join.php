<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';


$qb=app::get('base')->database()->createQueryBuilder();
$shop_id=4;
$qb->select('c.shop_name','b.name','b.mobile','a.login_account')
    ->from('sysshop_account','a')
    ->leftJoin('a','sysshop_seller','b','a.seller_id=b.seller_id')
    ->leftJoin('b','sysshop_shop','c','b.shop_id=c.shop_id')
    ->where('b.shop_id=?')
    ->setParameter(0,$shop_id);
$result=$qb->execute()->fetchAll();
var_dump($result);