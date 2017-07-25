#!/bin/bash
#函数
function CheckStatus(){
if [ $? == 0 ] 
then
echo '[成功]'
else
echo '[失败]'
sudo cat ${ec_setuplog}
sudo rm -f ${ec_setuplog}
unset ec_setuplog
exit
fi
}
ec_setuplog='ec_setup.log'

echo -e "\033[33;1m注意: 一键安装需要切换到root用户进行.\033[0m"

#查找本地包
gz=`ls onex_ecstore*.gz`
for gzfile in $gz
do
if [ -f $gzfile ]; then 
	echo -n -e "请确认是否需要安装此包:\n${gzfile}(Y/N)";
	read confirm
	if [ ${confirm} == "Y" -o ${confirm} == "y" ]
	then
	package=$gzfile
	break
	fi
	unset confirm
fi
done
unset gzfile
unset gz
if [ -z "$package" ]; then printf '没有选择合适的安装包,安装中止.\n'; unset ec_setuplog; exit; fi;

#确定安装选定的包,开始安装环境
printf '开始安装......'"\n"
printf '关闭SELinux......'
sudo setenforce 0 >${ec_setuplog} 2>&1
if [ -s /etc/selinux/config ]; then
	if [ ! -f /etc/selinux/config.peter.bak ]; then sudo cp /etc/selinux/config /etc/selinux/config.peter.bak; fi
	sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
fi
CheckStatus

printf '安装wget......'
sudo yum install wget -y >${ec_setuplog}
CheckStatus
#进入yum目录
cd /etc/yum.repos.d/
printf '配置商派yum资源......'
if [ ! -f shopex-lnmp.repo ]; then
sudo wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo >${ec_setuplog} 2>&1
fi
CheckStatus
printf '安装epel扩展源......'
sudo yum install epel-release -y >${ec_setuplog} 2>&1
CheckStatus
printf '安装PHP......'
sudo yum install php-fpm56 Zend56 -y >${ec_setuplog} 2>&1
CheckStatus
printf '安装Nginx......'
sudo yum install ngx_openresty -y >${ec_setuplog} 2>&1
CheckStatus
printf 'CentOS6.8自带Mysql5.1需删除......'
sudo yum list installed mysql|grep 5.1 >${ec_setuplog} 2>&1
if [ $? == 1 ]; then
echo '[无自带]'
else
sudo yum remove mysql -y >${ec_setuplog} 2>&1
CheckStatus
fi
printf '安装Mysql......'
sudo yum install mysql -y >${ec_setuplog} 2>&1
CheckStatus

if [ ! -f /etc/sysconfig/iptables.peter.bak ]; then sudo cp /etc/sysconfig/iptables /etc/sysconfig/iptables.peter.bak; fi
printf '开放80端口......'
#这里注意是用-I参数, 表示规则插在最前面, 如果用-A参数, 则会限制防问
sudo cat /etc/sysconfig/iptables|grep "\-\-dport 80"|grep "INPUT"|grep "ACCEPT" >${ec_setuplog} 2>&1
if [ $? == 1 ]; then 
	#INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
	sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT >${ec_setuplog} 2>&1
	CheckStatus
else
	echo '[已开放]'	
fi
printf '开放3306端口......'
sudo cat /etc/sysconfig/iptables|grep "\-\-dport 3306"|grep "INPUT"|grep "ACCEPT" >${ec_setuplog} 2>&1

if [ $? == 1 ]; then
	sudo iptables -I INPUT -p tcp --dport 3306 -j ACCEPT >${ec_setuplog} 2>&1
	CheckStatus
else
	echo '[已开放]'
fi
printf '开放21端口......'
sudo cat /etc/sysconfig/iptables|grep "\-\-dport 21"|grep "INPUT"|grep "ACCEPT" >${ec_setuplog} 2>&1

if [ $? == 1 ]; then
	sudo iptables -I INPUT -p tcp --dport 21 -j ACCEPT >${ec_setuplog} 2>&1
	CheckStatus
else
	echo '[已开放]'
fi
printf '开放40000~40080端口......'
sudo cat /etc/sysconfig/iptables|grep "\-\-dport 40000:40080"|grep "INPUT"|grep "ACCEPT" >${ec_setuplog} 2>&1

if [ $? == 1 ]; then
	sudo iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport 40000:40080 -j ACCEPT >${ec_setuplog} 2>&1
	CheckStatus
else
	echo '[已开放]'
fi
printf '保存端口配置......'
#这个需要注意用户是否有权限
sudo /etc/rc.d/init.d/iptables save >${ec_setuplog} 2>&1
CheckStatus
printf '重启防火墙......'
sudo service iptables restart >${ec_setuplog} 2>&1
CheckStatus
printf "解压${package}......"
sudo mkdir -p /data/httpd >${ec_setuplog}
#注意此时当前路径是在/etc/yum.repos.d/,需注意控制路径(研究了很久才发现问题所在)
cd - >${ec_setuplog}
sudo tar -zxf ${package} -C /data/httpd >${ec_setuplog} 2>&1
CheckStatus
unset package
printf '配置Zend解密文件......'
if [ -f /usr/local/php53/etc/php.d/Zend.ini ]; then
zendfile='/usr/local/php53/etc/php.d/Zend.ini'
phpfile='/usr/local/php53/bin/php'
elif [ -f /usr/local/php/etc/php.d/Zend.ini ]; then
zendfile='/usr/local/php/etc/php.d/Zend.ini'
phpfile='/usr/local/php/bin/php'
else
echo '[失败]'
unset zendfile
sudo rm -f ${ec_setuplog}
unset ec_setuplog
exit
fi 
if [ ! -f ${zendfile}.peter.bak ]; then sudo cp ${zendfile} ${zendfile}.peter.bak; fi
sudo sed -i '/zend_loader.license_path/d' ${zendfile} >${ec_setuplog} 2>&1
sudo sed -i "\$a zend_loader.license_path='/data/httpd/ecstore/config/developer.zl'" ${zendfile} >${ec_setuplog} 2>&1
CheckStatus
unset zendfile
printf '修改网站目录为/data/httpd/ecstore/......'
nginxconf='/usr/local/nginx/conf/vhosts/default.conf'
if [ ! -f ${nginxconf}.peter.bak ]; then sudo cp ${nginxconf} ${nginxconf}.peter.bak; fi
if [ -f ${nginxconf} ]; then
sudo sed -i '/root/d' ${nginxconf}
#sudo sed -i 'i/root \/data\/httpd\/ecstore\/;' ${nginxconf}
sudo sed -i '/index/a root \/data\/httpd\/ecstore\/;' ${nginxconf}
CheckStatus
else
echo '[失败:找不到配置文件]'
unset nginxconf
sudo rm -f ${ec_setuplog}
unset ec_setuplog
exit
fi
unset nginxconf
printf '重启PHP服务......'
if [ -f /etc/init.d/php-fpm53 ]; then
sudo service php-fpm53 restart >${ec_setuplog} 2>&1
CheckStatus
phpservice="php-fpm53"
elif [ -f /etc/init.d/php-fpm ]; then
sudo service php-fpm restart >${ec_setuplog} 2>&1
CheckStatus
phpservice="php-fpm"
else
echo '[失败]'
sudo rm -f ${ec_setuplog}
unset ec_setuplog
exit
fi
printf '开机自启动PHP服务......'
sudo chkconfig ${phpservice} on >${ec_setuplog} 2>&1
CheckStatus
unset phpservice
printf '重启NGINX服务......'
sudo service nginx restart >${ec_setuplog} 2>&1
CheckStatus
printf '开机自启动NGINX服务......'
sudo chkconfig nginx on >${ec_setuplog} 2>&1
CheckStatus
printf '重启MYSQL服务......'
sudo service mysqld restart >${ec_setuplog} 2>&1
CheckStatus
printf '开机自启动MYSQL服务......'
sudo chkconfig mysqld on
CheckStatus
printf '创建ecstore数据库......'
dbexists=`mysql -uroot -e"select 1 from information_schema.schemata where schema_name='ecstore';"`
if [ -z "${dbexists}" ]; then 
mysql -uroot -e"create database ecstore;" >${ec_setuplog} 2>&1
CheckStatus
else
echo '[已存在]'
fi
printf '授权用户使用ecstore数据库......'
mysql -uroot -e"grant all privileges on ecstore.* to 'ec_admin'@'%' identified by 'ec_admin@123';" >${ec_setuplog} 2>&1
CheckStatus
printf '定时任务配置......'
echo "* * * * * /data/httpd/ecstore/script/queue/queue.sh ${phpfile} > /dev/null" >peter.crontab.tmp
echo "* * * * * ${phpfile} /data/httpd/ecstore/script/crontab/crontab.php >/dev/null" >>peter.crontab.tmp
sudo crontab -uwww peter.crontab.tmp >${ec_setuplog} 2>&1
CheckStatus
rm -f peter.crontab.tmp
printf '安装vsftp......'
sudo yum install vsftpd -y >${ec_setuplog} 2>&1
CheckStatus
printf '修改FTP配置......'
ftpconf='/etc/vsftpd/vsftpd.conf'
if [ ! -f ${ftpconf}.peter.bak ]; then sudo cp ${ftpconf} ${ftpconf}.peter.bak; fi
sudo sed -i '/#设定不允许匿名访问/d' ${ftpconf} >${ec_setuplog} 2>&1 
sudo sed -i '/anonymous_enable=NO/d' ${ftpconf} >${ec_setuplog} 2>&1 
sudo sed -i '/#使用户不能离开主目录/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/chroot_list_enable=YES/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/#启用上传的ASCII传输方式/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/ascii_upload_enable=YES/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/#启用下载的ASCII传输方式/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/ascii_download_enable=YES/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/#设定支持ASCII模式的上传和下载功能/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/ascii_download_enable=YES/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/#指定虚拟用户的宿主用户/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/guest_username=ftp/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/#设定虚拟用户个人vsftp的CentOS FTP服务文件存放路径/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/user_config_dir=/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/chroot_list_file=/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/#开启PASV模式/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/pasv_enable=YES/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/pasv_min_port=40000/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/pasv_max_port=40080/d' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '/pasv_promiscuous=YES/d' ${ftpconf} >${ec_setuplog} 2>&1
#sed多行模式暂研究, 暂用单行
sudo sed -i '$a\#设定不允许匿名访问' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\anonymous_enable=NO' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\#使用户不能离开主目录' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\chroot_list_enable=YES' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\#启用上传的ASCII传输方式' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\ascii_upload_enable=YES' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\#启用下载的ASCII传输方式' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\ascii_download_enable=YES' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\#设定支持ASCII模式的上传和下载功能' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\ascii_download_enable=YES' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\#设定启用虚拟用户功能' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\guest_enable=YES' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\#指定虚拟用户的宿主用户，CentOS中已经有内置的ftp用户了' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\guest_username=ftp' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\user_config_dir=/etc/vsftpd/vuser_conf' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\chroot_list_file=/etc/vsftpd/vuser_passwd.txt' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\#开启PASV模式 （被动式）' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\pasv_enable=YES' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\pasv_min_port=40000' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\pasv_max_port=40080' ${ftpconf} >${ec_setuplog} 2>&1
sudo sed -i '$a\pasv_promiscuous=YES' ${ftpconf} >${ec_setuplog} 2>&1
CheckStatus
unset ftpconf
printf '安装虚拟用户管理工具db4......'
sudo yum install db4 db4-utils -y >${ec_setuplog} 2>&1
CheckStatus
printf '创建用户文件......'
ftptxt='/etc/vsftpd/vuser_passwd.txt'
sudo echo 'ec_ftp' >${ftptxt}
sudo echo 'ec_ftp@123'>>${ftptxt}
CheckStatus
printf '生成虚拟用户认证文件......'
ftpdb='/etc/vsftpd/vuser_passwd.db'
sudo db_load -T -t hash -f ${ftptxt} ${ftpdb}
CheckStatus
#认证完成,可以删除txt文件的密码行
sudo sed -i '/ec_ftp@123/d' ${ftptxt} >${ec_setuplog} 2>&1
unset ftptxt
unset ftpdb
printf '编辑FTP上传文件......'
if [ ! -f '/etc/padm.d/vsftpd.peter.bak' ]; then sudo cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.peter.bak; fi
sudo echo 'auth required pam_userdb.so db=/etc/vsftpd/vuser_passwd' >/etc/pam.d/vsftpd
sudo echo 'account required pam_userdb.so db=/etc/vsftpd/vuser_passwd' >>/etc/pam.d/vsftpd
CheckStatus
printf '创建虚拟用户配置文件夹......'
sudo mkdir -p /etc/vsftpd/vuser_conf
CheckStatus
printf '创建用户文件......'
ftpuser='/etc/vsftpd/vuser_conf/ec_ftp'
sudo echo 'local_root=/data/ftp' >${ftpuser}
sudo echo 'write_enable=YES' >>${ftpuser}
sudo echo 'anon_umask=022' >>${ftpuser}
sudo echo 'anon_world_readable_only=NO' >>${ftpuser}
sudo echo 'anon_upload_enable=YES' >>${ftpuser}
sudo echo 'anon_mkdir_write_enable=YES' >>${ftpuser}
sudo echo 'anon_other_write_enable=YES' >>${ftpuser}
CheckStatus
printf '创建FTP根目录及权限......'
sudo mkdir -p /data/ftp
chmod -R 777 /data/ftp
chown -R ftp:www /data/ftp
CheckStatus
printf '重启FTP服务......'
sudo service vsftpd restart >${ec_setuplog} 2>&1
CheckStatus
printf '开机自启动FTP服务......'
sudo chkconfig vsftpd on
CheckStatus
printf '修改ecstore目录权限......'
sudo chown -R www:www /data/httpd/ecstore >${ec_setuplog} 2>&1
CheckStatus
echo 'Mysql 用户名: ec_admin'
echo 'Mysql 密  码: ec_admin@123'
echo 'FTP   用户名: ec_ftp'
echo 'FTP   密  码: ec_ftp@123'
echo "注意开启config.php的php56配置:define('EC_PHP_VERSION','php5.6')"
sudo rm -f ${ec_setuplog}
unset ec_setuplog




