<?php
/**
 * 微信网页授权
 * 1.用户同意授权，获取code
 * code说明 ： code作为换取access_token的票据，每次用户授权带上的code将不一样，code只能使用一次，5分钟未被使用自动过期。
 * 2.通过code换取网页授权access_token(存起来，30天内可用refresh再获取最新的用户信息？)
 * 3.刷新access_token（如果需要）
 * 4.拉取用户信息(需scope为 snsapi_userinfo)
 */
require_once('https_method.php');
$code=$_GET['code'];
$state=$_GET['state'];
wlog(var_export($_GET,1));

// base
// $openid=t_openid($code);
// wlog(var_export($openid,1));

// userinfo
try{
    $value=t_userinfo($code);
    $headimgurl=$value['headimgurl'];
    echo "<img src='$headimgurl'></img>";
}
catch(Exception $ex){
    echo $ex->getMessage();
}






