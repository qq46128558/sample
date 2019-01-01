# pssh

ssh命令是一个python编写可以在多台服务器上执行命令的工具，同时支持拷贝文件，是同类工具中很出色的，类似pdsh，个人认为相对pdsh更为简便，使用必须在各个服务器上配置好密钥认证访问。

## 选项

	--version：查看版本
	--help：查看帮助，即此信息
	-h：主机文件列表，内容格式”[user@]host[:port]”
	-H：主机字符串，内容格式”[user@]host[:port]”
	-：登录使用的用户名
	-p：并发的线程数【可选】
	-o：输出的文件目录【可选】
	-e：错误输入文件【可选】
	-t：TIMEOUT 超时时间设置，0无限制【可选】
	-O：SSH的选项
	-v：详细模式
	-A：手动输入密码模式
	-x：额外的命令行参数使用空白符号，引号，反斜线处理
	-X：额外的命令行参数，单个参数模式，同-x
	-i：每个服务器内部处理信息输出
	-P：打印出服务器返回信息

## 注意
	a 使用前提
	中心主机连接远程主机可以通过ssh密钥无密码连接
	b 命令格式
	pssh 总是通过清单 文件指定主机
	其中的每行采用 [user] host[:port] 形式。
	c 创建servers.txt文件
	文件的内容为远程主机的ip,和用于连接ssh的用户名和端口
	# vim /home/server.txt
	192.168.0.177
	root@183.62.138.82:22031
	d pssh用法-在多个主机上并行地运行命令
	# pssh -P -h /home/server.txt hostname

~~~
# 建立ssh密钥登陆，脚本批量创建(验证通过)
[root@57135test pssh-1.4.3]# ssh-keygen -t rsa
创建rsa.sh脚本 test.txt中写入要管理的IP
[root@192 sh]# more rsa.sh 
#!/bin/sh
#by authors chy 2016
for i in $(cat test.txt)
do
        ssh-copy-id -i /root/.ssh/id_rsa.pub $i
        echo $i"设置密码登录成功"
done
注：可以将IP写在test.txt文件中
~~~

## 实例

### 获取每台服务器的uptime：

	# pssh -h ip.txt -i uptime
	[1] 11:15:03 [SUCCESS] Mar.mars.he
	11:15:11 up 4 days, 16:25,  1 user,  load average: 0.00, 0.00, 0.00
	[2] 11:15:03 [SUCCESS] Jan.mars.he
	11:15:12 up 3 days, 23:26,  0 users,  load average: 0.00, 0.00, 0.00
	[3] 11:15:03 [SUCCESS] Feb.mars.he
	11:15:12 up 4 days, 16:26,  2 users,  load average: 0.08, 0.02, 0.01

### 查看每台服务器上mysql复制IO/SQL线程运行状态信息：

	# pssh -h IP.txt -i "/usr/local/mysql/bin/mysql -e 'show slave status \G'"|grep Running:
             Slave_IO_Running: yes
            Slave_SQL_Running: Yes
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes

### 保存每台服务器运行的结果：

	# pssh -h IP.txt -i -o /tmp/pssh/ uptime
	[1] 11:19:47 [SUCCESS] Feb.mars.he
	11:19:55 up 4 days, 16:31,  2 users,  load average: 0.02, 0.03, 0.00
	[2] 11:19:47 [SUCCESS] Jan.mars.he
	11:19:56 up 3 days, 23:30,  0 users,  load average: 0.01, 0.00, 0.00
	[3] 11:19:47 [SUCCESS] Mar.mars.he
	11:19:56 up 4 days, 16:30,  1 user,  load average: 0.00, 0.00, 0.00

我们来看一下/tmp/pssh/下的文件及其内容

	# ll /tmp/pssh/
	总用量 12
	-rw-r--r--. 1 root root 70 12月  1 11:19 Feb.mars.he
	-rw-r--r--. 1 root root 70 12月  1 11:19 Jan.mars.he
	-rw-r--r--. 1 root root 69 12月  1 11:19 Mar.mars.he
	 
	# cat /tmp/pssh/*
	11:19:55 up 4 days, 16:31,  2 users,  load average: 0.02, 0.03, 0.00
	11:19:56 up 3 days, 23:30,  0 users,  load average: 0.01, 0.00, 0.00
	11:19:56 up 4 days, 16:30,  1 user,  load average: 0.00, 0.00, 0.00