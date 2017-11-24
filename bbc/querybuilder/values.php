<?php
require_once __DIR__.'/../../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../../b2b2c/bootstrap/start.php';

$queryBuilder=app::get('base')->database()->createQueryBuilder();
echo 'please refer to the source code.';
// Example
/*
$queryBuilder
->insert('users')
->values(
array(
'name' => '?',
'password' => '?'
)
)
->setParameter(0, $username)
->setParameter(1, $password);// INSERT INTO users (name, password) VALUES (?, ?)

$queryBuilder
->insert('users')
->setValue('name', '?')
->setValue('password', '?')
->setParameter(0, $username)
->setParameter(1, $password);

$queryBuilder
->insert('users')
->values(
array(
'name' => '?'
)
)
->setParameter(0, $username);// INSERT INTO users (name) VALUES (?)

if ($password) {
$queryBuilder
->setValue('password', '?')
->setParameter(1, $password)
;
// INSERT INTO users (name, password) VALUES (?, ?)}


$queryBuilder
->insert('users');// INSERT INTO users () VALUES ()
*/