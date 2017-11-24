<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$email='support@yn-ce.com';
$qb=app::get('base')->database()->createQueryBuilder();
$qb->select('a.app_id','a.app_name')
    ->from('base_apps','a')
    ->where('a.author_email=?')
    ->setParameter(0,$email);
$result=$qb->execute()->fetchAll();
var_dump($result);