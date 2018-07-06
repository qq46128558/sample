<?php
// 引入Yii框架基类的代码 (console应用)
defined('YII_DEBUG') or define('YII_DEBUG', true);
// require(__DIR__ . '/vendor/autoload.php');
// require(__DIR__ . '/vendor/yiisoft/yii2/Yii.php');
require(__DIR__ . '/../../yiibasic/vendor/autoload.php');
require(__DIR__ . '/../../yiibasic/vendor/yiisoft/yii2/Yii.php');
// $config = require(__DIR__ . '/config/console.php');
$config = require(__DIR__ . '/../../yiibasic/config/console.php');
$application = new yii\console\Application($config);

// 使用Yii类
Yii::$app->runAction('hello/index');