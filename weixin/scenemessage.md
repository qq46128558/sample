
## 一次性订阅消息

```php
/**
 * 前提:
 * build_message_url.php
 * 需要用户同意授权，获取一次给用户推送一条订阅模板消息的机会
 * 
 * 通过API推送订阅模板消息给到授权微信用户
 * 
 */
```

**由于测试号没有此接口(模版ID),所以直接使用宇能云公众号**

[生成确认授权URL](build_message_url.php "build_message_url.php")

### 示例代码 (蟹宝盒)
 ```php
 <?php
/**
 * 通过API推送订阅模板消息给到授权微信用户
 */
namespace app\commands\api\v1;

class ScenemessageController extends devController
{
    public function actionTest(){
        $access_token=self::getAccessToken();
        $url="https://api.weixin.qq.com/cgi-bin/message/template/subscribe?access_token=$access_token";
        $postdata=array(
            "touser"=>"oRnBdwrRp9wGh_q-IZW8XvWjyJn4",
            "template_id"=>"gQIxSr_43lX8kKoNLMODEB84ORs6CYQvhUgc-7IgznY",
            "url"=>"https://plugs.yn-ce.com",
            "scene"=>"101",
            "title"=>"一次性订阅消息",
            "data"=>array(
                "content"=>array(
                    "value"=>"消息正文，value为消息内容文本（200字以内），没有固定格式，可用\n换行，color为整段消息内容的字体颜色（目前仅支持整段消息为一种颜色",
                    "color"=>"#000000"
                )
            )
        );
        $result=self::httppost($url,json_encode($postdata));
        var_dump($result);
    }
}
```