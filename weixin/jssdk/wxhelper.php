<?php
/**
 * 给微信JS-SDK提供需要的信息
 * 
 */
require_once ("../https_method.php");
// require_once ("./https_method.php");

// 获取普通access_token>>获取jsapi_ticket>>计算签名>>获取配置
// echo $_POST['url'];
echo t_wx_config();