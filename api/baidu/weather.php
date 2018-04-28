<?php
/**
 * 天气查询
 * http://lbsyun.baidu.com/index.php?title=wxjsapi/guide/getweather
 * 
 * 百度地图微信小程序JavaScript API模块
 * https://github.com/baidumapapi/wxapp-jsapi/blob/master/src/bmap-wx.js
 * 
 */
$coord_type='gcj02';
$output='json';
$ak="nZU5zEXjfIG2SWKzFX8ld6Fsvt0Xj8WR";
$sn="";
$timestamp=time();
//longitude,latitude
$location="珠海";

$url="https://api.map.baidu.com/telematics/v3/weather?";
$url.="coord_type=$coord_type";
$url.="&output=$output";
$url.="&ak=$ak";
$url.="&sn=$sn";
$url.="&timestamp=$timestamp";
$url.="&location=$location";
echo $url."<br>";

$ch=curl_init();
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_HTTPGET,1);
curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
curl_setopt($ch,CURLOPT_URL,$url);
$res=curl_exec($ch);
curl_close($ch);

$resObj=json_decode($res);
if ($resObj->error==0 && $resObj->status=='success'){
    $weather=$resObj->results[0]->weather_data;
    $result["currentCity"]=$resObj->results[0]->currentCity;
    $result["pm25"]=$resObj->results[0]->pm25;
    $result["index"]=$resObj->results[0]->index;
}else{
    echo $res;exit;
}
?>
<!DOCTYPE>
<html>
    <head>
        <title>天气查询</title>
        <style type="text/css">
            table.gridtable {
                font-family: verdana,arial,sans-serif;
                font-size:11px;
                color:#333333;
                border-width: 1px;
                border-color: #666666;
                border-collapse: collapse;
            }
            table.gridtable th {
                border-width: 1px;
                padding: 8px;
                border-style: solid;
                border-color: #666666;
                background-color: #dedede;
            }
            table.gridtable td {
                border-width: 1px;
                padding: 8px;
                border-style: solid;
                border-color: #666666;
                background-color: #ffffff;
            }
        </style>
    </head>
    <body>
        <table>
        <tr><td>当前城市:</td><td><?php echo $result["currentCity"];?></td>
        <td style="padding-left:50px;">PM2.5:</td><td><?php echo $result["pm25"];?></td></tr>
        </table>
        <table class="gridtable">
        <tr>
            <th><?php echo $weather[0]->date;?></th>
            <th><?php echo $weather[1]->date;?></th>
            <th><?php echo $weather[2]->date;?></th>
            <th><?php echo $weather[3]->date;?></th>
        </tr>
        <tr>
            <td><img src=<?php echo $weather[0]->dayPictureUrl;?>> <img src=<?php echo $weather[0]->nightPictureUrl;?>> </td>
            <td><img src=<?php echo $weather[1]->dayPictureUrl;?>> <img src=<?php echo $weather[1]->nightPictureUrl;?>></td>
            <td><img src=<?php echo $weather[2]->dayPictureUrl;?>> <img src=<?php echo $weather[2]->nightPictureUrl;?>></td>
            <td><img src=<?php echo $weather[3]->dayPictureUrl;?>> <img src=<?php echo $weather[3]->nightPictureUrl;?>></td>
        </tr>
        <tr>
            <td><?php echo $weather[0]->weather;?></td>
            <td><?php echo $weather[1]->weather;?></td>
            <td><?php echo $weather[2]->weather;?></td>
            <td><?php echo $weather[3]->weather;?></td>
        </tr>
        <tr>
            <td><?php echo $weather[0]->wind;?></td>
            <td><?php echo $weather[1]->wind;?></td>
            <td><?php echo $weather[2]->wind;?></td>
            <td><?php echo $weather[3]->wind;?></td>
        </tr>
        <tr>
            <td><?php echo $weather[0]->temperature;?></td>
            <td><?php echo $weather[1]->temperature;?></td>
            <td><?php echo $weather[2]->temperature;?></td>
            <td><?php echo $weather[3]->temperature;?></td>
        </tr>
        </table>
        <p>
        <table class="gridtable" style="width:500px;">
        <tr style="text-align:center;">
            <th><?php echo $result["index"][0]->tipt;?></th>
            <th><?php echo $result["index"][1]->tipt;?></th>
            <th><?php echo $result["index"][2]->tipt;?></th>
            <th><?php echo $result["index"][3]->tipt;?></th>
            <th><?php echo $result["index"][4]->tipt;?></th>
        </tr>
        <tr style="text-align:center">
            <td><?php echo $result["index"][0]->zs;?></td>
            <td><?php echo $result["index"][1]->zs;?></td>
            <td><?php echo $result["index"][2]->zs;?></td>
            <td><?php echo $result["index"][3]->zs;?></td>
            <td><?php echo $result["index"][4]->zs;?></td>
        </tr>
        <tr>
            <td><?php echo $result["index"][0]->des;?></td>
            <td><?php echo $result["index"][1]->des;?></td>
            <td><?php echo $result["index"][2]->des;?></td>
            <td><?php echo $result["index"][3]->des;?></td>
            <td><?php echo $result["index"][4]->des;?></td>
        </tr>
        </table>
    </body>
</html>