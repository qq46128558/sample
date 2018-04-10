#### 将当前日期时间显示成时间戳
	#seconds since 1970-01-01 00:00:00 UTC
    date +%s

#### 显示成年月日时分秒指定格式
	#year-month-day of month time; same as %H:%M:%S
    #由于中间有空格,所以加引号
    date +"%Y-%m-%d %T"