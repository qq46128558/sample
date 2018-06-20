# BBC集群部署指南

*本示例以四台虚拟机为示例进行说明, 存在共用机器的情况, 正式环境应该分开使用.*

> 系统环境:centos6.5~6.9
> 
> 本示例没有安装ftp服务器,有需要可自行尝试

|机器说明|IP地址|备注|阿里云产品|
|-|-|-|-|
|主mysql服务器|192.168.239.130|master机,用于mysql的写功能|云数据库RDS版|
|从mysql服务器|192.168.239.131|slave机,用于mysql的读功能,自动同步master的数据|-|
|redis服务器|192.168.239.132||云数据库Redis版|
|缓存服务器|192.168.239.132||云数据库Memcache版|
|静态资源服务器|192.168.239.132|资源图片||
|web服务器1(主)|192.168.239.130|单向同步,主web向从web推送代码|云服务器ECS|
|web服务器2(从)|192.168.239.131|单向同步|云服务器ECS|
|负载均衡服务器|192.168.239.133||负载均衡|




## 安装mysql服务器(同步,主从模式)
*阿里云可直接购买云数据库RDS版,带读写分离及灾难备份,不用自己配置*  
**(这一部份供了解学习用)**

### 安装步骤

> 无特别说明,则master与slave机器均需安装  


1. 初始化yum源
	~~~
	yum install wget -y
	cd /etc/yum.repos.d/
	wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo
	~~~

2. 安装mysql  
	~~~
	#如有mysql5.1存在则先删除
	yum remove mysql -y
	yum install mysql -y
	#备份一下配置文件
	cp /usr/local/mysql/my.cnf /usr/local/mysql/my.cnf.peter.bak
	~~~

3. 配置mysql的cnf文件  
	vim /usr/local/mysql/my.cnf  
	**master机**  
	~~~
	[mysqld]
	#启用二进制日志
	log-bin=mysql-bin 
	#服务器唯一ID默认是1一般取IP最后一段
	server_id=1 
	~~~

	**slave机**
	~~~
	[mysqld]
	#服务器唯一ID默认是1一般取IP最后一段
	server_id=2 
	~~~

3. 重启mysqld服务
	~~~
	service mysqld restart
	~~~

4. 开启3306端口
	~~~
	#插入一条规则,使开放3306端口
	iptables -I INPUT -p tcp --dport 3306 -j ACCEPT
	#保存防火墙规则
	/etc/rc.d/init.d/iptables save
	service iptables restart
	~~~

5. 登录MySQL删除空用户

	*初始安装后root为空密码, 注意修改*
	~~~
	mysql -h localhost -u root
	delete from mysql.user where user='' and host='localhost';
	delete from mysql.user where user='' and host='localhost.localdomain';
	~~~
	*修改root密码的其中一种方法(123456就是你的密码)*  
	*UPDATE mysql.user SET password=PASSWORD('123456') WHERE user='root';*  
	*重启服务后生效*  
	*service mysqld restart*

6. 给slave服务器授权

	**master机**
	~~~
	#确认已登入mysql,然后执行授权
	#授权ip 131机器通过ceslave用户进行同步(replication)
	grant replication slave on *.* to 'ceslave'@'192.168.239.131' identified by 'ceslave@123';
	#ceslave是用户名,ceslave@123是密码
	~~~

	查询并记录file与position值
	~~~
	#查询主数据库状态
	show master status;
	~~~

	**slave机**
	~~~
	#确认已登入mysql
	#停止同步进程
	stop slave;
	#执行同步配置语句,用到上面记录的file与position值
	change master to master_host='192.168.239.130',master_user='ceslave',master_password='ceslave@123',master_log_file='mysql-bin.xxxxxx',master_log_pos=xxx;
	#启动同步进程
	start slave;
	#主从同步检查
	show slave status\G;
	#如果以下两个均为Yes, 则表示同步正常运行
	#Slave_IO_Running: Yes
	#Slave_SQL_Running: Yes
	~~~

7. 重启mysqld服务
		
		service mysqld restart
		#设置mysqld服务开机自启动
		chkconfig mysqld on


8. 测试同步效果

	在master创建数据库, 数据表, 插入记录
	~~~
	create database mytest;
	create table mytest.user(id int, name varchar(50));
	insert into mytest.user (id,name) values (1, 'jason');
	~~~
	
	在slave中能查询到新创建的
	~~~
	select * from mytest.user;
	~~~

9. 测试同步效果成功后,创建bbc数据库并授权

	**master机**
	~~~
	create database bbc;
	grant all privileges on bbc.* to 'ec_admin'@'%' identified by 'ec_admin@123';
	~~~


## 安装redis服务器
*如果是阿里云产品 云数据库Redis版 直接配置后连接即可*

### 安装步骤

1. 初始化yum源

	*初始化yum源，将shopex-lnmp源加入到系统中，如果已经参照单机部署初始化过yum源了则省略此步骤*

	~~~
	yum install wget -y
	cd /etc/yum.repos.d/
	wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo
	yum install epel-release -y
	~~~

2. 安装

	~~~
	yum install redis -y
	~~~

3. 配置

	redis开启远程访问

	~~~
	vim /etc/redis.conf
	#注释 #bind 127.0.0.1, 表示支持外部连接
	#bind 127.0.0.1
	# 关闭保护模式,这样bbc安装时,检测redis服务器才能连入, 否则报: 远程redis连接错误check
	protected-mode no 

	#设置密码(按需设置)
	# requirepass foobared
	requirepass 123456
	~~~

3. 开放6379端口

	~~~
	iptables -I INPUT -p tcp --dport 6379 -j ACCEPT
	/etc/rc.d/init.d/iptables save
	service iptables restart
	~~~

4. 启动

	~~~
	/etc/init.d/redis start
	#开机自启动
	chkconfig redis on
	~~~

5. 测试是否安装正确

	~~~
	#-a 123456 为连接密码
	redis-cli -h 192.168.239.132 -a 123456
	#返回PONG(否则有问题)
	ping
	quit
	~~~

tcp://xxxx:6379

**如果redis服务设置了密码, 则安装bbc连接时注意填写**

**redis://xxxx:6379?password=123456**


## 安装缓存服务器
*如果是阿里云产品 云数据库Memcache版 直接配置后连接即可*

### 安装步骤

1. 初始化yum源

	*初始化yum源，将shopex-lnmp源加入到系统中，如果已经参照单机部署初始化过yum源了则省略此步骤*

	~~~
	yum install wget -y
	cd /etc/yum.repos.d/
	wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo
	yum install epel-release -y
	~~~

2. 安装

	~~~
	yum install memcached -y
	~~~

3. 配置

	~~~
	#配置文件位置
	vim /etc/sysconfig/memcached
	#可以修改内存大小等配置
	#修改OPTIONS监听内网IP
	OPTIONS="-l 192.168.239.132,::1"
	
	#或注释OPTIONS本地监听,这样才能连入
	#OPTIONS="-l 127.0.0.1,::1"
	~~~

3. 开放11211端口

	~~~
	iptables -I INPUT -p tcp --dport 11211 -j ACCEPT
	/etc/rc.d/init.d/iptables save
	service iptables restart
	~~~

4. 启动

	~~~
	/etc/init.d/memcached start
	chkconfig memcached on
	~~~

5. 测试缓存服务器是否能正确连接

	~~~
	#使用telnet(windows带)
	telnet 192.168.239.132 11211
	#连不通则重启一下memcached服务
	service memcached restart
	#能正常连入后,用stats命令查看各种状态
	stats
	quit
	~~~

## 安装静态资源服务器

### 安装步骤

1. 初始化yum源

	*初始化yum源，将shopex-lnmp源加入到系统中，如果已经参照单机部署初始化过yum源了则省略此步骤*

	~~~
	yum install wget -y
	cd /etc/yum.repos.d/
	wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo
	yum install epel-release -y
	~~~

2. nfs安装
	
	~~~
	yum install nfs-utils -y
	~~~

3. 安装rpcbind

	~~~
	#适用centos 5
	yum install portmap -y
	#适用centos 6
	yum install rpcbind -y
	~~~

4. 启动nfs服务

	*启动顺序一定要先启动rpcbind，后在启动nfs*
	
	~~~
	/etc/init.d/rpcbind start
	chkconfig rpcbind on
	/etc/init.d/nfs start
	chkconfig nfs on
	~~~

5. 安装nginx

	~~~
	yum install ngx_openresty -y
	service nginx restart
	chkconfig nginx on
	~~~

6. 修改exports配置

	~~~
	vim /etc/exports

	#加入如下参数
	#可以使用*不限制挂载机器
	#/data/httpd/themes *(rw,sync,all_squash,anonuid=502,anongid=502)
	/data/httpd/themes 192.168.239.130/24(rw,sync,all_squash,anonuid=502,anongid=502)
	/data/httpd/images 192.168.239.130/24(rw,sync,all_squash,anonuid=502,anongid=502)
	/data/httpd/app 192.168.239.130/24(rw,sync,all_squash,anonuid=502,anongid=502)

	#192.168.239.130为主web服务器
	#502为用户id, 用命令cat /etc/passwd查询本服务器www的用户id/组id,如495,则改为495
	
	#rw 该主机对该共享目录有读写权限
	#sync 资料同步写入到内存与硬盘中
	#all_squash 客户机上的任何用户访问该共享目录时都映射成匿名用户
	#anonuid 将客户机上的用户映射成指定的本地用户ID的用户
	#anongid 将客户机上的用户映射成属于指定的本地用户组ID
	~~~

7. 修改好后执行命令

	~~~
	mkdir /data/httpd/themes -p
	mkdir /data/httpd/images 
	mkdir /data/httpd/app
	exportfs -rv
	~~~

8. 查看是否成功
	
	*192.168.239.132为静态资源服务器*

	~~~
	showmount -e 192.168.239.132
	~~~

9. 开启端口

	~~~
	vim /etc/sysconfig/iptables
	#放在上面一点的位置
	-A INPUT -p tcp -m state --state NEW  --dport 111 -j ACCEPT
	-A INPUT -p udp -m state --state NEW  --dport 111 -j ACCEPT
	-A INPUT -p tcp -m state --state NEW  --dport 2049 -j ACCEPT
	-A INPUT -p udp -m state --state NEW  --dport 4046 -j ACCEPT
	-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
	#重启服务
	service iptables restart
	~~~

>后面还有几个步骤需在主Web服务器中安装配置


## 主Web服务器安装

### 安装步骤

1. bbc基本环境安装
	
	~~~
	setenforce 0
	vim /etc/selinux/config
	#改为:SELINUX=disabled
	
	#初始化yum源
	yum install wget -y
	cd /etc/yum.repos.d/
	wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo
	yum install epel-release -y
	
	#基本安装
	yum install ngx_openresty php-fpm56 Zend56 php-memcached56 -y
	
	#上传安装包
	cd 安装包所在目录
	mkdir -p /data/httpd
	tar -zxf 安装包名称 -C /data/httpd
	vim /usr/local/php56/etc/php.d/Zend.ini
	#修改zend_loader.license_path='/data/httpd/b2b2c/config/developer.zl'
	vim /usr/local/nginx/conf/vhosts/default.conf
	#修改网站目录为/data/httpd/b2b2c/public
	
	#定时任务配置
	crontab -uwww -e
	* * * * * /data/httpd/b2b2c/script/queue/queue.sh /usr/local/php56/bin/php > /dev/null
	* * * * * /usr/local/php56/bin/php /data/httpd/b2b2c/script/crontab/crontab.php >/dev/null
	
	#修改bbc目录权限
	chown -R www:www /data/httpd/
	#配置本地映射环境
	vim /etc/hosts
	127.0.0.1   %CONNECTIONS.DEFAULT.HOST%
	
	#开放80端口
	vim /etc/sysconfig/iptables
	-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT 
	service iptables restart

	service php-fpm56 restart
	chkconfig php-fpm56 on
	service nginx restart
	chkconfig nginx on
	~~~

2. 进入bbc页面安装

	~~~
	#打开安装页面
	http://192.168.239.130/index.php
	#数据库主机
	192.168.239.130
	#数据库用户名
	ec_admin
	#数据库密码
	ec_admin@123
	#数据库名
	bbc
	#redis配置
	#tcp://192.168.239.132:6379?password=123456
	#无密码
	tcp://192.168.239.132:6379
	#发现redis服务器设置密码后,能连接,但是进入下一步时报错:NOAUTH Authentication required.
	#解决：
	redis://192.168.239.132:6379?password=123456
	

	#redis数据库
	database=0
	~~~
	

3. 接着静态资源服务器未完成的步骤

	~~~
	#nfs安装
	yum install nfs-utils -y
	#安装rpcbind
	#适用centos 5
	yum install portmap -y 
	#适用centos 6
	yum install rpcbind -y 
	#启动NFS服务，启动顺序一定要先启动rpcbind，后在启动nfs
	/etc/init.d/rpcbind start
	chkconfig rpcbind on
	/etc/init.d/nfs start
	chkconfig nfs on
	
	#将web服务器中已有的资源复制到静态资源服务器(132)
	#(按提示输入yes及132的登录密码)
	scp -r /data/httpd/b2b2c/public/themes/ root@192.168.239.132:/data/httpd/
	scp -r /data/httpd/b2b2c/public/images/ root@192.168.239.132:/data/httpd/
	scp -r /data/httpd/b2b2c/public/app/ root@192.168.239.132:/data/httpd/
	
	#修改静态资源服务器中挂载目录的owner(因为上面复制后是root用户)
	chown -R www.www /data/httpd/

	#将web服务器中静态资源挂载到静态资源服务器(132)
	mount 192.168.239.132:/data/httpd/themes /data/httpd/b2b2c/public/themes
	mount 192.168.239.132:/data/httpd/images /data/httpd/b2b2c/public/images
	mount 192.168.239.132:/data/httpd/app /data/httpd/b2b2c/public/app
	(ps:发现主web服务器重启后, 需要重新挂载?待验证)
	
	#挂载失败:
	mount.nfs: Connection timed out
	一般是静态资源服务器防火墙端口没开启.

	#检查挂载是否正常
	df -h
	cd /data/httpd/b2b2c/public/themes/
	echo 'abc'>1
	#切换到静态资源服务器
	cd /data/httpd/themes/
	ls
	~~~

4. 主web配置

	> 注意:　连接storage服务器的地址需要用外网IP, 阿里云有内网与外网IP

	~~~
	#复制配置文件到production 
	cp /data/httpd/b2b2c/config/storager.php /data/httpd/b2b2c/config/production/
	#修改配置文件
	vim /data/httpd/b2b2c/config/production/storager.php
	#修改资源映像站地址
	'host_mirrors' => array('http://192.168.239.132',),
	#修改图片映象站地址
	'host_mirrors_img' => ['img0'=>'http://192.168.239.132',],

	#修改memcached配置
	vim config/cache.php
	session的resource设为memcached
	memcached的server连接到memcached服务器:
	'servers'=>[['host' => '192.168.239.132', 'port' => 11211, 'weight' => 100],],

	#配置mysql读写分离
	vim config/production/database.php
	'default' => array(
            'master' => array('user' => 'ec_admin', 'password' => 'ec_admin@123', 'host' => '192.168.239.130', 'dbname' => 'bbc','charset'   => 'utf8'),
            'slaves' => array(
                array('user' => 'ec_admin', 'password'=>'ec_admin@123', 'host' => '192.168.239.131', 'dbname' => 'bbc','charset'=> 'utf8'),
             ),
            'driver'    => 'mysqli',
        ),
	~~~

5. 检查主web网站是否能正常打开

	~~~
	http://192.168.239.130/index.php
	~~~

## 主从Web服务器(代码)同步
*商派文档的配置是采取单向同步，采取 主web机 向 从web机 推送代码，如要双向同步，需自行查阅资料*

### 安装步骤

1. 从web机器安装

	~~~
	setenforce 0
	vim /etc/selinux/config
	#改为:SELINUX=disabled
	
	#初始化yum源
	yum install wget -y
	cd /etc/yum.repos.d/
	wget http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo
	yum install epel-release -y

	#基本安装
	yum install ngx_openresty php-fpm56 Zend56 php-memcached56 -y

	#无需安装bbc

	#开放80端口
	vim /etc/sysconfig/iptables
	-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT 
	service iptables restart
	
	#安装 rsync
	yum install rsync -y

	#编辑配置文件
	vim /etc/rsyncd.conf
	~~~

	(无则创建) , 编辑内容如下:  
	`uid = root`  
	`gid = root`  
	use chroot = 0  
	`port = 873`  
	`hosts allow = *`  
	max connections = 0  
	timeout = 300  
	pid file = /var/run/rsyncd.pid  
	lock file = /var/run/rsyncd.lock  
	log file = /var/log/rsyncd.log  
	log format = %t %a %m %f %b  
	transfer logging = yes  
	syslog facility = local3  
	[slave_web]  
	`path = /data/httpd/b2b2c`  
	`comment = slave_web`  
	ignore errors  
	read only = no  
	list = no  
	`auth users = rsync`  
	`secrets file = /etc/rsyncd.passwd`  

	~~~
	#编辑密码文件
	vim /etc/rsyncd.passwd
	#编辑内容:
	rsync:123456
	#开放873端口
	vim /etc/sysconfig/iptables
	#增加:
	-A INPUT -p tcp -m state --state NEW -m tcp --dport 873 -j ACCEPT
	#重启服务:
	service iptables restart
	#修改密码文件权限为600
	chmod 600 /etc/rsyncd.passwd
	
	#以守护进程方式启动rsync服务
	/usr/bin/rsync --daemon --config=/etc/rsyncd.conf
	#添加开机自启动
	echo "/usr/bin/rsync --daemon --config=/etc/rsyncd.conf">>/etc/rc.local
	
	#手动创建b2b2c目录(否则测试同步时报chdir failed错)
	mkdir /data/httpd/b2b2c
	
	#修改从web机器的nginx网站目录
	vim /usr/local/nginx/conf/vhosts/default.conf
		root  /data/httpd/b2b2c/public/
	#修改从web机品license指向
	vim /usr/local/php56/etc/php.d/Zend.ini
		zend_loader.license_path='/data/httpd/b2b2c/config/developer.zl'
	#重启服务
	service php-fpm56 restart
	chkconfig php-fpm56 on
	service nginx restart
	chkconfig nginx on
	~~~

2. 主web机器安装
	
	rsync [^1]
	
	> 主web服务器 推送代码到 从web服务器 的时候主web服务器的rsync.passwd只需要配置密码就可以，不用配置用户名，从服务器最好配置同一个用户名和密码)


	~~~
	#安装 rsync
	yum install rsync -y
	#编辑密码文件
	vim /etc/rsyncd.passwd
	#编辑内容:
	123456
	#修改密码文件权限为600
	chmod 600 /etc/rsyncd.passwd
	
	#验证代码是否能够同步, 在主web服务器上执行下面命令 
	rsync -vzrtopg --delete --progress --password-file=/etc/rsyncd.passwd /data/httpd/b2b2c/ rsync@192.168.239.131::slave_web
	
	#使用文件监控工具inotify-tools 监控并触发单向同步
	#安装 inotify-tools
	yum install gcc -y
	wget http://github.com/downloads/rvoicilas/inotify-tools/inotify-tools-3.14.tar.gz
	tar xzf inotify-tools-3.14.tar.gz
	cd inotify-tools-3.14
	./configure --prefix=/usr && make && su -c 'make install'

	#编辑rsync.sh单向同步监控脚本
	vim /root/rsync.sh
	~~~

	rsync.sh

	> 注意: 删除没有单向同步成功, 可能是因为src不对, 注意后面有 /data/httpd/b2b2c/
	
	~~~
	#!/bin/bash
	src=/data/httpd/b2b2c/
	des=slave_web
	user=rsync
	#多个ip就用空格间断
	host="192.168.239.131"
	/usr/bin/inotifywait -mrq --exclude=public/images --exclude=public/themes --exclude=data/logs --timefmt '%d/%m/%y %H:%M' --format '%T %w%f' -e modify,delete,create,attrib $src | while read file
	do
	    for hostip in $host
	    do
	        rsync -vzrtopg --delete --progress --exclude=public/images --exclude=public/themes --exclude=data/logs ${src} ${user}@${hostip}::${des}  --password-file=/etc/rsyncd.passwd
	        echo "${file} was rsynced" >> /tmp/rsync.log 2>&1
	    done
	done
	~~~

	~~~
	#无需同步的参考(未确定)
	--exclude=vendor/bin/doctrine-dbal --exclude=data/cache --exclude=data/logs
	~~~

	~~~
	#给脚本增加执行权限
	chmod +x /root/rsync.sh
	#运行rsync.sh同步监控脚本
	nohup sh /root/rsync.sh &
	
	#运行后, 可能提示:
	nohup: ignoring input and appending output to `nohup.out'
	按enter即可, 此时已在进程中运行.
	~~~

	~~~
	报错: /usr/bin/inotifywait: error while loading shared libraries: libinotifytools.so.0: cannot open shared object file: No such file or directory
	原因: 该文件在/usr/lib, 而inotify查找的是/usr/lib64
	解决: 建个链接文件:
	     ln -s /usr/lib/libinotifytools.so.0.4.1 /usr/lib64/libinotifytools.so.0
	~~~

	~~~
	配置守护进程
	#建立守护进程运行rsync.sh脚本
	echo "nohup sh /root/rsync.sh &" >> /etc/rc.local
	~~~

	[^1]:rsync 简要说明:  
	rsync [OPTION]... SRC [USER@]HOST::DEST  
	-v, --verbose 详细模式输出。  
	-z, --compress 对备份的文件在传输时进行压缩处理。  
	-r, --recursive 对子目录以递归模式处理。  
	-t, --times 保持文件时间信息。  
	-o, --owner 保持文件属主信息。  
	-p, --perms 保持文件权限。  
	-g, --group 保持文件属组信息。  
	--delete 删除那些DST中SRC没有的文件。  
	--progress 显示备份过程。  
	--password-file=FILE 从FILE中得到密码。  

	

## 负载均衡服务器的安装
*如果是阿里云产品 负载均衡 直接配置即可用(此处了解即可)*

### 安装步骤

1. 安装 haproxy
	~~~
	yum install haproxy -y
	~~~

2. 配置
	~~~
	vim /etc/haproxy/haproxy.cfg
	~~~
	
	以下为配置内容，根据实际情况调整
	~~~
	global
	  log 127.0.0.1 local3
	  chroot /var/lib/haproxy
	  pidfile /var/run/haproxy.pid
	  maxconn 30000
	  user haproxy
	  group haproxy
	  daemon
	
	  stats socket /var/lib/haproxy/stats
	
	defaults
	  option http-keep-alive
	  mode http
	  log global
	  option httplog
	  option dontlognull
	  option accept-invalid-http-request
	  option http-server-close
	  option redispatch
	  retries 3
	  timeout http-request 60s
	  timeout queue 1m
	  timeout http-keep-alive 60s
	  timeout connect 60s
	  timeout client 1m
	  timeout server 1m
	  timeout check 2000
	  maxconn 30000
	  stats enable
	  stats uri /shopexadminss
	  stats auth admin:r4b7x3m7vVN3
	frontend main *:80
	  default_backend app
	
	backend static
	  balance roundrobin
	  server static 192.168.239.130:80 check
	
	
	backend app
	  balance roundrobin
	  mode http
	  cookie SERVERID insert nocache indirect
	  server web1 192.168.239.130:80 check inter 1500 rise 1 fall 3 weight 1
	  server web2 192.168.239.131:80 check inter 1500 rise 1 fall 3 weight 1
	~~~

3. 启动 haproxy

	~~~
	/etc/init.d/haproxy start
	chkconfig haproxy on

	如报错: Starting haproxy: [ALERT] 264/082446 (4203) : Starting frontend main: cannot bind socket [0.0.0.0:80]
	原因: 80端口被占用.(因为之前在负截均衡服务器装了nginx)
	解决: 更换端口.
	~~~

3. 开放80端口

	~~~
	vim /etc/sysconfig/iptables
	-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT 
	service iptables restart
	~~~

4. 访问负载均衡服务器，检验效果
	
	~~~
	http://192.168.239.133/index.php
	
	#如无法打开, 则自己写一个test.php测试
	#主web的public内写一个test.php
	#检查是否同步到从web
	#分别打开主从web的test.php,检查是否正常
	~~~


## 其他遇到过的问题

~~~
1 cmd update报错: 
ALTER TABLE base_rpcpoll ADD id VARCHAR(32) DEFAULT NULL, ADD process_id VARC  
  HAR(32) DEFAULT NULL, ADD type VARCHAR(8) DEFAULT NULL, ADD calltime INT UNSIGNED DEFAULT NULL, ADD network INT UNSI  
  GNED DEFAULT NULL, ADD method VARCHAR(100) DEFAULT NULL, ADD params LONGTEXT DEFAULT NULL COMMENT '请求和响应的参数(  
  序列化)', ADD callback VARCHAR(200) DEFAULT NULL, ADD callback_params LONGTEXT DEFAULT NULL, ADD result LONGTEXT DEF  
  AULT NULL, ADD fail_times VARCHAR(10) DEFAULT '1' NOT NULL, ADD status VARCHAR(6) DEFAULT 'failed' NOT NULL':         
  Duplicate column name 'id'  

解决:
base_rpcpoll并没有客开过, 均是标准产品的内容.
原因是启用了主从模式的mysql (/data/httpd/config/production/database.php) 连接报此错
先改回原来的连接, 只连接主mysql, 之后再cmd update, 成功后再改回主从mysql连接.

2 bbc后台, 无法正常安装应用(未解决)
目前是通过cmd命令, 用install 应用名称进行安装.

3 通过负载均衡进入运营后台, 安装app有时会报500错
安装app以及更新代码应从主web地址进入, 因为是web机是单向同步

~~~
