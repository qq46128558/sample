<?php
/**
 * 提供HTTPS 请求调用方法
 * @version 1.0
 */


function https_post($url,$postdata)
{
   $ch=curl_init();
   curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
   curl_setopt($ch,CURLOPT_POST,1);
   curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
   curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
   curl_setopt($ch,CURLOPT_URL,$url);
   curl_setopt($ch,CURLOPT_POSTFIELDS,$postdata);
   $output=curl_exec($ch);
   curl_close($ch);
   return $output;
}

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
