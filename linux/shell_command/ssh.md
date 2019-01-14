# ssh 远程linux

	# 远程连入
	ssh root@ip地址
	# 本地生成公钥
	ssh-keygen
	# 推送公钥到linux则下次不用输入密码
	ssh-copy-id root@ip地址

ssh命令是openssh套件中的客户端连接工具，可以给予ssh加密协议实现安全的远程登录服务器。

## 語法

ssh(选项)(参数)

## 選項

~~~
-1：强制使用ssh协议版本1；
-2：强制使用ssh协议版本2；
-4：强制使用IPv4地址；
-6：强制使用IPv6地址；
-A：开启认证代理连接转发功能；
-a：关闭认证代理连接转发功能；
-b：使用本机指定地址作为对应连接的源ip地址；
-C：请求压缩所有数据；
-F：指定ssh指令的配置文件；
-f：后台执行ssh指令；
-g：允许远程主机连接主机的转发端口；
-i：指定身份文件；
-l：指定连接远程服务器登录用户名；
-N：不执行远程指令；
-o：指定配置选项；
-p：指定远程服务器上的端口；
-q：静默模式；
-X：开启X11转发功能；
-x：关闭X11转发功能；
-y：开启信任X11转发功能。
~~~

~~~
 -R [bind_address:]port:host:hostport
     -R [bind_address:]port:local_socket
     -R remote_socket:host:hostport
     -R remote_socket:local_socket
             Specifies that connections to the given TCP port or Unix socket on the remote (server) host are to be forwarded to the given host and port, or Unix socket, on the local side.
             This works by allocating a socket to listen to either a TCP port or to a Unix socket on the remote side.  Whenever a connection is made to this port or Unix socket, the connection
             is forwarded over the secure channel, and a connection is made to either host port hostport, or local_socket, from the local machine.

             Port forwardings can also be specified in the configuration file.  Privileged ports can be forwarded only when logging in as root on the remote machine.  IPv6 addresses can be
             specified by enclosing the address in square brackets.

             By default, TCP listening sockets on the server will be bound to the loopback interface only.  This may be overridden by specifying a bind_address.  An empty bind_address, or the
             address ‘*’, indicates that the remote socket should listen on all interfaces.  Specifying a remote bind_address will only succeed if the server's GatewayPorts option is enabled
             (see sshd_config(5)).

             If the port argument is ‘0’, the listen port will be dynamically allocated on the server and reported to the client at run time.  When used together with -O forward the allocated
             port will be printed to the standard output.
~~~

## 参数

* 远程主机：指定要连接的远程ssh服务器；
* 指令：要在远程ssh服务器上执行的指令。

## 實例

### 未理解

	ssh -R 2344:10.210.1.65:22 root@60.190.239.50 -p 3402

