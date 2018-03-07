<?php
/**
 * json 转 array
 * 多行赋值
 * 暂无用到
 */

 $json=<<<STR
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
                "type":"miniprogram",
                "name":"wxa",
                "url":"http://mp.weixin.qq.com",
                "appid":"wx286b93c14bbf93aa",
                "pagepath":"pages/lunar/index"
            },
           {
              "type":"click",
              "name":"赞一下我们",
              "key":"V1001_GOOD"
           }]
      }]
}
STR;

$value=json_decode($json,1);
echo var_export($value,true);


// array ( 'button' => array ( 0 => array ( 'type' => 'click', 'name' => '今日歌曲', 'key' => 'V1001_TODAY_MUSIC', ), 1 => array ( 'name' => '菜单', 'sub_button' => array ( 0 => array ( 'type' => 'view', 'name' => '搜索', 'url' => 'http://www.soso.com/', ), 1 => array ( 'type' => 'miniprogram', 'name' => 'wxa', 'url' => 'http://mp.weixin.qq.com', 'appid' => 'wx286b93c14bbf93aa', 'pagepath' => 'pages/lunar/index', ), 2 => array ( 'type' => 'click', 'name' => '赞一下我们', 'key' => 'V1001_GOOD', ), ), ), ), )