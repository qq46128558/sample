<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

/*发送短信验证码*/
echo kernel::single('topc_passport')->sendVcode('13928016056','signup');
