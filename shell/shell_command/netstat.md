## netstat
Linux中网络系统的状态信息

#### 查看9000端口是否有在监听
    netstat -anp |grep 9000
    #-a display all sockets (default: connected) 显示所有sockets
    #-n don't resolve names 以端口号显示(如http=>80,ssh=>22)
    #-p display PID/Program name for sockets 显示进程ID/程序名称