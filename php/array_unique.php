<?php
// 数组去重
// array_unique — 移除数组中重复的值 
$value=array('A','A','B','B','C','中文','中文','数学');

$value=array_unique($value,SORT_STRING);
// array_values()  返回 input 数组中所有的值并给其建立数字索引。 
var_dump(array_values($value));

// 1. SORT_REGULAR  - compare items normally (don't change types) 
// 2. SORT_NUMERIC  - compare items numerically 
// 3. SORT_STRING  - compare items as strings 
// 4. SORT_LOCALE_STRING  - compare items as strings, based on the current locale. 


// ps: array_column — 返回数组中指定的一列 