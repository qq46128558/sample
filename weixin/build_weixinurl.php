<?php
/**
 * 生成一个微信中的网页链接
 * 
 */
require_once('https_method.php');
$redirecturl="http://ser.yn-ce.com/wx/webpage_auth.php";
$redirecturl=urlencode($redirecturl);

// 不同公众号请修改appid
if (isset($_GET['scope'])){
    // state是自定义传参
    echo 'scope=snsapi_base</br>';
    $url="https://open.weixin.qq.com/connect/oauth2/authorize?appid=".$appinfo->t_appid."&redirect_uri=$redirecturl&response_type=code&scope=snsapi_base&state=0#wechat_redirect";
}else{
    echo 'scope=snsapi_userinfo</br>';
    $url="https://open.weixin.qq.com/connect/oauth2/authorize?appid=".$appinfo->t_appid."&redirect_uri=$redirecturl&response_type=code&scope=snsapi_userinfo&state=1#wechat_redirect";
}
echo $url;
