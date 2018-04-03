<?php
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');
require(__DIR__ . '/../vendor/autoload.php');
require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');
$config = require(__DIR__ . '/../config/web.php');
(new yii\web\Application($config));

use Da\QrCode\QrCode;
use Da\QrCode\Format\BtcFormat; 
$format = new BtcFormat(['address' => '175tWpb8K1S7NmH4Zx6rewF9WQrcZv245W', 'amount' => 1, 'name' => 'antonio']);
$qrCode = new QrCode($format);
header('Content-Type: ' . $qrCode->getContentType());
echo $qrCode->writeString();

// 扫描结果:
// bitcoin:175tWpb8K1S7NmH4Zx6rewF9WQrcZv245W?amount=1&label=antonio
