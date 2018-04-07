<?php
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');
require(__DIR__ . '/../vendor/autoload.php');
require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');
$config = require(__DIR__ . '/../config/web.php');
(new yii\web\Application($config));


use Da\QrCode\QrCode;
use Da\QrCode\Format\vCardFormat; 
$format = new vCardFormat();
$format->name = "Antonio";
$format->fullName = "Antonio Ramirez";
$format->email = "hola@2amigos.us";
$qrCode = new QrCode($format);
header('Content-Type: ' . $qrCode->getContentType());
echo $qrCode->writeString();

// 扫描结果:
// 弹出一个名片,提供保存按钮