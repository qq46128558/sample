# service

service命令是Redhat Linux兼容的发行版中用来控制系统服务的实用工具，它以启动、停止、重新启动和关闭系统服务，还可以显示所有系统服务的当前状态。

## 语法

service(选项)(参数)

## 选项

	-h：显示帮助信息；
	--status-all：显示所服务的状态。

## 参数

	服务名：自动要控制的服务名，即/etc/init.d目录下的脚本文件名；
	控制命令：系统服务脚本支持的控制命令。

## 实例

	service network status
	service network restart
	service mysqld status
	service mysqld restart
	