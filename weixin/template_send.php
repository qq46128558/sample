<?php
/**
 * 发送模板消息
 * 
 * 注：url和miniprogram都是非必填字段，若都不传则模板无跳转；若都传，会优先跳转至小程序。开发者可根据实际需要选择其中一种跳转方式即可。当用户的微信客户端版本不支持跳小程序时，将会跳转至url。
 * "miniprogram":{
 *     "appid":"xiaochengxuappid12345",
 *     "pagepath":"index?foo=bar"
 *   },   
 * @version 1.0
 * 
 * 
 */

require_once './https_method.php';
$json=<<<STR
{
    "touser":"o0ZAd1V-_YTIf2SXA3prYu_X6Cr0",
    "template_id":"ltqLvdupREV5MSOsHTHpA9kYwYeQWcvmrkckrStLnoQ",
    "url":"http://weixin.qq.com/download",  
    "data":{
            "first": {
                "value":"恭喜你购买成功！",
                "color":"#173177"
            },
            "keynote1":{
                "value":"巧克力",
                "color":"#173177"
            },
            "keynote2": {
                "value":"39.8元",
                "color":"#173177"
            },
            "keynote3": {
                "value":"2014年9月22日",
                "color":"#173177"
            },
            "remark":{
                "value":"欢迎再次购买！",
                "color":"#173177"
            }
    }
}
STR;
$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=$access_token";
$value=https_post($url,$json);

echo $value;