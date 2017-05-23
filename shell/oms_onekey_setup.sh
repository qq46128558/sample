#!/bin/bash

echo -e "\033[33;1m注意；一键安装需要切换到root用户进行\033[0m"
#查找本地包

gz=`ls onex_ecstore*gz`

for gzfile in ${gz}
do
	echo -n -e "请确认是否需要安装此包：\n${gzfile}(y/n)";
	read confirm;
	if [ ${confirm} == "Y" -o ${confirm} == "y" ]
	then
	package=${gzfile}
	break
	fi
	unset confirm

done
unset gzfile
unset gz
if [ -z ${package} ]; then printf '没有选择合适的安装包，安装中止.\n'; exit; fi

printf '开始执行一键安装包。。。。。。。。。。。。。。。。。。。\n'
printf '关闭SELinux。。。。。。。。。。。。。。。。。。。。。。'
setenforce 0  >setup_log 2>&1
if [ -s /etc/selinux/config ]; then 
	if [ ! -s /etc/selinux/config.ycd.bak ]; then cp /etc/selinux/config /etc/selinux/config.ycd.bak; fi;
       sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
fi;

function check_status()
{
   if [ $?==0 ]
   then
      echo -e "\033[32;1m成功\033[0m"
   else 
      echo -e "\033[31;1m失败\033[0m"
      cat setup_log
      exit
   fi
}

check_status

printf '安装wget。。。。。。。。。。。。。。。。。。。。。。。'
yum install wget -y >>setup_log 2>&1
check_status

#进入yum目录
printf '开始安装yum资源。。。。。。。。。。。。。。。。。。。'
cd /etc/yum.repos.d/

if [ ! -f shopex-lnmp.repo ];then
 wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo >> setup_log 2>&1
fi
check_status

printf '安装epel扩展源。。。。。。。。。。。。。。。。。。。'
yum install epel-release -y >>setup_log 2>&1
check_status

printf '安装php。。。。。。。。。。。。。。。。。。。。。。。'
yum install php-fpm53 Zend53 -y >>setup_log 2>&1
check_status

printf '安装nginx 。。。。。。。。。。。。。。。。。。。。。'
yum install ngx_openresty -y >>setup_log 2>&1
check_status

printf '如果mysql已安装，则需要删除。。。。。。。。。。。。。'
yum list installed mysql|grep 5.1 >>setup_log 2>&1
if [ $?==1 ] 
then 
  echo '【无已安装的mysql】'
else
  yum remove mysql -y >>setup_log 2>&1
  check_status
fi

printf '安装mysql。。。。。。。。。。。。。。。。。。。。。。'
yum install mysql -y >>setup_log 2>&1
check_status

if [ ! -f /etc/sysconfig/iptables.ldward.bak ];then 
cp /etc/sysconfig/iptables /etc/sysconfig/iptables.ldward.bak;fi


printf '开放80端口。。。。。。。。。。。。。。。。。。。。。。'
cat /etc/sysconfig/iptables|grep "\-\-dport 80"|grep "INPUT"|grep "ACCEPT" >>setup_log 2>&1
if [ $? == 1 ];then
    iptables -I INPUT -p tcp --dport 80 -j ACCEPT >>setup_log 2>&1
    check_status
else
    echo '【已开放】'
fi

printf '开放3306端口。。。。。。。。。。。。。。。。。。。。。'
cat /etc/sysconfig/iptables|grep "\-\-dport 3306"|grep "INPUT"|grep "ACCEPT" >>setup_log 2>&1
if [ $? == 1 ];then
   iptables -I INPUT -p tcp --dport 3306 -j ACCEPT >>setup_log 2>&1
   check_status
else 
   echo '【已开放】'
fi


printf '开放21端口。。。。。。。。。。。。。。。。。。。。。'
cat /etc/sysconfig/iptables|grep "\-\-dport 21"|grep "INPUT"|grep "ACCEPT" >>setup.log 2>&1
if [ $? == 1 ]; then
        iptables -I INPUT -p tcp --dport 21 -j ACCEPT >>setup.log 2>&1
        check_status
else
        echo '【已开放】'
fi
printf '开放40000~40080端口。。。。。。。。。。。。。。。。。'
cat /etc/sysconfig/iptables|grep "\-\-dport 40000:40080"|grep "INPUT"|grep "ACCEPT" >>setup.log 2>&1
if [ $? == 1 ]; then
        iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport 40000:40080 -j ACCEPT >>setup.log 2>&1
        check_status
else
        echo '【已开放】'
fi

printf '保存以上所有的端口配置。。。。。。。。。。。。。。。'
/etc/rc.d/init.d/iptables save >>setup_log 2>&1
check_status

printf '重启防火墙。。。。。。。。。。。。。。。。。。。。。'
service iptables restart >>setup_log 2>&1
check_status

printf '创建ecstore 目录。。。。。。。。。。。。。。。。。。'
mkdir -p /data/httpd

check_status

printf "解压${package}。。。。。"
cd - >/dev/null

 tar -zxf ${package} -C /data/httpd >>setup_log 2>&1
check_status
unset package
check_status

printf '配置Zend解密文件。。。。。。。。。。。。。。。。。。'
if [ -f /usr/local/php53/etc/php.d/Zend.ini ]; then
 zendfile='/usr/local/php53/etc/php.d/Zend.ini'
 phpfile='/usr/local/php53/bin/php'
elif [ -f /usr/local/php/etc/php.d/Zend.ini ]; then
zendfile='/usr/local/php/etc/php.d/Zend.ini
phpfile='/usr/local/php/bin/phpi
else
echo '【失败】'
unset zendfile
exit 
fi

if [ ! -f ${zendfile}.ldward.bak ]; then cp ${zendfile} ${zendfile}.ldward.bak;fi
  sudo sed -i '/zend_loader.license_path/d' ${zendfile} >/dev/null 2>&1
  sudo sed -i "\$a zend_loader.license_path='/data/httpd/ecstore/config/developer.zl'" ${zendfile} >>setup_log 2>&1
check_status
unset zendfile
check_status

printf '修改网站目录为/data/httpd/ecstore/。。。。。。。。'
nginxconf='/usr/local/nginx/conf/vhosts/default.conf'
if [ ! -f ${nginxconf}.ldward.bak ]; then sudo cp ${nginxconf} ${nginxconf}.ldward.bak; fi
if [ -f ${nginxconf} ]; then
sudo sed -i '/root/d' ${nginxconf}
#sudo sed -i 'i/root \/data\/httpd\/ecstore\/;' ${nginxconf}
sudo sed -i '/index/a root \/data\/httpd\/ecstore\/;' ${nginxconf}
check_status
else
echo '[失败:找不到配置文件]'
unset nginxconf
exit
fi
unset nginxconf

printf '重启PHP服务。。。。。。。。。。。。。。。。。。。'
if [ -f /etc/init.d/php-fpm53 ]; then
sudo service php-fpm53 restart >/dev/null 2>&1
check_status
phpservice="php-fpm53"
elif [ -f /etc/init.d/php-fpm ]; then
sudo service php-fpm restart >/dev/null 2>&1
check_status
phpservice="php-fpm"
else
echo '[失败]'
exit
fi
printf '开机自启动PHP服务......'
sudo chkconfig ${phpservice} on >/dev/null 2>&1
check_status
unset phpservice
printf '重启NGINX服务......'
sudo service nginx restart >/dev/null 2>&1
check_status
printf '开机自启动NGINX服务......'
sudo chkconfig nginx on >/dev/null 2>&1
check_status
printf '重启MYSQL服务......'
sudo service mysqld restart >/dev/null 2>&1
check_status
printf '开机自启动MYSQL服务......'
sudo chkconfig mysqld on
check_status

printf '创建ecstore数据库。。。。。。。。。。。。。。。。'
dbexists=`mysql -uroot -e"select 1 from information_schema.schemata where schema_name='ecstore';"`
if [ -z "${dbexists}" ]; then
mysql -uroot -e"create database ecstore;" >/dev/null 2>&1
check_status
else
echo '【已存在】'
fi

printf '授权用户使用ecstore数据库。。。。。。。。。。。'
mysql -uroot -e"grant all privileges on ecstore.* to 'ec_admin'@'%' identified by 'ec_admin@123';" >>setup_log  2>&1
check_status

printf '定时任务配置。。。。。。。。。。。。。。。。。'
echo "* * * * * /data/httpd/ecstore/scirpt/queue/queue.sh ${phpfile} >/dev/null "> ldward.crontab.tmp
echo "* * * * * ${phpfile} /data/httpd/ecstore/script/crontab/crontab.php >/dev/null" >>ldward.crontab.tmp
crontab -uroot ldward.crontab.tmp >>setup_log 2>&1
check_status
rm -f ldward.crontab.tmp

printf '安装vsftp。。。。。。。。。。。。。。。。。。。'
yum install vsftpd -y >>setup_log 2>&1
check_status
printf '修改FTP配置。。。。。。。。。。。。。。。。。。'
ftpconf='/etc/vsftpd/vsftpd.conf'
if [ ! -f ${ftpconf}.ldward.bak ]; then cp ${ftpconf} ${ftpconf}.ldward.bak; fi
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
check_status
unset ftpconf

printf "安装虚拟用户管理工具db4。。。。。。。。"
yum install db4 db4-utils -y >>setup_log 2>&1
check_status

printf "创建用户文件。。。。。。。。。。。。。。"
ftptxt='/etc/vsftpd/vuser_passwd.txt'
echo 'ec_ftp' >${ftptxt}
echo 'ec_ftp@123' >>${ftptxt}
check_status

printf "生成虚拟用户认证文件。。。。。。。。。。。"
ftpdb='/etc/vsftpd/vuser_passwd.db'
db_load -T -t hash -f${ftptxt} ${ftpdb}
check_status

printf "认证完成，可以删除txt文件的密码行"
sed -i '/ec_ftp@123/d' ${ftptxt} >>setup_log 2>&1
unset ftptxt
unset ftpdb
check_status

printf "编辑FTP上传文件。。。。。。。。。。。。。"
if [ ! -f '/etc/pam.d/vsftpd.ldward.bak' ]; then cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.ldward.bak; fi
echo 'auth required pam_userdb.so db=/etc/vsftpd/vuser_passwd' >/etc/pam.d/vsftpd
echo 'account required pam_userdb.so db=/etc/vsftpd/vuser_passwd' >>/etc/pam.d/vsftpd
check_status

printf "创建虚拟用户配置文件夹。。。。。。。。。。。。。"
mkdir -p /etc/vsftpd/vuser_conf
check_status

printf "创建用户文件。。。。。。。。。。。。。。。。。。"
ftpuser='/etc/vsftpd/vuser_conf/ec_ftp'
echo 'local_root=/data/ftp' >${ftpuser}
echo 'write_enable=YES' >>${ftpuser}
echo 'anon_umask=022' >>${ftpuser}
echo 'anon_world_readable_only=NO' >>${ftpuser}
echo 'anon_upload_enable=YES' >>${ftpuser}
echo 'anon_mkdir_write_enable=YES' >>${ftpuser}
echo 'anon_other_write_enable=YES' >>${ftpuser}
check_status

printf "创建FTP根目录及权限。。。。。。。。。。。。。。。"
mkdir -p /data/ftp
chmod -R 774 /data/ftp
chown -R ftp:www /data/ftp
check_status

printf "开机自启动FTP服务。。。。。。。。。。。。。。。。"
chkconfig vsftpd on
check_status

printf "修改ecstore目录权限。。。。。。。。。。。。。。。"
chown -R www:www /data/httpd/ecstore
check_status

echo "mysql 用户名：ec_admin"
echo "mysql 密  码：ec_admin@123"
echo "FTP   用户名：ec_ftp"
echo "FTP   密  码：ec_ftp@123"

rm -f setup_log











