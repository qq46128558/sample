<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

$userId=80;
//生成ID示例: 2027 415 00006 0080
$startTime = 1388505600;//2014-01--1 做为初始年(够4位)(1388505600) (2017-01-01 1325347200)
//当前时间相距初始年的天数，4位可使用20年
$day =  floor( (time() - $startTime) / 86400);
//确定每90秒内的订单生成 一天总共有960个90秒，控制在三位 (这里的意思就是以每90秒为一个周期进行单号流水)
$minute = floor((time() - strtotime(date('Y-m-d')) ) / 90);
//原来代码为rand(0,9) (为每个90秒周期进行随机增量, 用到redis)
//这里用sysuser的场景, 应该按需修改config/redis.php或config/production/redis.php
$redisId = redis::scene('sysuser')->hincrby(date('Ymd'), $minute, rand(1,9));
//年份值4位, 90秒周期值3位, 周期增量流水值5位, 用户id值4位
//由于id一般是长整型, 所以$day前面不用补0
$id = $day. str_pad($minute,3,'0',STR_PAD_LEFT) . str_pad($redisId,5,'0',STR_PAD_LEFT) . str_pad($userId%10000,4,'0',STR_PAD_LEFT);//16位
//压力测试?
//$id = redis::scene('sysitem')->incr('stress_testing_tid');
echo $id;

