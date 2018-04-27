<?php
/**
 * 云逆地理编码服务
 * http://lbsyun.baidu.com/index.php?title=lbscloud/yunni/explain
 * 
 */

$latitude=$_GET['latitude'];
$longitude=$_GET['longitude'];
$geotable_id=1;
$coord_type="gcj02ll";
$ak="mutYvoaB2U47IrueGcGzNWzfvDSefiWk";

$url="http://api.map.baidu.com/cloudrgc/v1?";
$url.="location=$latitude,$longitude";
$url.="&geotable_id=$geotable_id";
$url.="&coord_type=$coord_type";
$url.="&ak=$ak";

$ch=curl_init();
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_HTTPGET,1);
curl_setopt($ch,CURLOPT_URL,$url);
$output=curl_exec($ch);
curl_close($ch);
echo $output;


