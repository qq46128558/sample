<?php
define('ROOT_DIR',realpath(__DIR__.'/../../ecstore/'));
require_once ROOT_DIR.'/app/base/kernel.php';
require_once ROOT_DIR.'/app/base/autoload.php';
require_once ROOT_DIR.'/config/config.php';
require_once ROOT_DIR.'/app/base/ego/ego.php';
require_once ROOT_DIR.'/config/mapper.php';
require_once ROOT_DIR.'/app/base/defined.php';
error_reporting(E_ALL ^ E_NOTICE);


try{
                $sendTo='13928016056';
                $title='测试';
                $contents='发送测试短信内容';
                $config['sendType']='notice';
                $config['use_reply']='false';
                $sendResult = kernel::single('b2c_messenger_sms')->send($sendTo,$title,$contents,$config);
                if ($sendResult){
                	echo $sendResult;
                }else{
                	echo '短信发送成功.';
                }
        }catch(Exception $e){
                echo '短信发送失败: '.$e->getMessage();
        }

