<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$qb=app::get('base')->database()->createQueryBuilder();
// 写法一
$parameter="%服务%"; 
$qb=app::get('base')->database()->createQueryBuilder();
$qb->select('*')
        ->from('base_apps')
        ->where($qb->expr()->orX(
            $qb->expr()->like('app_name','?'),
            $qb->expr()->like('description','?')
        ))
        ->setParameter(0,$parameter)
        ->setParameter(1,$parameter);
$result=$qb->execute()->fetchAll();
var_dump($result);
