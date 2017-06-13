#!/bin/bash
#记录执行时间
timestart=`date +%s`
#检查是否执行成功
function CheckStatus(){
#退格用于刷新显示秒数
echo -en '\b\b\b\b'
if [ $? == 0 ]
then
	timeend=`date +%s`;
	#3位格式化显示秒数
	printf  "%3us" `expr ${timeend} - ${timestart}`; 
	if [[ $1 == "end" ]]; then
		sleep 2;
		echo -en '\b\b\b\b'
		echo -e "[\033[32;1m成功\033[0m]";
		echo -e "\033[32m(请手动复制vim插件文件并修改端口为9010)\033[0m"
	fi
	return;
else 
echo -e "[\033[31;1m失败\033[0m]";
echo -e "\033[31;1m失败日志记录如下:\033[0m"
cat ${logfile} 
rm -f ${logfile} 
exit;
fi
}
#用到家目录,不能用引号括起来
logfile=~/sh.log;

echo -e "\033[33;1m注意: 当前安装需要切换到root用户进行.\033[0m"
#echo "(按任意键继续, 按Ctrl+C终止.)"
#read
printf '开始安装XDEBUG(预计时间8分钟)......    '
#安装wget
sudo yum install wget -y>>${logfile} 2>&1
CheckStatus
cd /etc/yum.repos.d/
#配置商派yum资源
if [ ! -f shopex-lnmp.repo ]; then
sudo wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo >>${logfile} 2>&1
fi
CheckStatus
#sudo cp ./shopex-lnmp.repo /etc/yum.repos.d/
#CheckStatus
#rm -f ./shopex-lnmp.repo
#安装PHP56
sudo yum install php-fpm56 -y >>${logfile} 2>&1
CheckStatus
#下载xdebug
cd ~>/dev/null
if [ ! -f xdebug-2.5.4.tgz ]; then 
wget http://www.xdebug.org/files/xdebug-2.5.4.tgz >>${logfile} 2>&1
CheckStatus
fi;
#解压xdebug
tar zxf xdebug-2.5.4.tgz >>${logfile} 2>&1
CheckStatus
#进入xdebug目录
cd xdebug-2.5.4
#安装php-devel & gcc
sudo yum install php-devel -y >>${logfile} 2>&1
CheckStatus
sudo yum install gcc -y >>${logfile} 2>&1
CheckStatus
#建立外挂模块
sudo /usr/local/php56/bin/phpize >>${logfile} 2>&1
CheckStatus
#配置
sudo ./configure --with-php-config=/usr/local/php56/bin/php-config >>${logfile} 2>&1
CheckStatus
#安装
sudo make >>${logfile} 2>&1
CheckStatus
sudo make install >>${logfile} 2>&1
CheckStatus
#配置php.ini
phpfile='/usr/local/php56/etc/php.ini'
if [ -s ${phpfile} ]; then 
	if [ ! -s ${phpfile}.peter.bak ]; then cp ${phpfile} ${phpfile}.peter.bak; fi;
	#开启php错误显示
	sed -i '/html_errors =/d' ${phpfile}
	sed -i '/display_errors =/d' ${phpfile}
	sed -i '$a\html_errors = On' ${phpfile}
	sed -i '$a\display_errors = On' ${phpfile}
	#先删除
	#此处需加转义,否则会有问题
	sed -i '/\[xdebug\]/d' ${phpfile}
	sed -i '/zend_extension=/d' ${phpfile}
	sed -i '/;基本调试配置/d' ${phpfile}
	sed -i '/xdebug.collect_params=on/d' ${phpfile}
	sed -i '/xdebug.collect_return=on/d' ${phpfile}
	sed -i '/;xdebug.auto_trace = on/d' ${phpfile}
	sed -i '/;xdebug.trace_output_dir=/d' ${phpfile}
	sed -i '/;xdebug.profiler_enable=on/d' ${phpfile}
	sed -i '/;xdebug.profiler_output_dir=/d' ${phpfile}
	sed -i '/;远程调试配置/d' ${phpfile}
	sed -i '/xdebug.remote_enable=on/d' ${phpfile}
	sed -i '/xdebug.remote_host=localhost/d' ${phpfile}
	sed -i '/xdebug.remote_port=9010/d' ${phpfile}
	sed -i '/xdebug.remote_autostart=on/d' ${phpfile}
	#再增加
	sed -i '$a\[xdebug]' ${phpfile}
	sed -i '$a\zend_extension="/usr/local/php56/lib/php/extensions/no-debug-non-zts-20131226/xdebug.so"' ${phpfile}
	sed -i '$a\;基本调试配置' ${phpfile}
	sed -i '$a\xdebug.collect_params=on' ${phpfile}
	sed -i '$a\xdebug.collect_return=on' ${phpfile}
	sed -i '$a\;xdebug.auto_trace = on' ${phpfile}
	sed -i '$a\;xdebug.trace_output_dir="/data/httpd/xdebug_trace"' ${phpfile}
	sed -i '$a\;xdebug.profiler_enable=on' ${phpfile}
	sed -i '$a\;xdebug.profiler_output_dir="/data/httpd/xdebug_profiler"' ${phpfile}
	sed -i '$a\;远程调试配置' ${phpfile}
	sed -i '$a\xdebug.remote_enable=on' ${phpfile}
	sed -i '$a\xdebug.remote_host=localhost' ${phpfile}
	sed -i '$a\xdebug.remote_port=9010' ${phpfile}
	sed -i '$a\xdebug.remote_autostart=on' ${phpfile}
fi;
CheckStatus
#重启php服务
service php-fpm56 restart >>${logfile} 2>&1
CheckStatus end
rm -f ${logfile}
