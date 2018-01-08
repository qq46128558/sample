<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$qb=app::get('base')->database()->createQueryBuilder();
$parameter="%服务%"; 

$qb=app::get('base')->database()->createQueryBuilder();
$app_id='debugbar';
$status='uninstalled';
$qb->select('*')
        ->from('base_apps')
        ->where("app_id=?")
        ->andWhere("status=?")
        ->setParameter(0,$app_id)
        ->setParameter(1,$status);
$result=$qb->execute()->fetchAll();
var_dump($result);
