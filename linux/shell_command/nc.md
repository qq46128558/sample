# nc/netcat命令

nc命令是netcat命令的简称，都是用来设置路由器。

## 语法

	nc/netcat(选项)(参数)

## 选项

	-g<网关>：设置路由器跃程通信网关，最多设置8个；
	-G<指向器数目>：设置来源路由指向器，其数值为4的倍数；
	-h：在线帮助；
	-i<延迟秒数>：设置时间间隔，以便传送信息及扫描通信端口；
	-l：使用监听模式，监控传入的资料；
	-n：直接使用ip地址，而不通过域名服务器；
	-o<输出文件>：指定文件名称，把往来传输的数据以16进制字码倾倒成该文件保存；
	-p<通信端口>：设置本地主机使用的通信端口；
	-r：指定源端口和目的端口都进行随机的选择；
	-s<来源位址>：设置本地主机送出数据包的IP地址；
	-u：使用UDP传输协议；
	-v：显示指令执行过程；
	-w<超时秒数>：设置等待连线的时间；
	-z：使用0输入/输出模式，只在扫描通信端口时使用。
	-q seconds
             after EOF on stdin, wait the specified number of seconds and then quit. If seconds is negative, wait forever.

## 参数

* 主机：指定主机的IP地址或主机名称；
* 端口号：可以是单个整数或者是一个范围。

## 实例

### 扫描端口
	
	nc -zvw1 127.0.0.1 80
	#返回: Connection to 127.0.0.1 80 port [tcp/http] succeeded!
	nc -zvw1 127.0.0.1 3306
	#返回: Connection to 127.0.0.1 3306 port [tcp/mysql] succeeded!
	nc -zvw1 127.0.0.1 21
	#返回: nc: connect to 127.0.0.1 port 21 (tcp) failed: Connection refused

### 端口扫描(指定端口范围)
	
	nc -zvw1 127.0.0.1 80-89

### 聊天(内网)

nc还可以作为简单的字符下聊天工具使用，同样的，server2上需要启动监听：

	nc -lp 1234

server1上传输：

	nc 192.168.228.222 1234

这样，双方就可以相互交流了。使用Ctrl+D正常退出。

### 保存Web页面

	while true; do
	    nc -l -p 80 -q 1 < somepage.html;
	done

### 远程拷贝文件

从server1拷贝文件到server2上。需要先在server2上，用nc激活监听。server2上运行：

	nc -lp 1234 > install.log

server1上运行：
	
	nc -w 1 192.168.228.222 1234 < install.log

### 传输目录

从server1拷贝nginx-0.6.34目录内容到server2上。需要先在server2上，用nc激活监听，server2上运行：
	
	nc -l 1234 | tar xzvf -

server1上运行：(nginx-0.6.34是一个目录)

	tar czvf – nginx-0.6.34 | nc 192.168.228.222 1234

### 其他测试
	
	# 向localhost 22端口,发送test字符串
	echo "test"|nc localhost 22
	# 返回:
	SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
	Protocol mismatch.

	# 阿里nuwa角色测试(在NuwaZK#角色机器上执行)
	echo srvr|nc localhost 10240|grep Mode
	# 返回
	Mode: follower
