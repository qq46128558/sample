<?php
/*
配合检查mysqld服务是否停止的脚本(servicecheck.sh)使用
利用b2b2c的核心发邮件功能(不依赖mysqld服务)
发邮件提醒用户, mysqld服务已停止
*/

require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

try{
        $sendTo='dgw@yn-ce.com';
        $title='Linux服务器mysql服务异常终止提醒';
	$date=date('Y-m-d H:i:s',time());
        $contents = <<<eof
	<p>系统于$date(服务器时间)检测到预警的服务(mysqld等)异常终止,请尽快登录服务器进行问题排查.</p>
	<p>mysqld日志:/var/log/mysqld.log</p>
	<p style="color:red">问题排查结查后,请删除防止重复发送邮件的标记文件:/root/sent.email</p>
eof;
        $config['sendType']='notice';
        $config['use_reply']='false';
	$config['sendway']='smtp';
	// 密码自行修改
	$config['smtppasswd']='XXXXX';
	$config['smtpport']=25;
	$config['smtpserver']='smtp.exmail.qq.com';
	$config['smtpuname']='dgw@yn-ce.com';
	$config['usermail']='dgw@yn-ce.com';
	$objDesktopEmail = kernel::single('desktop_email_email');
	if($objDesktopEmail->ready($config))
		{
		    $result = $objDesktopEmail->send($sendTo,$title,$contents,$config);
		    if ($err = $objDesktopEmail->errorinfo)
		    {
			echo '邮件发送失败,'.$err['error'];
			exit();
		    }
		}
		else
		{
			echo '邮件发送失败,配置信息不全';
			exit();	
		}
        echo '邮件发送成功.';
}catch(Exception $e){
        echo '邮件发送失败: '.$e->getMessage();
}

