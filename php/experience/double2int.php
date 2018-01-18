<?php
// php浮点数转整型后不正确的问题
// http://www.jb51.net/article/80726.htm

$amount=2.3;
$value=$amount*100;

$errorValue=intval($value);
echo 'Error int result: '.$errorValue;
var_dump($errorValue);

$correctValue=bcmul($value,1);
$correctValue=intval($correctValue);
echo '<br>Correct int result: '.$correctValue;
var_dump($correctValue);

// bc是Binary Calculator的缩写。bc*函数的参数都是操作数加上一个可选的 [int scale]，比如
// string bcadd(string $left_operand, string $right_operand[, int $scale])，
// 如果scale没有提供，就用bcscale的缺省值。这里大数直接用一个由0-9组成的string表示，计算结果返回的也是一个 string。

// bcadd — 将两个高精度数字相加 
// bccomp — 比较两个高精度数字，返回-1, 0, 1 
// bcdiv — 将两个高精度数字相除 
// bcmod — 求高精度数字余数 
// bcmul — 将两个高精度数字相乘 
// bcpow — 求高精度数字乘方 
// bcpowmod — 求高精度数字乘方求模，数论里非常常用 
// bcscale — 配置默认小数点位数，相当于就是Linux bc中的”scale=” 
// bcsqrt — 求高精度数字平方根 
// bcsub — 将两个高精度数字相减