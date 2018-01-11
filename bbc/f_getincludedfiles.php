<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

// array get_included_files  ( void )
// 返回所有被 include 、 include_once 、 require  和 require_once  的文件名。 
var_dump(get_included_files());  