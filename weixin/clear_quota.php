<?php
/**
 * 公众号调用或第三方平台帮公众号调用对公众号的所有api调用（包括第三方帮其调用）次数进行清零
 * 
 * 对于认证帐号可以对实时调用量清零，说明如下：
 * 1、由于指标计算方法或统计时间差异，实时调用量数据可能会出现误差，一般在1%以内。
 * 2、每个帐号每月共10次清零操作机会，清零生效一次即用掉一次机会（10次包括了平台上的清零和调用接口API的清零）。
 * 3、第三方帮助公众号调用时，实际上是在消耗公众号自身的quota。
 * 4、每个有接口调用限额的接口都可以进行清零操作。
 * @version 1.0
 * 
 */


require_once './https_method.php';
$json='{"appid":"wxa32cab395cd85a85"}';

$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/cgi-bin/clear_quota?access_token=$access_token";
$value=https_post($url,$json);

echo $value;