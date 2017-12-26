<?php
$timestamp=strtotime(date('1969-01-01 16:36:01'));
if ($timestamp){
echo $timestamp."<br>";
$date=date('Y-m-d H:i:s',$timestamp);
echo $date."<br>";
}else{
    var_dump($timestamp);
}

$timestamp=strtotime(date('2039-01-01 16:36:01'));
if ($timestamp){
echo $timestamp."<br>";
$date=date('Y-m-d H:i:s',$timestamp);
echo $date."<br>";
}else{
    var_dump($timestamp);
    echo 'Linux系统(centos6.8 x64)测试可以显示';
}
