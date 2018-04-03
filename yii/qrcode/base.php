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
// now we can display the qrcode in many ways
// saving the result to a file:
// $qrCode->writeFile(__DIR__ . '/code.png'); // writer defaults to PNG when none is specified
// display directly to the browser 
header('Content-Type: '.$qrCode->getContentType());
echo $qrCode->writeString();

// 有遇到过在Yii的控制器中部份Code响应为text/html(乱码)的解决:
// use yii\web\Response;
// \Yii::$app->response->format = Response::FORMAT_RAW;