# tsar

Tsar是淘宝的系统信息采集和监测工具，主要用来收集服务器的系统信息（如cpu，io，mem，tcp等）以及应用数据（如squid haproxy nginx等），这些信息可以保存在本地磁盘或者发送到Nagios中

## 安装

	wget -O tsar.zip https://github.com/alibaba/tsar/archive/master.zip --no-check-certificate
	unzip tsar.zip
	cd tsar-master
	make
	make install

## 常用
	--live/-l      running print live mode, which module will print
	--interval/-i  specify intervals numbers, in minutes if with --live, it is in seconds
	tsar -li1