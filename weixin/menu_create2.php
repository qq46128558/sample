<?php
/**
 * 自定义菜单创建接口2
 * 使用测试号测试
 * @version 1.0
 */

 /*
 测试media_id有问题,暂去掉
 {
    "type": "media_id", 
    "name": "图片", 
    "media_id": "",
    "sub_button": [ ]
    }, 
    {
    "type": "view_limited", 
    "name": "图文消息", 
    "media_id": "",
    "sub_button": [ ]
    }
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

$json=<<<STR
{
    "button": [
        {
            "name": "扫码", 
            "sub_button": [
                {
                    "type": "scancode_waitmsg", 
                    "name": "扫码带提示", 
                    "key": "rselfmenu_0_0", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "scancode_push", 
                    "name": "扫码推事件", 
                    "key": "rselfmenu_0_1", 
                    "sub_button": [ ]
                }
            ]
        }, 
        {
            "name": "发图", 
            "sub_button": [
                {
                    "type": "pic_sysphoto", 
                    "name": "系统拍照发图", 
                    "key": "rselfmenu_1_0", 
                   "sub_button": [ ]
                 }, 
                {
                    "type": "pic_photo_or_album", 
                    "name": "拍照或者相册发图", 
                    "key": "rselfmenu_1_1", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "pic_weixin", 
                    "name": "微信相册发图", 
                    "key": "rselfmenu_1_2", 
                    "sub_button": [ ]
                }
            ]
        }, 
        {
            "name":"其他",
            "sub_button":[
                {
                    "name": "发送位置", 
                    "type": "location_select", 
                    "key": "rselfmenu_2_0",
                    "sub_button": [ ]
                }
            ]
        }
    ]
}
STR;

$access_token=file_get_contents('./t_token.txt');
$url="https://api.weixin.qq.com/cgi-bin/menu/create?access_token=$access_token";
$value=https_post($url,$json);

echo $value;