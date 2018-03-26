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
 * 生成wx.config所需的配置信息
 * 测试号
 * $_SERVER['HTTP_REFERER'] 链接到当前页面的前一页面的 URL 地址
 * 
 */
function t_wx_config($url=null){
    global $appinfo;
    if (!$url) $url=$_SERVER['HTTP_REFERER'];
    $ticket=t_jsapi_ticket();
    $appid=$appinfo->t_appid;

    return json_encode(wx_config($appid,$ticket,$url));
}

/**
 * 生成wx.config所需的配置信息
 * 通过config接口注入权限验证配置
 * 
 */
function wx_config($appid,$ticket,$url){
    // 生成签名的时间戳
    $timestamp=time();
    // 生成签名的随机串
    $noncestr=getNoncestr();
    // 参与签名的字段包括noncestr（随机字符串）, 有效的jsapi_ticket, timestamp（时间戳）, url（当前网页的URL，不包含#及其后面部分）
    $config=array('nonceStr'=>$noncestr,'jsapi_ticket'=>$ticket,'timestamp'=>$timestamp,'url'=>$url);
    // 签名
    $config['signature']=get_wx_signature($config);
    // 公众号的唯一标识
    $config['appId']=$appid;
    $config['jsApiList']=array(
        'checkJsApi','onMenuShareTimeline','onMenuShareAppMessage','onMenuShareQQ','onMenuShareWeibo','onMenuShareQZone','hideMenuItems','showMenuItems','hideAllNonBaseMenuItem','showAllNonBaseMenuItem','translateVoice','startRecord','stopRecord','onVoiceRecordEnd','playVoice','onVoicePlayEnd','pauseVoice','stopVoice','uploadVoice','downloadVoice','chooseImage','previewImage','uploadImage','downloadImage','getNetworkType','openLocation','getLocation','hideOptionMenu','showOptionMenu','closeWindow','scanQRCode','chooseWXPay','openProductSpecificView','addCard','chooseCard','openCard'
    );
    // unset($config['jsapi_ticket']);
    // unset($config['url']);
    return $config;
    
}
/**
 * wx.config 签名算法
 * 签名生成规则如下：
 * 对所有待签名参数按照字段名的ASCII 码从小到大排序（字典序）后，
 * 使用URL键值对的格式（即key1=value1&key2=value2…）拼接成字符串string1。
 * 这里需要注意的是所有参数名均为小写字符。
 * 对string1作sha1加密，字段名和字段值都采用原始值，不进行URL 转义。
 * 
 */
function get_wx_signature($config){
    ksort($config);
    $config['url']=explode('#',$config['url'])[0];
    $str='';
    foreach($config as $key=>$value){
        $str.=(strlen($str)>0 ? '&':'').strtolower($key)."=".$value;
    }
    return sha1($str);
}
/**
 * 生成随机字符串
 * 
 */
function  make_seed ()
{
  list( $usec ,  $sec ) =  explode ( ' ' ,  microtime ());
  return (float)  $sec  + ((float)  $usec  *  100000 );
}
function getNoncestr($len=16){
    mt_srand ( make_seed ());
    $noncestr='';
    // ascii 33 ~ 126(字符) 随机
    for ($i=0;$i<$len;$i++){
        $noncestr.=chr(mt_rand(33,126));
    }
    return $noncestr;
}

/**
 * 用access_token 采用http GET方式请求获得jsapi_ticket
 * 普通access_token
 * 测试号
 * 
 */
function t_jsapi_ticket(){
    global $appinfo;
    $appid=$appinfo->t_appid;
    $secret=$appinfo->t_secret;
    $filename=__DIR__."/".$appinfo->t_ticket_filename;
    // 普通access_token
    $access_token=t_access_token();
    return jsapi_ticket($appid,$secret,$filename,$access_token);
}

/**
 * 用access_token 采用http GET方式请求获得jsapi_ticket
 * {
 * "errcode":0,
 * "errmsg":"ok",
 * "ticket":"bxLdikRXVbTPdHSM05e5u5sUoXNKd8-41ZO3MhKoyN5OfkWITDGgnr2fwJ0m9E8NYzWKVZvdVtaUgWvsdshFKA",
 * "expires_in":7200
 * }
 * 
 */
function jsapi_ticket($appid,$secret,$filename,$access_token){
    //先从文件取
    //转成数组
    $ticket=json_decode(file_get_contents($filename),1);

    //无值则重新取一次
    if (!$ticket || ($ticket && $ticket['expires_in']<time())){
        $url="https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=$access_token&type=jsapi";
        $ticket=https_get($url);
        //转成对象
        $ticket=json_decode($ticket);
        if ($ticket!=null && $ticket->ticket){
            $ticket->expires_in=time()+$ticket->expires_in;
            //取值后写入文件
            file_put_contents($filename,json_encode($ticket));
            return $ticket->ticket;
        }else{
            //返回错误信息
            return json_encode($ticket);
        }

    }
    //有值则直接返回
    return $ticket['ticket'];
}


/**
 * 检验授权凭证（access_token）是否有效
 * 网页授权access_token
 * 
 */
function auth_access_token($openid){
    $value=file_get_contents(__DIR__."/openid/".$openid);
    $access_token=json_decode($value)->access_token;
    $url="https://api.weixin.qq.com/sns/auth?access_token=$access_token&openid=$openid";
    $value=https_get($url);
    return $value;
}

/**
 * 拉取用户信息(需scope为 snsapi_userinfo)
 * 根据openid
 * 
 */
function t_userinfo_byid($openid){
    $value=file_get_contents(__DIR__."/openid/".$openid);
    $value=json_decode($value,1);
    // 网页授权access_token
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
        file_put_contents(__DIR__.'/openid/'.$value['openid']."_2",json_encode($value));
        return $value;
    }
}

/**
 * 拉取用户信息(需scope为 snsapi_userinfo)
 * 根据code
 * 通过code换取网页授权access_token(存起来，30天内可用refresh再获取最新的用户信息？)
 */
function t_userinfo($code)
{
    // 网页授权access_token
    $value=t_openid($code);
    if ($value && $value['openid']){
        $url="https://api.weixin.qq.com/sns/userinfo?access_token=".$value['access_token']."&openid=".$value['openid']."&lang=zh_CN";
        $value=https_get($url);
        wlog($value);
        $value=json_decode($value,1);
        if ($value && $value['openid']){
            file_put_contents(__DIR__.'/openid/'.$value['openid']."_2",json_encode($value));
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
 * 网页授权access_token
 */
function t_refresh_token($openid){
    global $appinfo;
    $value=json_decode(file_get_contents(__DIR__."/openid/$openid"),1);
    if ($value && $value["refresh_token"]){
        $refresh_token=$value["refresh_token"];
        $url="https://api.weixin.qq.com/sns/oauth2/refresh_token?appid=".$appinfo->t_appid."&grant_type=refresh_token&refresh_token=$refresh_token";
        wlog($url);
        $value=https_get($url);
        wlog($value);
        $value=json_decode($value,1);
        if ($value && $value['openid']){
            $value['expires_in']=time()+$value['expires_in'];
            file_put_contents(__DIR__.'/openid/'.$openid,json_encode($value));
            return $value['access_token'];
        }
        $value=json_encode($value);
        wlog("refresh_token failed: ".$value,2);
        throw new Exception($value);
    }
    throw new Exception("openid file not found.");
}

/**
 * 根据微信提供的code获取用户的openid & access_token
 * 网页授权access_token
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
        file_put_contents(__DIR__.'/openid/'.$openid,json_encode($value));
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
        file_put_contents(__DIR__."/".'all.log',"\n",FILE_APPEND);
        file_put_contents(__DIR__."/".'all.log',$value,FILE_APPEND);
    }
}

/**
 * APPID & SECRET 信息
 */
function appinfo()
{
    $value=json_decode(file_get_contents(__DIR__."/appinfo.json"));
    return $value;
}

 /**
  * 获取测试号的access_token
  * 普通access_token
  */
function t_access_token(){
    global $appinfo;
    $secret=$appinfo->t_secret;
    $appid=$appinfo->t_appid;
    $filename=__DIR__."/".$appinfo->t_filename;
    return access_token($appid,$secret,$filename);
}


 /**
  * 获取我的个人订阅号的access_token
  * 返回格式
  * {"access_token":"ACCESS_TOKEN","expires_in":7200}
  * 普通access_token
  */
function my_access_token(){
    global $appinfo;
    return access_token($appinfo->my_appid,$appinfo->my_secret,__DIR__."/".$appinfo->my_filename);
}

/**
 * 获取指定appid的access_token
 * 普通access_token
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

