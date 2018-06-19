
<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';
//bbc框架中使用断言
//需启用回调函数
assert_options(ASSERT_CALLBACK,'assert_callback');

$a='abc';
assert(is_numeric($a),'要求参数是数值');

function assert_callback($path,$line,$unknow,$description){
        echo "$description:failed,$path,第${line}行<br>";
}
echo "这是继续的执行代码.<br>";