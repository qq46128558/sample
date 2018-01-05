<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$email='support@yn-ce.com';
$qb=app::get('base')->database()->createQueryBuilder();
$qb->select('app_id','app_name')
    ->from('base_apps')
    ->where('author_email=?')
    ->setParameter(0,$email);
$result=$qb->execute()->fetchAll();
var_dump($result);

// add by peter 2018-01-05
// 如果是数值字段,变量传入字符值,发现会查询全部