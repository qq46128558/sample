<?php  
// error_reporting(E_ALL & ~E_NOTICE);
require(__DIR__.'/../vendor/PHPMailer/class.phpmailer.php');  
  
$mail = new PHPMailer(); //实例化  
  
$mail->IsSMTP(); // 启用SMTP  
  
$mail->Host = "smtp.exmail.qq.com"; //SMTP服务器 163邮箱例子  
  
$mail->Port = 25;  //邮件发送端口  
$mail->SMTPAuth   = true;  //启用SMTP认证  
  
$mail->CharSet  = "UTF-8"; //字符集  
$mail->Encoding = "base64"; //编码方式  
  
$mail->Username = "dgw@yn-ce.com";  //你的邮箱  
$mail->Password = "XXX";  //你的密码  
$mail->Subject = "带多个附件的邮件测试"; //邮件标题  
  
$mail->From = "dgw@yn-ce.com";  //发件人地址（也就是你的邮箱）  
$mail->FromName = "Peter";   //发件人姓名  
  
$address1 = "46128558@qq.com";//收件人email  
$mail->AddAddress($address1, "46128558");    //添加收件人1（地址，昵称）  
  
$mail->AddAttachment('E:\TDDownLoad\1353022505371.jpg','1353022505371.jpg'); // 添加附件,并指定名称  
$mail->AddAttachment('E:\TDDownLoad\07_01 290x293.jpg','07_01 290x293.jpg'); // 可以添加多个附件  
  
$mail->IsHTML(true); //支持html格式内容  
// $mail->AddEmbeddedImage("logo.jpg", "my-attach", "logo.jpg"); //设置邮件中的图片  
$mail->Body = '你好, <b>朋友</b>! <br/>这是一封邮件！'; //邮件主体内容  
  
//发送  
if(!$mail->Send()) {  
  echo "发送失败: " . $mail->ErrorInfo;  
} else {  
  echo "成功";  
}  
?>  
