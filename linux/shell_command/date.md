#### 将当前日期时间显示成时间戳
	#seconds since 1970-01-01 00:00:00 UTC
    date +%s

#### 显示成年月日时分秒指定格式
	#year-month-day of month time; same as %H:%M:%S
    #由于中间有空格,所以加引号
    date +"%Y-%m-%d %T"

#### 将指定日期转成时间戳
    date -d"2018-04-04 17:00" +%s

#### 日期按标准格式显示
    #%Y-%m-%d %H:%M:%S
    date +"%F %T"

#### 将指定时间戳显示成标准日期
    date -d@1523462400 +"%F %T"