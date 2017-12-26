<?php
$serialize=serialize('淘力网运营后台');
echo $serialize."<br>";
$unserialize=unserialize($serialize);
echo $unserialize."<br>";

echo '---------<br>';
$str='a:1:{s:32:"b2c_promotion_solutions_discount";a:1:{s:7:"percent";s:2:"50";}}';
echo $str;
$value=unserialize($str);
var_dump($value);