<?php
/**
 * 引入Yii框架基类的代码
 */
// comment out the following two lines when deployed to production
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');

// require(__DIR__ . '/../vendor/autoload.php');
// require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');
require(__DIR__ . '/../../yiibasic/vendor/autoload.php');
require(__DIR__ . '/../../yiibasic/vendor/yiisoft/yii2/Yii.php');

// $config = require(__DIR__ . '/../config/web.php');
$config = require(__DIR__ . '/../../yiibasic/config/web.php');

(new yii\web\Application($config));

//使用Yii类
// 控制器中如果没有use Yii(namespace yii\web),则可以用\Yii调用
echo Yii::getVersion();
