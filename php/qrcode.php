<?php
include_once __DIR__.'/../vendor/phpqrcode/phpqrcode.php';

// http://phpqrcode.sourceforge.net/

// 下载官网提供的类库后，只需要使用phpqrcode.php就可以生成二维码了，当然您的PHP环境必须开启支持GD2。phpqrcode.php提供了一个关键的png()方法，其中
// 参数$text表示生成二位的的信息文本；
// 参数$outfile表示是否输出二维码图片文件，默认否；
// 参数$level表示容错率，也就是有被覆盖的区域还能识别，分别是L（QR_ECLEVEL_L，7%），M（QR_ECLEVEL_M，15%），Q（QR_ECLEVEL_Q，25%），H（QR_ECLEVEL_H，30%）；
// 参数$size表示生成图片大小，默认是3；
// 参数$margin表示二维码周围边框空白区域间距值；
// 参数$saveandprint表示是否保存二维码并显示。
/* 
public static function png($text, $outfile=false, $level=QR_ECLEVEL_L, $size=3, $margin=4, 
$saveandprint=false) 
{
    $enc = QRencode::factory($level, $size, $margin);
    return $enc->encodePNG($text, $outfile, $saveandprint=false);
} */

$value = 'welcome to qrcode'; //二维码内容
$errorCorrectionLevel = 'L';//容错级别
$matrixPointSize = 6;//生成图片大小
//生成二维码图片
QRcode::png($value, 'qrcode.png', $errorCorrectionLevel, $matrixPointSize, 2);
// 在二维码的中间加上自己的LOGO
// $logo = '';//准备好的logo图片
$QR = 'qrcode.png';//已经生成的原始二维码图
 
$QR = imagecreatefromstring(file_get_contents($QR));
if (isset($logo)) {
    $logo = imagecreatefromstring(file_get_contents($logo));
    $QR_width = imagesx($QR);//二维码图片宽度
    $QR_height = imagesy($QR);//二维码图片高度
    $logo_width = imagesx($logo);//logo图片宽度
    $logo_height = imagesy($logo);//logo图片高度
    $logo_qr_width = $QR_width / 5;
    $scale = $logo_width/$logo_qr_width;
    $logo_qr_height = $logo_height/$scale;
    $from_width = ($QR_width - $logo_qr_width) / 2;
    //重新组合图片并调整大小
    imagecopyresampled($QR, $logo, $from_width, $from_width, 0, 0, $logo_qr_width, 
    $logo_qr_height, $logo_width, $logo_height);
}
//输出图片
imagepng($QR, 'qrcode_withlogo.png');
echo '<img src="qrcode_withlogo.png">';