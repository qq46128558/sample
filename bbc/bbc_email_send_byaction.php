<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

try{
        $type='email';
        $sendTo='46128558@qq.com';
        //action名称
        $tmpl='account-member';
        //变量替换
        $content['shopname']='XXX小姐';
        $content['vcode']='666666';
        $messenger=new system_messenger();
        $sendResult = $messenger->sendMessenger($type,$sendTo,$tmpl,$content);
        //var_dump($sendResult);
        if ($sendResult && $sendResult['rsp']=='succ'){
                echo '邮件发送成功.';
        }else{
                echo '邮件发送失败:'.$sendResult['err_msg'];
        }
}catch(Exception $e){
        echo '邮件发送失败: '.$e->getMessage();
}