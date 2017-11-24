<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$qb=app::get('base')->database()->createQueryBuilder();
$qb->select('dbver','count(1) as vercount')
    ->from('base_apps')
    ->groupBy('dbver')
    ->having('vercount>5');
$result=$qb->execute()->fetchAll();
var_dump($result);