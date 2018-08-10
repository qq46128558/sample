
#### 开启慢查询日志
	SET GLOBAL SLOW_QUERY_LOG='on';
	<!-- 查询超过1秒就记录:验证失败 --> 
	SET GLOBAL LONG_QUERY_TIME=1;

#### 设置环境变量的值
    #log_timestamps 日志时间参数
    SET GLOBAL log_timestamps = SYSTEM;