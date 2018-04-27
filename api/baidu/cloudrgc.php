<?php
/**
 * LBS.云服务
 * http://lbsyun.baidu.com/index.php?title=lbscloud
 * 
 * 云逆地理编码服务
 * http://lbsyun.baidu.com/index.php?title=lbscloud/yunni/explain
 * 
 */

// location:待解析的坐标，格式：纬度,经度。
$latitude=22.373041;
$longitude=113.55883;
// geotable_id:用户使用云存储服务，存储自定义数据时生成的数据表ID。使用个性化逆地理编码服务必须（使用指定geotable_id数据表中地理数据对坐标进行位置描述）
// 135675,144316 未知
$geotable_id=1;
// extensions:扩展信息控制。是否返回扩展信息：默认不返回，extensions=pois时返回pois和custom_pois
$extensions="pois";
// coord_type:输入坐标的坐标系：bd09ll（百度经纬度坐标）、gcj02ll（国测局经纬度坐标）、wgs84ll（wgs84经纬度坐标）
$coord_type="gcj02ll";
// ak:用户申请注册的key（服务鉴权秘钥）
$ak="mutYvoaB2U47IrueGcGzNWzfvDSefiWk";
// sn:若用户所用ak的校验方式为sn校验时该参数必须
$sn="";
// timestamp:鉴权时间戳，配合ak鉴权
$timestamp=time();

$url="http://api.map.baidu.com/cloudrgc/v1?";
$url.="location=$latitude,$longitude";
$url.="&geotable_id=$geotable_id";
// $url.="&extensions=$extensions";
$url.="&coord_type=$coord_type";
$url.="&ak=$ak";
// $url.="&sn=$sn";
// $url.="&timstamp=$timestamp";
echo $url."<br>";

$ch=curl_init();
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_HTTPGET,1);
// curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
// curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
curl_setopt($ch,CURLOPT_URL,$url);
$output=curl_exec($ch);
curl_close($ch);

print_r($output);


