<?php
/**
 * 获取微信测试号的access_token
 * 
 */
build_access_token();
// read_token();

 function build_access_token(){
    $secret="81f6c3f0ec261d983c55576e3659661f";
    $appid="wxa32cab395cd85a85";
    $ch = curl_init(); 
    curl_setopt($ch, CURLOPT_URL, "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$appid&secret=$secret");
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER,0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST,2);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $data = json_decode(curl_exec($ch));
    if($data && $data->access_token){
        file_put_contents("./t_token.txt",$data->access_token);
    }else{
        echo $data->errmsg or die('failed to get access_token');
    }
    curl_close($ch);
 }

 function read_token(){
     $value=file_get_contents("./t_token.txt");
     echo $value;
 }