<?php
/**
 * 自定义菜单删除接口
 * 使用测试号测试
 * 调用此接口会删除默认菜单及全部个性化菜单
 * @version 1.0
 */

 function https_get($url)
 {
    $ch=curl_init();
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
    curl_setopt($ch,CURLOPT_HTTPGET,1);
    curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
    curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
    curl_setopt($ch,CURLOPT_URL,$url);
    $output=curl_exec($ch);
    curl_close($ch);
    return $output;
 }

$access_token=file_get_contents('./t_token.txt');
$value=https_get("https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=$access_token");
echo $value;