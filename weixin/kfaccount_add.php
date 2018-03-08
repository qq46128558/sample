<?php
/**
 * 添加客服帐号
 * 客服消息接口文档
 * https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140547
 * @version 1.0
 * 
 * 报错:
 * {"errcode":65400,"errmsg":"please enable new custom service, or wait for a while if you have enabled hint: [zQZK9a0603shb1]"}
 * 多客服将于7月1日全面升级为新版客服功能
 * https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncement&key=1464266075&version=12&lang=zh_CN
 * 暂不处理
 */

require_once './https_method.php';
$json=<<<STR
{
    "kf_account" : "test1@test",
    "nickname" : "客服1",
    "password" : "pswmd5",
}
STR;
$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/customservice/kfaccount/add?access_token=$access_token";
$value=https_post($url,$json);

echo $value; 
