## Class yii\BaseYii t() public static 方法

Translates a message to the specified language.

This is a shortcut method of yii\i18n\I18N::translate().

public static string t ( $category, $message, $params = [], $language = null )


配置文件:  
config/web.php
~~~
$config = [
    'language'=> 'zh-CN',

......

'components' => [
        'i18n' => [
            'translations' => [
                'app' => [
                    'class' => 'yii\i18n\PhpMessageSource',
                    //'basePath' => '@app/messages',
                    //'sourceLanguage' => 'en-US',
                    'fileMap' => [
                        'app' => 'app.php',
                    ],
                ],
            ],
        ],
~~~

i18n类文件:  
vendor/yiisoft/yii2/i18n/PhpMessageSource.php
~~~
#basePath指向
public $basePath = '@app/messages';
~~~

则资源文件在此处:  
messages/zh-CN/app.php
~~~
<?php
return [
    '10001' => 'HTTP请求方法不支持',
    '10002' => 'JSON数据格式错误',
];
~~~

基本用法:
~~~
#比如$result->status为10002
$msg = \Yii::t('app', $result->status);
~~~

消息参数:
    Yii::t('backend','可通過{0}標識{1}訪問',['Yii::$app->params["web"]["','"]']);