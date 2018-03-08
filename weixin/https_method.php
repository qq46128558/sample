<?php
/**
 * 提供HTTPS 请求调用方法
 * 提供获取有效的access_token方法
 * 
 * @version 1.1
 */

 error_reporting(E_ALL ^ E_NOTICE);

 /**
  * 获取我的个人订阅号的access_token
  * 返回格式
  * {"access_token":"ACCESS_TOKEN","expires_in":7200}
  */
 function my_access_token(){
     $my_secret="f6d0edf04c31754b92e108c9fb20a180";
     $my_appid="wx817b492673790402";
     //先从文件取
     //转成数组
     $token=json_decode(file_get_contents('./token.json'),1);

     //无值则重新取一次
     if (!$token || ($token && $token['expires_in']<time())){
        $token=https_get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$my_appid&secret=$my_secret");
        //转成对象
        $token=json_decode($token);
        if ($token!=null && $token->access_token){
            $token->expires_in=time()+$token->expires_in;
            //取值后写入文件
            file_put_contents('./token.json',json_encode($token));
            return $token->access_token;
        }else{
            //返回错误信息
            return json_encode($token);
        }

     }
    //有值则直接返回
     return $token['access_token'];
 }

/**
 * https的post请求
 */
function https_post($url,$postdata)
{
   $ch=curl_init();
   curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
   curl_setopt($ch,CURLOPT_POST,1);
   curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
//    curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,1);
   curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
   curl_setopt($ch,CURLOPT_URL,$url);
   curl_setopt($ch,CURLOPT_POSTFIELDS,$postdata);
   $output=curl_exec($ch);
   curl_close($ch);
   return $output;
}

/**
 * https的get请求
 */
function https_get($url)
{
    $ch=curl_init();
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
    curl_setopt($ch,CURLOPT_HTTPGET,1);
    curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
    // curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,1);
    curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
    curl_setopt($ch,CURLOPT_URL,$url);
    $output=curl_exec($ch);
    curl_close($ch);
    return $output;
}

