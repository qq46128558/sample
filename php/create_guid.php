<?php

/* 生成像GUID的随机数
int mt_rand  ( int $min  , int $max  )
返回 0 到 mt_getrandmax() 2147483647 之间的伪随机数。例如想要 5 到 15（包括 5 和 15）之间的随机数，用 mt_rand(5, 15)。

string uniqid  ([ string $prefix  = ""  [, bool $more_entropy  = false  ]] )
获取一个带前缀、基于当前时间微秒数的唯一ID。 
prefix为空，则返回的字符串长度为13。more_entropy 为 TRUE ，则返回的字符串长度为23。 

string md5  ( string $str  [, bool $raw_output  = false  ] )
计算字符串的 MD5 散列值 
以 32 字符十六进制数字形式返回散列值。 
*/
function create_guid(){
    $charid=strtoupper(md5(uniqid(mt_rand(), true)));
    // echo $charid;
    $hyphen = chr(45);// "-"
    $uuid = substr($charid, 6, 2).substr($charid, 4, 2).substr($charid, 2, 2).substr($charid, 0, 2).$hyphen.substr($charid, 10, 2).substr($charid, 8, 2).$hyphen.substr($charid,14, 2).substr($charid,12, 2).$hyphen.substr($charid,16, 4).$hyphen.substr($charid,20,12);
    return $uuid;
}

// create_guid();
echo create_guid();