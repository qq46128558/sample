<?php
define('ROOT_DIR',realpath(__DIR__.'/../../ecstore/'));
require_once ROOT_DIR.'/app/base/kernel.php';
require_once ROOT_DIR.'/app/base/autoload.php';
require_once ROOT_DIR.'/config/config.php';
require_once ROOT_DIR.'/app/base/ego/ego.php';
require_once ROOT_DIR.'/config/mapper.php';
require_once ROOT_DIR.'/app/base/defined.php';
error_reporting(E_ALL ^ E_NOTICE);


$db=kernel::database();
var_dump($db->select('select 1 from dual'));
