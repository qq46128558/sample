<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

$objEmailconf = kernel::single('desktop_email_emailconf');
$config=$objEmailconf->get_emailConfig();
var_dump($config);