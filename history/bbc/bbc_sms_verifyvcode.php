<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

/*校验短信验证码*/
$vcodeData=userVcode::verify('611601','13928016056','signup');
var_dump($vcodeData);