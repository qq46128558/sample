<?php
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');
require(__DIR__ . '/../vendor/autoload.php');
require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');
$config = require(__DIR__ . '/../config/web.php');
(new yii\web\Application($config));


use Da\QrCode\QrCode;
use Da\QrCode\Format\PhoneFormat; 
$format = new PhoneFormat(['phone' => 657657657]);
$qrCode = new QrCode($format);
header('Content-Type: ' . $qrCode->getContentType());
echo $qrCode->writeString();

// 扫描结果:
// TEL:657657657