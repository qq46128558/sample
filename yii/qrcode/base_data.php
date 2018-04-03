<?php
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');
require(__DIR__ . '/../vendor/autoload.php');
require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');
$config = require(__DIR__ . '/../config/web.php');
(new yii\web\Application($config));

use Da\QrCode\QrCode;
$qrCode = (new QrCode('http://www.baidu.com'))
    ->setSize(250)
    ->setMargin(5)
    ->useForegroundColor(51, 153, 255);
echo '<img src="' . $qrCode->writeDataUri() . '">';