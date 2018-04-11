
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

[参考示例源码](../../xbh_plugin/yii2/commands/api/v1/ScenemessageController.php "ScenemessageController.php")

 