<?php
// 数组去重
// 去除数组中重复的元素值
$value=array('A','A','B','B','C','中文','中文','数学');

$value=array_unique($value,SORT_STRING);
var_dump(array_values($value));

// 1. SORT_REGULAR  - compare items normally (don't change types) 
// 2. SORT_NUMERIC  - compare items numerically 
// 3. SORT_STRING  - compare items as strings 
// 4. SORT_LOCALE_STRING  - compare items as strings, based on the current locale. 
