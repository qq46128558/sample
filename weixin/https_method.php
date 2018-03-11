<?php
/**
 * 提供HTTPS 请求调用方法
 * 提供获取有效的access_token方法
 * 
 * @version 1.1
 */

error_reporting(E_ALL ^ E_NOTICE);

$appinfo=appinfo();

/**
 * 拉取用户信息(需scope为 snsapi_userinfo)
 * 根据openid
 * 
 */
function t_userinfo_byid($openid){
    $value=file_get_contents("./openid/".$openid);
    $value=json_decode($value,1);
    // 未过期
    if ($value && $value['expires_in']>time()){
        $access_token=$value['access_token'];
    }
    // 已过期
    elseif($value && $value['refresh_token']){
        $access_token=t_refresh_token($openid);
    }else{
        $value=json_encode($value);
        wlog($value);
        throw new Exception('openid file error.');
    }

    $url="https://api.weixin.qq.com/sns/userinfo?access_token=".$access_token."&openid=".$openid."&lang=zh_CN";
    $value=https_get($url);
    wlog($value);
    $value=json_decode($value,1);
    if ($value && $value['openid']){
        file_put_contents('./openid/'.$value['openid']."_2",json_encode($value));
        return $value;
    }
}

/**
 * 拉取用户信息(需scope为 snsapi_userinfo)
 * 根据code
 */
function t_userinfo($code)
{
    $value=t_openid($code);
    if ($value && $value['openid']){
        $url="https://api.weixin.qq.com/sns/userinfo?access_token=".$value['access_token']."&openid=".$value['openid']."&lang=zh_CN";
        $value=https_get($url);
        wlog($value);
        $value=json_decode($value,1);
        if ($value && $value['openid']){
            file_put_contents('./openid/'.$value['openid']."_2",json_encode($value));
            return $value;
        }
        $value=json_encode($value);
        wlog("get userinfo failed: ".$value,2);
        throw new Exception($value);
    }
}

/**
 * 刷新access_token
 * 测试号
 */
function t_refresh_token($openid){
    global $appinfo;
    $value=json_decode(file_get_contents("./openid/$openid"),1);
    if ($value && $value["refresh_token"]){
        $refresh_token=$value["refresh_token"];
        $url="https://api.weixin.qq.com/sns/oauth2/refresh_token?appid=".$appinfo->t_appid."&grant_type=refresh_token&refresh_token=$refresh_token";
        wlog($url);
        $value=https_get($url);
        wlog($value);
        $value=json_decode($value,1);
        if ($value && $value['openid']){
            $value['expires_in']=time()+$value['expires_in'];
            file_put_contents('./openid/'.$openid,json_encode($value));
            return $value['access_token'];
        }
        $value=json_encode($value);
        wlog("refresh_token failed: ".$value,2);
        throw new Exception($value);
    }
    throw new Excption("openid file not found.");
}

/**
 * 根据微信提供的code获取用户的openid & access_token
 */
function t_openid($code)
{
    global $appinfo;
    return openid($appinfo->t_appid,$appinfo->t_secret,$code);
}
function openid($appid,$secret,$code){
    $url="https://api.weixin.qq.com/sns/oauth2/access_token?appid=".$appid."&secret=".$secret."&code=$code&grant_type=authorization_code";
    $value=https_get($url);
    $value=json_decode($value,1);
    if ($value && $value['openid']){
        $openid=$value['openid'];
        $value['expires_in']=time()+$value['expires_in'];
        file_put_contents('./openid/'.$openid,json_encode($value));
        return array('openid'=>$openid,'access_token'=>$value['access_token']);
    }
    $value=json_encode($value);
    wlog("get openid failed: ".$value,2);
    throw new Exception($value);
}
/**
 * 写日志
 */
function wlog($value,$level=4)
{
    //2 error 4 info
    $currentLevel=4;
    if ($currentLevel>=$level){
        file_put_contents('all.log',"\n",FILE_APPEND);
        file_put_contents('all.log',$value,FILE_APPEND);
    }
}

/**
 * APPID & SECRET 信息
 */
function appinfo()
{
    $value=json_decode(file_get_contents("appinfo.json"));
    return $value;
}

 /**
  * 获取测试号的access_token
  *
  */
function t_access_token(){
    global $appinfo;
    $secret=$appinfo->t_secret;
    $appid=$appinfo->t_appid;
    $filename=$appinfo->t_filename;
    return access_token($appid,$secret,$filename);
}


 /**
  * 获取我的个人订阅号的access_token
  * 返回格式
  * {"access_token":"ACCESS_TOKEN","expires_in":7200}
  */
function my_access_token(){
    global $appinfo;
    return access_token($appinfo->my_appid,$appinfo->my_secret,$appinfo->my_filename);
}

/**
 * 获取指定appid的access_token
 * 
 */
 function access_token($appid,$secret,$filename){
    
     //先从文件取
     //转成数组
     $token=json_decode(file_get_contents($filename),1);

     //无值则重新取一次
     if (!$token || ($token && $token['expires_in']<time())){
        $token=https_get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$appid&secret=$secret");
        //转成对象
        $token=json_decode($token);
        if ($token!=null && $token->access_token){
            $token->expires_in=time()+$token->expires_in;
            //取值后写入文件
            file_put_contents($filename,json_encode($token));
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

