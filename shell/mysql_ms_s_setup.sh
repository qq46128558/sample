#!/bin/bash
echo -e "\033[33;1mMYSQL主从模式--从机Slave脚本"
echo -e "\033[0m(按Ctrl+C可中止,按Enter继续)"
#执行是否成功的函数
function CheckStatus(){
if [ $? == 0 ]
then
echo '[成功]'
else
echo '[失败]'
sudo cat ${log}
sudo rm -f ${log}
exit
fi 
}

log='setup.log'
read
printf '开始安装......'"\n"
printf '安装wget......'
sudo yum install wget -y >${log} 2>&1
CheckStatus
cd /etc/yum.repos.d/
printf '配置商派yum资源......'
if [ ! -f shopex-lnmp.repo ]; then
sudo wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo >${log} 2>&1
fi
CheckStatus
printf 'CentOS6.8自带Mysql5.1需删除......'
sudo yum list installed mysql|grep 5.1 >${log} 2>&1
if [ $? == 1 ]; then
echo '[无自带]'
else
sudo yum remove mysql -y >${log} 2>&1
CheckStatus
fi
printf '安装Mysql......'
sudo yum install mysql -y >${log} 2>&1
CheckStatus
printf '开机自启动MYSQL服务......'
sudo chkconfig mysqld on
CheckStatus
printf '删除空用户......'
mysql -uroot -e"delete from mysql.user where user='' and host='localhost'" >${log} 2>&1
mysql -uroot -e"delete from mysql.user where user='' and host='localhost.localdomain'" >${log} 2>&1
CheckStatus
printf '备份slave配置......'
mycnf="/usr/local/mysql/my.cnf"
if [ ! -f ${mycnf}.peter.bak ]; then sudo cp ${mycnf} ${mycnf}.peter.bak; fi
CheckStatus
printf 'slave配置......'
#sudo sed -i '/log-bin/d' ${mycnf}
#sudo sed -i '/\[mysqld\]/a log-bin=mysql-bin #启用二进制日志' ${mycnf}
sudo sed -i '/server_id/d' ${mycnf}
sudo sed -i '/\[mysqld\]/a server_id=2 #服务器唯一ID默认是1一般取IP最后一段' ${mycnf}
CheckStatus
echo -n -e '请输入master服务器IP:'
read masterip
echo -n -e '请输入File:'
read file
echo -n -e '请输入Position:'
read position
printf 'Change master......'
mysql -uroot -e"stop slave"
mysql -uroot -e"change master to master_host='${masterip}',master_user='ceslave',master_password='ceslave@123',master_log_file='${file}',master_log_pos=${position}" >${log} 2>&1
CheckStatus
printf '启用同步进程......'
mysql -uroot -e"start slave"
CheckStatus
if [ ! -f /etc/sysconfig/iptables.peter.bak ]; then sudo cp /etc/sysconfig/iptables /etc/sysconfig/iptables.peter.bak; fi
printf '开放3306端口......'
sudo cat /etc/sysconfig/iptables|grep "\-\-dport 3306"|grep "INPUT"|grep "ACCEPT" >${log} 2>&1
if [ $? == 1 ]; then
	sudo iptables -I INPUT -p tcp --dport 3306 -j ACCEPT >${log} 2>&1
	CheckStatus
else
	echo '[已开放]'
fi
printf '保存端口配置......'
#这个需要注意用户是否有权限
sudo /etc/rc.d/init.d/iptables save >${log} 2>&1
CheckStatus
printf '重启防火墙......'
sudo service iptables restart >${log} 2>&1
CheckStatus
printf '重启MYSQL服务......'
sudo service mysqld restart >${log} 2>&1
CheckStatus
echo -e "主从同步检查:(看到两项均为Yes,则同步正常运行中)"
mysql -uroot -e"show slave status\G"|grep -e "Slave_IO_Running:" -e "Slave_SQL_Running:"
echo -e "\033[32;1m安装配置结束\033[0m"
sudo rm -f ${log}

