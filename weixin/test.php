<?php
/**
 * 各种临时调试测试
 */

require_once __DIR__."/https_method.php";

try{
    $value=auth_access_token("o0ZAd1V-_YTIf2SXA3prYu_X6Cr0");
    echo $value;
}
catch(Exception $ex){
    echo $ex->getMessage();
}
