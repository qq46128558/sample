#!/bin/bash
/sbin/service mysqld status
# 发现服务停止了
if [ $? == 3 ]; then
# 发送邮件提醒,但不重复发送
	if [ ! -e /root/sent.email ]
	then
		# 调用发邮件的php程序(如果php-fpm停了可能没效果?)
		# /usr/local/php56/bin/php /data/httpd/b2b2c/service_stop_notice.php >/root/sent.email
		current_time=`date`
		content="系统于$current_time(服务器时间)检测到预警的服务(mysqld等)异常终止,请尽快登录服务器进行问题排查.\nmysqld日志:/var/log/mysqld.log\n问题排查结查后,请删除防止重复发送邮件的标记文件:/root/sent.email"
		echo -e $content|mail -s "Linux服务器mysql服务异常终止提醒" dgw@yn-ce.com>/root/sent.email 	
		# 记录时间,已发送
		date>>/root/sent.email  
	fi 
fi
