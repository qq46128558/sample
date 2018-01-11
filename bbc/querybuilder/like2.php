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
            // 注意null值的like,会查不出内容,所以加个ifnull
            $qb->expr()->like("ifnull(app_name,'')",'?'),
            $qb->expr()->like("ifnull(description,'')",'?')
        ))
        ->setParameter(0,$parameter)
        ->setParameter(1,$parameter);
$result=$qb->execute()->fetchAll();
var_dump($result);
