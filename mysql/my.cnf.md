## mysql配置文件记录

#### [mysqld]
    #mysql 5.7日志时间与本地时间不一致的问题,该参数主要是控制 error log、genera log
    #UTC/SYSTEM
    log_timestamps = SYSTEM