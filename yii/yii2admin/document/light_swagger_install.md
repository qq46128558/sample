## yii2admin light swagger安装
1. 在composer.json>>require属性增加:
	- "doctrine/annotations":"1.6.0",
	- "light/yii2-swagger": "~1.0.4"

2. 执行composer update

3. 在前端页面增加一个控制器(或原有控制器中增加方法)
~~~
<?php
namespace frontend\controllers;
use yii\web\Controller;
use Yii;
/**
 * @referurl https://packagist.org/packages/light/yii2-swagger
 */
class SwgController extends Controller{
    // 修改当前控制器的默认动作
    public $defaultAction='doc';
    
    public function actions()
    {
        return [
            //The document preview addesss:http://api.yourhost.com/site/doc
            'doc' => [
                'class' => 'light\swagger\SwaggerAction',
                'restUrl' => \yii\helpers\Url::to(['/swg/api'], true),
            ],
            //The resultUrl action.
            'api' => [
                'class' => 'light\swagger\SwaggerApiAction',
                //The scan directories, you should use real path there.
                'scanDir' => [
                    Yii::getAlias('@api/modules/tp/swagger'),
                    Yii::getAlias('@api/modules/tp/controllers'),
                    // Yii::getAlias('@api/modules/tp/models'),
                    // Yii::getAlias('@api/models'),
                ],
                //The security key 如果设定此值,则页面上需要输入此Key才能测试API,未验证
                'api_key' => '',
            ],
        ];
    }
}
~~~


4. 增加swagger注释文件,如api/modules/tp/swagger/*.php

5. 在api接口文件中增加swagger注释

6. 测试页面是否能正常打开: http://47.106.160.48/swg

7. http://47.106.160.48/swg/api 测试返回的json(即那些注释)

8. swagger 主页面文件: vendor/light/yii2-swagger/src/index.php


#### 参考资料
- [安装](https://packagist.org/packages/light/yii2-swagger "https://packagist.org/packages/light/yii2-swagger")
- [DEMO](https://github.com/lichunqiang/yii2-swagger-demo "https://github.com/lichunqiang/yii2-swagger-demo")
