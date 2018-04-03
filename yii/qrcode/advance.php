<?php
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');
require(__DIR__ . '/../vendor/autoload.php');
require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');
$config = require(__DIR__ . '/../config/web.php');
(new yii\web\Application($config));

use Da\QrCode\QrCode;
use Da\QrCode\Label;
use Da\QrCode\Contracts\ErrorCorrectionLevelInterface;

$label = (new Label('2amigos'))
    //->useFont(__DIR__ . '/../resources/fonts/monsterrat.otf')
    ->updateFontSize(12);

$qrCode = (new QrCode('https://2amigos.us'))
    ->useLogo(__DIR__ . '/logo.png')
    ->useForegroundColor(0,0,0)
    ->useBackgroundColor(255,255,255)
    ->useEncoding('UTF-8')
    ->setErrorCorrectionLevel(ErrorCorrectionLevelInterface::HIGH)
    ->setLogoWidth(60)
    ->setSize(300)
    ->setMargin(5)
    ->setLabel($label);

header('Content-Type:'.$qrCode->getContentType());
//$qrCode->writeFile(__DIR__ . '/my-code.png');
echo $qrCode->writeString();