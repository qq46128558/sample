<?php
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');
require(__DIR__ . '/../vendor/autoload.php');
require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');
$config = require(__DIR__ . '/../config/web.php');
(new yii\web\Application($config));

use Da\QrCode\QrCode;
use Da\QrCode\Format\MeCardFormat; 
$format = new MeCardFormat();
$format->firstName = 'Antonio';
$format->lastName = 'Ramirez';
$format->sound = 'docomotaro';
$format->phone = '657657XXX';
$format->videoPhone = '657657XXX';
$format->email = 'hola@2amigos.us';
$format->note = 'test-note';
$format->birthday = '19791201';
$format->address = 'test-address';
$format->url = 'http://2amigos.us';
$format->nickName = 'tonydspaniard';
$qrCode = new QrCode($format);
header('Content-Type: ' . $qrCode->getContentType());
echo $qrCode->writeString();

// 扫描结果:
// 生成详细名片,提供保存按钮