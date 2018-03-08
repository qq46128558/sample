<?php
/**
 * 获取自定义菜单配置接口
 * 认证/未认证的服务号/订阅号，以及接口测试号，均拥有该接口权限。
 * 本接口与自定义菜单查询接口的不同之处在于，本接口无论公众号的接口是如何设置的，都能查询到接口，而自定义菜单查询接口则仅能查询到使用API设置的菜单配置
 * @version 1.0
 */

 require_once './https_method.php';

$access_token=file_get_contents('./token.txt');
$url="https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=$access_token";
$value=https_get($url);

echo $value;