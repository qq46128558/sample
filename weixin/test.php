<?php
/**
 * 各种临时调试测试
 */

require_once __DIR__."/https_method.php";

// $access_token=file_get_contents('./t_token.txt');
// echo https_get("https://api.weixin.qq.com/cgi-bin/menu/get?access_token=$access_token");

// echo my_access_token();
// echo t_access_token();
// var_dump($appinfo);

try{
    // echo t_refresh_token("o0ZAd1V-_YTIf2SXA3prYu_X6Cr0");
    $value=t_userinfo_byid("o0ZAd1V-_YTIf2SXA3prYu_X6Cr0");
    $headimgurl=$value['headimgurl'];
    echo "<img src='$headimgurl'></img>";
}
catch(Exception $ex){
    echo $ex->getMessage();
}
