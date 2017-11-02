<?php
assert_options(ASSERT_ACTIVE,1); // 启用 assert()  断言
assert_options(ASSERT_WARNING,1); // 为每个失败的断言产生一个 PHP 警告（warning）
assert_options(ASSERT_BAIL,0); // 在断言失败时中止执行
assert_options(ASSERT_QUIET_EVAL,1); // 在断言表达式求值时禁用 error_reporting

$a='abc';
assert(is_numeric($a),'要求参数是数值');

echo '这是继续执行的代码.<br>';


