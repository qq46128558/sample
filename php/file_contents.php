<?php
define('ROOT_DIR',realpath(__DIR__.'/../../ecstore/'));
require_once ROOT_DIR.'/app/base/kernel.php';
require_once ROOT_DIR.'/app/base/autoload.php';
require_once ROOT_DIR.'/config/config.php';
require_once ROOT_DIR.'/app/base/ego/ego.php';
require_once ROOT_DIR.'/config/mapper.php';
require_once ROOT_DIR.'/app/base/defined.php';
error_reporting(E_ALL ^ E_NOTICE);

$rows=app::get('base')->model('setting')->getList('*');

// 和依次调用 fopen() ， fwrite()  以及 fclose()  功能一样。 
$result=file_put_contents('sample.txt',var_export($rows,true),FILE_APPEND);
echo $result;

$result=file_get_contents('sample.txt');
var_dump($result);