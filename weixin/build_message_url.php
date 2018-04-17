<?php
/**
 * 一次性订阅消息
 * 测试号没有一次性订阅消息
 */
require_once(__DIR__."/https_method.php");

$template_id="gQIxSr_43lX8kKoNLMODEB84ORs6CYQvhUgc-7IgznY";
$appid="wx56c09a46dfc4c131";
$redirect_url=urlencode("https://plugs.yn-ce.com/scenemessage.php");
// 用于保持请求和回调的状态，授权请后原样带回给第三方。该参数可用于防止csrf攻击（跨站请求伪造攻击），建议第三方带上该参数，可设置为简单的随机数加session进行校验，开发者可以填写a-zA-Z0-9的参数值，最多128字节，要求做urlencode
$reserved="test";

$url="https://mp.weixin.qq.com/mp/subscribemsg?";
$url.="action=get_confirm";
$url.="&appid=$appid";
// scene: 开发者可以填0-10000的整形值，用来标识订阅场景值, 若要订阅多条，需要不同scene场景值
$url.="&scene=101";
$url.="&template_id=$template_id";
$url.="&redirect_url=$redirect_url";
$url.="&reserved=$reserved";
// 无论直接打开还是做页面302重定向时，必须带此参数
$url.="#wechat_redirect";

echo $url;
