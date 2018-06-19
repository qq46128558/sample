<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$qb=app::get('base')->database()->createQueryBuilder();

$qb->select("*")
    ->from('base_apps','a')
    ->where ('a.status=?')
    ->orderBy('a.app_id','desc')
    ->setParameter(0,'uninstalled');

// $result=$qb->execute()->fetchAll();
// var_dump($result);
var_dump($qb->getSQL());