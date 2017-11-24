<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$qb=app::get('base')->database()->createQueryBuilder();

$remote_config='abc';
$app_id='debugbar';
$qb->update('base_apps','a')
    ->set('a.description',"concat(a.description,'1')")
    ->set('a.remote_config','?')
    ->where('a.app_id=?')
    ->setParameter(0,$remote_config)
    ->setParameter(1,$app_id);    
$result=$qb->execute();
var_dump($result);
