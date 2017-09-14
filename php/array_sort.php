<?php
error_reporting(~E_NOTICE);
//根据传入的数组和数组中值的键值，将对数组的键进行替换
function array_bind_key($array, $key )
{
foreach( (array)$array as $value )
{
    if( !empty($value[$key]) )
    {   
        $k = $value[$key];
        $result[$k] = $value;
    }   
}
return $result;
}

//按grade排序的实现
$data = array(
    '60'=>array("id"=>'60',"grade"=>'c',"name"=>'jason'),  
    '30'=>array("id"=>'30',"grade"=>'a',"name"=>'bob'),  
    '90'=>array("id"=>'90',"grade"=>'b',"name"=>'kate')  
);
foreach($data as $key=>$value){
    //排序关键点
    $grade[$key] = $value['grade'];
}
//但数字键名会被重新索引
array_multisort($grade,SORT_ASC,$data);
// var_dump($data);exit();
//将序号key绑定为指定字段
$data=array_bind_key($data,'id');
var_dump($data);