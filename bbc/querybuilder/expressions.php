<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$qb=app::get('base')->database()->createQueryBuilder();

$qb->select('*')
    ->from('base_apps')
    ->where(
        $qb->expr()->andX(
            $qb->expr()->eq('local_ver','?'),
            $qb->expr()->eq('status','?')
        )
    )
    ->setParameter(0,'0.1')
    ->setParameter(1,'uninstalled');
$result=$qb->execute()->fetchAll();
var_dump($result);