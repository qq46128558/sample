<?php
$str='淘力网运营平台';

$encode=urlencode($str);
echo $encode.'</br>';

$decode=urldecode($encode);
echo $decode;
