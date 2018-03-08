<?php
/**
 * 自定义菜单创建接口
 * 使用测试号测试
 * @version 1.0
 */

/* 
一开始报错:
array (size=2)
'errcode' => int 85005
'errmsg' => string 'appid not bind weapp hint: [C9Ryja0111vr30]' (length=43)

因为微信技术文档中的这一段是小程序
小程序的appid（仅认证公众号可配置）
{
    "type":"miniprogram",
    "name":"wxa",
    "url":"http://mp.weixin.qq.com",
    "appid":"wx286b93c14bbf93aa",
    "pagepath":"pages/lunar/index"
},
 */

$access_token=file_get_contents("./t_token.txt");
$ch=curl_init();
curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);

curl_setopt($ch,CURLOPT_POST,1);
$url="https://api.weixin.qq.com/cgi-bin/menu/create?access_token=$access_token";
curl_setopt($ch,CURLOPT_URL,$url);

$postdata=<<<STR
{
    "button":[
    {    
         "type":"click",
         "name":"今日歌曲",
         "key":"V1001_TODAY_MUSIC"
     },
     {
          "name":"菜单",
          "sub_button":[
          {    
              "type":"view",
              "name":"搜索",
              "url":"http://www.soso.com/"
           },
           {
              "type":"click",
              "name":"赞一下我们",
              "key":"V1001_GOOD"
           }]
      }]
}
STR;
curl_setopt($ch,CURLOPT_POSTFIELDS,$postdata);
$output=curl_exec($ch);
var_dump(json_decode($output,1));

/* 正常返回:
array (size=2)
  'errcode' => int 0
  'errmsg' => string 'ok' (length=2) */

curl_close($ch);
