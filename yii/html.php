<?php
/**
 * 引入Yii框架基类的代码
 */
// comment out the following two lines when deployed to production
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');

require(__DIR__ . '/../vendor/autoload.php');
require(__DIR__ . '/../vendor/yiisoft/yii2/Yii.php');

$config = require(__DIR__ . '/../config/web.php');

(new yii\web\Application($config));
?>

<!-- HTML代码 -->
<html>
<!DOCTYPE>
<head>
<script src="./assets/69345674/jquery.min.js"></script>
<script type="text/javascript">

'use strict';

// 蟹宝盒post接口测试
// Yii::$app->request->csrfToken
// $('meta[name="csrf-token"]').attr("content");
$(function(){

// JS中调PHP
var csrftoken="<?php echo Yii::$app->request->csrfToken;?>";
console.log(csrftoken);

var activityId="5aa64336f8990b4d9c82fdcb";
var user={
  "userId":"oRnBdwv0rXOiUWFt_UvC1ZyMBJuo",
  "nickName":"Peter",
  "headImgUrl":"http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJ4gfafuPCFibAfhWc5d41EI4ad6KWfP4IGbIzouLYJhUqQufsS1brmNZSsCEEoTPica5Ywic9F5dLTQ/132",
};
var data={
  "name":"guiwen","phone":"13928016056","product":"蟹宝盒","area":"珠海",
}
var mobile="13928016056";
var shareUserId="";

$.ajax({
    type: "post",
    // url: "http://192.168.66.128/apply/dev/main/submit",
    url: "http://192.168.239.136/apply/dev/main/submit",
    data: {_csrf:csrftoken,activityId:activityId, user:user,data:data,mobile:mobile,shareUserId:shareUserId},
    anysc: false,
    success: function (data) {
        // console.log(data);
        var responseText=data;
        responseText = unescape(responseText.replace(/\\/g, "%"));
        $('#responsetext').get(0).innerText=responseText;
        // document.getElementById("responsetext").innerText=responseText;
    },
    error: function (e) {
        alert('接口调用错误,请到控制台查看详细的错误信息.')
        console.log(e);
        $('#responsetext').get(0).innerText=e.responseText;
        // document.getElementById("responsetext").innerText=e.responseText;
    },
    complete: function(data){
        console.log(data);
        // var responseText=data.responseText;
        // responseText = unescape(responseText.replace(/\\/g, "%"));
        // console.log(responseText);
    }
});
});
</script>
</head>
<body>
  <!-- <div id="csrftoken"></div> -->
  <div id='responsetext'></div>
</body>
</html>
