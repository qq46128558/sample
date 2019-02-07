
#### dns

##### 查看dns伺服器
	
	cat /etc/resolv.conf

#### cpu
	
	总核数 = 物理CPU个数 X 每颗物理CPU的核数 
	总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数

##### 查看物理CPU个数

	cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l

##### 查看每个物理CPU中core的个数(即核数)
	
	cat /proc/cpuinfo| grep "cpu cores"| uniq

##### 查看逻辑CPU的个数
	
	cat /proc/cpuinfo| grep "processor"| wc -l

##### 查看CPU信息（型号）
	
	cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
	
#### /proc信息
	
	# 查看进程的命令行
	cat /proc/`PID`/cmdline
	# cpu信息
	cat /proc/cpuinfo
	# 未知
	cat /proc/vmstat
	# 内存
	cat /proc/meminfo
	# 开机时间
	cat /proc/uptime
	
#### 查看用户
    cat /etc/passwd

#### 查看组
    cat /etc/group

#### Ubuntu apt更新源
    cat /etc/apt/sources.list
