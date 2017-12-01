#!/bin/bash
echo -e "\033[33;1m注意: 一键安装需要切换到root用户进行.\033[0m"

#查找本地包
gz=`ls b2b2c-*.gz`
for gzfile in $gz
do
if [ -f $gzfile ]; then 
	echo -n -e "请确认是否需要安装bbc:\n${gzfile}(Y/N)";
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
if [ -z "$package" ]; then printf '没有选择合适的bbc安装包,安装中止.\n'; exit; fi;


printf '开始安装......'"\n"
printf '关闭SELinux......'
setenforce 0 >setup_log 2>&1

if [ -s /etc/selinux/config ]; then
	if [ ! -s /etc/selinux/config.lkb.bak ]; then cp /etc/selinux/config /etc/selinux/config.lkb.bak; fi;
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config


fi

function check()
{
if [ $? == 0 ]
then
 echo '成功'
else
echo '失败'
cat setup_log
exit
fi
}

check

printf '安装Wget.....'
yum install wget -y >>setup_log 2>&1
check



#进入YUM目录
printf '下载商派yum源......'
cd /etc/yum.repos.d/
if [ ! -f shopex-lnmp.repo ] ; then
wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo >setup_log 2>&1
fi
check


printf '安装epel扩展源......'
yum install epel-release -y >>setup_log 2>&1
check
printf '安装PHP......'
yum install php-fpm56 Zend56 php-memcached56 memcached -y >>setup_log 2>&1
check
printf '安装Nginx......'
yum install ngx_openresty -y >>setup_log 2>&1
check


printf 'CentOS6.8自带Mysql5.1需删除......'
yum list installed mysql|grep 5.1 >>setup_log 2>&1
if [ $? == 1 ]; then
echo '[无自带]'
else
yum remove mysql -y >>setup_log 2>&1
check
fi
printf '安装Mysql......'
yum install mysql -y >setup_log 2>&1
check



if [ ! -f /etc/sysconfig/iptables.lkb.bak ]; then cp /etc/sysconfig/iptables /etc/sysconfig/iptables.lkb.bak; fi



printf '安装Redis......'
yum install  redis -y >setup_log 2>&1
check



printf '开放80端口......'
#这里注意是用-I参数, 表示规则插在最前面, 如果用-A参数, 则会限制防问
cat /etc/sysconfig/iptables|grep "\-\-dport 80"|grep "INPUT"|grep "ACCEPT" >>setup_log 2>&1
if [ $? == 1 ]; then 
	iptables -I INPUT -p tcp --dport 80 -j ACCEPT >>setup_log 2>&1
	check
else
	echo '[已开放]'	
fi
printf '开放3306端口......'
cat /etc/sysconfig/iptables|grep "\-\-dport 3306"|grep "INPUT"|grep "ACCEPT" >>setup_log 2>&1

if [ $? == 1 ]; then
	iptables -I INPUT -p tcp --dport 3306 -j ACCEPT >>setup_log 2>&1
	check
else
	echo '[已开放]'
fi
printf '开放21端口......'
cat /etc/sysconfig/iptables|grep "\-\-dport 21"|grep "INPUT"|grep "ACCEPT" >>setup_log 2>&1

if [ $? == 1 ]; then
	iptables -I INPUT -p tcp --dport 21 -j ACCEPT >>setup_log 2>&1
	check
else
	echo '[已开放]'
fi


printf '开放6379端口......'
cat /etc/sysconfig/iptables|grep "\-\-dport 6379"|grep "INPUT"|grep "ACCEPT" >>setup_log 2>&1

if [ $? == 1 ]; then
	iptables -I INPUT -p tcp --dport 6379 -j ACCEPT >>setup_log 2>&1
	check
else
	echo '[已开放]'
fi


printf '开放40000~40080端口'
cat /etc/sysconfig/iptables|grep "\-\-dport 40000:40080"|grep "INPUT"|grep "ACCEPT" >>setup_log 2>&1

if [ $? == 1 ]; then
	iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport 40000:40080 -j ACCEPT >>setup_log 2>&1
	check
else
	echo '[已开放]'
fi




printf '保存端口配置......'
#这个需要注意用户是否有权限
/etc/rc.d/init.d/iptables save >>setup_log 2>&1
check

printf '重启防火墙......'
service iptables restart >>setup_log 2>&1
check



mkdir -p /data/httpd

printf "解压${package}...."
cd - >/dev/null
sudo tar -zxf ${package} -C /data/httpd >/dev/null 2>&1
check
unset package


printf '配置zend解密文件。。。。'
zendfile='/usr/local/php56/etc/php.d/Zend.ini'
phpfile='/usr/local/php56/bin/php'
if [ ! -f ${zendfile}.lkb.bak ] ; then cp ${zendfile} ${zendfile}.lkb.bak;fi
sed -i '/zend_loader.license_path/d' ${zendfile} >>setup_log 2>&1

sed -i "\$a zend_loader.license_path='/data/httpd/b2b2c/config/developer.zl'" ${zendfile} >/dev/null 2>&1


check 
unset zendfile



printf '修改网站目录为/data/httpd/b2b2c/public....'
nginxconf='/usr/local/nginx/conf/vhosts/default.conf'
if [ ! -f ${nginxconf}.lkb.bak ];then cp ${nginxconf} ${nginxconf}.lkb.bak;fi
sed -i '/root/d' ${nginxconf}
sed -i '/index/a root \/data\/httpd\/b2b2c\/public\/;' ${nginxconf}
check
unset nginxconf

printf '重启PHP服务......'
service php-fpm56 restart >setup_log 2>&1
check 

printf '开机自启动php服务'
chkconfig php-fpm56 on >setup_log 2>&1
check


printf '重启nginx服务......'
service nginx restart >setup_log 2>&1
check      

printf '开机自启动nginx服务'
chkconfig nginx on >setup_log 2>&1
check


printf '重启mysql服务......'
service mysqld restart >setup_log 2>&1
check

printf '开机自启动mysql服务'
chkconfig mysqld on >setup_log 2>&1
check



printf '重启redis服务......'
service redis restart >setup_log 2>&1
check

printf '开机自启动redis服务'
chkconfig redis on >setup_log 2>&1
check


printf '创建bbc数据库......'
dbexists=`mysql -uroot -e"select 1 from information_schema.schemata where schema_name='bbc';"`
if [ -z "${dbexists}" ]; then 
mysql -uroot  -e"create database bbc;" >set_log 2>&1
check
else
echo '已存在'
fi


printf '授权用户使用bbc数据库......'
mysql -uroot  -e"grant all privileges on bbc.* to 'ec_admin'@'%' identified by 'ec_admin@123';" >setup_log 2>&1
check

printf '定时任务配置......'
echo "* * * * * /data/httpd/b2b2c/script/queue/queue.sh ${phpfile} > /dev/null" >lkb.crontab.tmp
echo "* * * * * ${phpfile} /data/httpd/b2b2c/script/crontab/crontab.php >/dev/null" >>lkb.crontab.tmp
sudo crontab -uwww lkb.crontab.tmp >setup_log 2>&1
check
rm -f lkb.crontab.tmp


printf '安装vsftp......'
yum install vsftpd -y >setup_log 2>&1
check
printf '修改FTP配置......'
ftpconf='/etc/vsftpd/vsftpd.conf'
if [ ! -f ${ftpconf}.lkb.bak ]; then  cp ${ftpconf} ${ftpconf}.lkb.bak; fi
sed -i '/#设定不允许匿名访问/d' ${ftpconf}
sed -i '/anonymous_enable=NO/d' ${ftpconf}
sed -i '/#使用户不能离开主目录/d' ${ftpconf}
sed -i '/chroot_list_enable=YES/d' ${ftpconf}
sed -i '/#启用上传的ASCII传输方式/d' ${ftpconf}
sed -i '/ascii_upload_enable=YES/d' ${ftpconf}
sed -i '/#启用下载的ASCII传输方式/d' ${ftpconf}
sed -i '/ascii_download_enable=YES/d' ${ftpconf}
sed -i '/#设定支持ASCII模式的上传和下载功能/d' ${ftpconf}
sed -i '/ascii_download_enable=YES/d' ${ftpconf}
sed -i '/#指定虚拟用户的宿主用户/d' ${ftpconf}
sed -i '/guest_username=ftp/d' ${ftpconf}
sed -i '/#设定虚拟用户个人vsftp的CentOS FTP服务文件存放路径/d' ${ftpconf}
sed -i '/user_config_dir=/d' ${ftpconf}
sed -i '/chroot_list_file=/d' ${ftpconf}
sed -i '/#开启PASV模式/d' ${ftpconf}
sed -i '/pasv_enable=YES/d' ${ftpconf}
sed -i '/pasv_min_port=40000/d' ${ftpconf}
sed -i '/pasv_max_port=40080/d' ${ftpconf}
sed -i '/pasv_promiscuous=YES/d' ${ftpconf}
#sed多行模式未研究, 暂用单行
sed -i '$a\#设定不允许匿名访问' ${ftpconf}
sed -i '$a\anonymous_enable=NO' ${ftpconf}
sed -i '$a\#使用户不能离开主目录' ${ftpconf}
sed -i '$a\chroot_list_enable=YES' ${ftpconf}
sed -i '$a\#启用上传的ASCII传输方式' ${ftpconf}
sed -i '$a\ascii_upload_enable=YES' ${ftpconf}
sed -i '$a\#启用下载的ASCII传输方式' ${ftpconf}
sed -i '$a\ascii_download_enable=YES' ${ftpconf}
sed -i '$a\#设定支持ASCII模式的上传和下载功能' ${ftpconf}
sed -i '$a\ascii_download_enable=YES' ${ftpconf}
sed -i '$a\#设定启用虚拟用户功能' ${ftpconf}
sed -i '$a\guest_enable=YES' ${ftpconf}
sed -i '$a\#指定虚拟用户的宿主用户，CentOS中已经有内置的ftp用户了' ${ftpconf}
sed -i '$a\guest_username=ftp' ${ftpconf}
sed -i '$a\user_config_dir=/etc/vsftpd/vuser_conf' ${ftpconf}
sed -i '$a\chroot_list_file=/etc/vsftpd/vuser_passwd.txt' ${ftpconf}
sed -i '$a\#开启PASV模式 （被动式）' ${ftpconf}
sed -i '$a\pasv_enable=YES' ${ftpconf}
sed -i '$a\pasv_min_port=40000' ${ftpconf}
sed -i '$a\pasv_max_port=40080' ${ftpconf}
sed -i '$a\pasv_promiscuous=YES' ${ftpconf}
check
unset ftpconf


printf '安装虚拟用户管理工具db4......'
yum install db4 db4-utils -y >setup_log 2>&1
check
printf '创建用户文件......'
ftptxt='/etc/vsftpd/vuser_passwd.txt'
echo 'ec_ftp' >${ftptxt}
echo 'ec_ftp@123'>>${ftptxt}
check
printf '生成虚拟用户认证文件......'
ftpdb='/etc/vsftpd/vuser_passwd.db'
db_load -T -t hash -f ${ftptxt} ${ftpdb}
check
unset ftptxt
unset ftpdb
#认证完成，可以删除txt文件的密码行
sed -i '/ec_ftp@123/d' ${ftptxt}>>setup_log 2>&1

printf '编辑FTP上传文件......'
if [ ! -f '/etc/padm.d/vsftpd.peter.bak' ]; 
then cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.lkb.bak; 
fi
echo 'auth required pam_userdb.so db=/etc/vsftpd/vuser_passwd' >/etc/pam.d/vsftpd
echo 'account required pam_userdb.so db=/etc/vsftpd/vuser_passwd' >>/etc/pam.d/vsftpd
check


printf '创建虚拟用户配置文件夹......'
mkdir -p /etc/vsftpd/vuser_conf
check

printf '创建用户文件......'
ftpuser='/etc/vsftpd/vuser_conf/ec_ftp'
echo 'local_root=/data/ftp' >${ftpuser}
echo 'write_enable=YES' >>${ftpuser}
echo 'anon_umask=022' >>${ftpuser}
echo 'anon_world_readable_only=NO' >>${ftpuser}
echo 'anon_upload_enable=YES' >>${ftpuser}
echo 'anon_mkdir_write_enable=YES' >>${ftpuser}
echo 'anon_other_write_enable=YES' >>${ftpuser}
check



printf '创建FTP根目录及权限......'
mkdir -p /data/ftp
chmod -R 774 /data/ftp
chown -R ftp:www /data/ftp
check

printf '重启vsftpd服务......'
service vsftpd restart >setup_log 2>&1
check

printf '开机自启动FTP服务......'
chkconfig vsftpd on
check

printf '修改bbc目录权限......'
chown -R www:www /data/httpd
check


echo 'Mysql 用户名: ec_admin'
echo 'Mysql 密  码: ec_admin@123'
echo 'FTP   用户名: ec_ftp'
echo 'FTP   密  码: ec_ftp@123'
rm -f setup_log

# 配置host
# /etc/hosts
# 127.0.0.1 %CONNECTIONS.DEFAULT.HOST%
# 重启nginx