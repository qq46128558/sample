<?php
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');
require(__DIR__ . '/../vendor/autoload.php');
require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');
$config = require(__DIR__ . '/../config/web.php');
(new yii\web\Application($config));

use Da\QrCode\QrCode;
use Da\QrCode\Format\GeoFormat; 
$format = new GeoFormat(['lat' => 1,'lng' => 1, 'altitude' => 20]);
$qrCode = new QrCode($format);
header('Content-Type: ' . $qrCode->getContentType());
echo $qrCode->writeString();

// 扫描结果:
// GEO:1,1,20
