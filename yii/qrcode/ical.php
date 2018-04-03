<?php
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');
require(__DIR__ . '/../vendor/autoload.php');
require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');
$config = require(__DIR__ . '/../config/web.php');
(new yii\web\Application($config));

use Da\QrCode\QrCode;
use Da\QrCode\Format\iCalFormat; 
$format = new iCalFormat(['summary' => 'test-summary', 'startTimestamp' => 1260232200, 'endTimestamp' => 1260318600]);
$qrCode = new QrCode($format);
header('Content-Type: ' . $qrCode->getContentType());
echo $qrCode->writeString();

// 扫描结果:
// BEGIN:VEVENT SUMMARY:test-summary DTSTART:20091208T083000Z DTEND:20091209T083000Z END:VEVENT
