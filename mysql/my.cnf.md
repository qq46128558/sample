## mysql配置文件记录

#### 查找配置文件(linux命令)
	whereis my.cnf  
	locate my.cnf

- /etc/mysql/my.cnf
- /etc/my.cnf

#### [mysqld]
    #mysql 5.7日志时间与本地时间不一致的问题,该参数主要是控制 error log、genera log
    #UTC/SYSTEM
    log_timestamps = SYSTEM

	#绑定地址(默认127.0.0.1只能本机访问)
	bind-address = 0.0.0.0

> 更改完配置一般需要重启服务: /etc/init.d/mysql restart | service mysql restart