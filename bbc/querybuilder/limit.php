<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

// setFirstResult(6-1) 从第6条开始
// setMaxResults(5) 取5条
$qb=app::get('base')->database()->createQueryBuilder();
$qb->select('item_id','title')
    ->from('sysitem_item')
    ->setFirstResult(6-1)
    ->setMaxResults(5)
    ->orderBy('item_id','asc');
$result=$qb->execute()->fetchAll();
var_dump($result);
