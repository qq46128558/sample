#!/bin/bash
# 注意这里调用service命令需要全路径
/sbin/service mysqld status
# 发现服务停止了
if [ $? == 3 ]; then
# 发送邮件提醒,但不重复发送
	if [ ! -e /root/sent.email ]
	then
		# 调用发邮件的php程序(如果php-fpm停了可能没效果?)
		/usr/local/php56/bin/php /data/httpd/b2b2c/service_stop_notice.php >/root/sent.email
		# 记录时间,已发送
		date>>/root/sent.email  
	fi 
fi
