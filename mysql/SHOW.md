
#### 显示创建表的信息
	
	SHOW CREATE TABLE `tablename`\G
	
#### 显示连接数
	
	SHOW STATUS LIKE 'thread%';
	

#### 慢查询相关参数
	<!-- 开启慢查询日志，可以让MySQL记录下查询超过指定时间的语句，通过定位分析性能的瓶颈，才能更好的优化数据库系统的性能。 -->
	<!-- 慢查询开启状态 -->
	SHOW VARIABLES LIKE 'slow_query_log';
	<!-- 慢查询日志存放的位置 -->
	SHOW VARIABLES LIKE 'slow_query_log_file';
	<!-- 查询超过多少秒才记录 -->
	SHOW VARIABLES LIKE 'long_query_time';
	
#### 显示表的信息
	SHOW TABLE STATUS LIKE 'yii2_menu';
	
#### 显示所有databases
    SHOW DATABASES;

#### 显示所有tables
    SHOW TABLES;

#### 显示指定变量的信息
    #log_timestamps 日志时间参数
    SHOW GLOBAL VARIABLES LIKE 'log_timestamps'