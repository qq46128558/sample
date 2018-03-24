<?php
/**
 * 各种临时调试测试
 */

require_once __DIR__."/https_method.php";

try{
    $value=t_userinfo_byid("o0ZAd1V-_YTIf2SXA3prYu_X6Cr0");
    $headimgurl=$value['headimgurl'];
    echo "<img src='$headimgurl'></img>";
}
catch(Exception $ex){
    echo $ex->getMessage();
}
