<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$qb=app::get('base')->database()->createQueryBuilder();
$parameter="%服务%"; 

$qb=app::get('base')->database()->createQueryBuilder();
$app_id1='debugbar';
$app_id2='dev';
$qb->select('*')
        ->from('base_apps')
        ->where("app_id=?")
        ->orWhere("app_id=?")
        ->setParameter(0,$app_id1)
        ->setParameter(1,$app_id2);
$result=$qb->execute()->fetchAll();
var_dump($result);
