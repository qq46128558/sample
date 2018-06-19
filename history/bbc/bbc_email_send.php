<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

try{
        $sendTo='46128558@qq.com';
        $title='测试邮件标题';
        $contents='测试邮件内容';
        $config['sendType']='notice';
        $config['use_reply']='false';
        $email=new system_messenger_email();
        $sendResult = $email->send($sendTo,$title,$contents,$config);
        //var_dump($sendResult);
        echo '邮件发送成功.';
}catch(Exception $e){
        echo '邮件发送失败: '.$e->getMessage();
}