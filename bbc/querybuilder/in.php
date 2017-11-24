<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$qb=app::get('base')->database()->createQueryBuilder();

$parameter=array("'base'","'dbeav'"); //字符串的in,双引号内有单引号, 如果是数值型则不用单引号
$qb=app::get('base')->database()->createQueryBuilder();
$qb->select('*')
        ->from('base_apps')
        ->where($qb->expr()->in('app_id',$parameter));
$result=$qb->execute()->fetchAll();
var_dump($result);
