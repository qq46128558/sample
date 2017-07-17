<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

try{
        $sendTo='13928016056';
        $title='测试';
        $contents='发送测试短信内容';
        $config['sendType']='notice';
        $config['use_reply']='false';
        $sms=new system_messenger_sms();
        $sendResult = $sms->send($sendTo,$title,$contents,$config);
        echo '短信发送成功.';
}catch(Exception $e){
        echo '短信发送失败: '.$e->getMessage();
}  