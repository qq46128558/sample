# sysctl命令

sysctl命令被用于在内核运行时动态地修改内核的运行参数，可用的内核参数在目录/proc/sys中。它包含一些TCP/ip堆栈和虚拟内存系统的高级选项， 这可以让有经验的管理员提高引人注目的系统性能。用sysctl可以读取设置超过五百个系统变量。

## 语法

sysctl(选项)(参数)

## 选项

	-n：打印值时不打印关键字；
	-e：忽略未知关键字错误；
	-N：仅打印名称；
	-w：当改变sysctl设置时使用此项；
	-p：从配置文件“/etc/sysctl.conf”加载内核参数设置；
	-a：打印当前所有可用的内核参数变量和值；
	-A：以表格方式打印当前所有可用的内核参数变量和值。

## 参数

变量=值：设置内核参数对应的变量值。

## 实例

查看所有可读变量：

	sysctl -a

读一个指定的变量，例如kern.maxproc：

	sysctl net.core.somaxconn

要设置一个指定的变量，直接用variable=value这样的语法：

	sysctl net.core.somaxconn=128

您可以使用sysctl修改系统变量，也可以通过编辑sysctl.conf文件来修改系统变量。sysctl.conf看起来很像rc.conf。它用variable=value的形式来设定值。指定的值在系统进入多用户模式之后被设定。并不是所有的变量都可以在这个模式下设定。

sysctl变量的设置通常是字符串、数字或者布尔型。（布尔型用 1 来表示'yes'，用 0 来表示'no'）。

## 配置sysctl

编辑此文件：/etc/sysctl.conf

### 如果希望屏蔽别人 ping 你的主机，则加入以下代码：

	# Disable ping requests
	net.ipv4.icmp_echo_ignore_all = 1

编辑完成后，请执行以下命令使变动立即生效：

	/sbin/sysctl -p
	/sbin/sysctl -w net.ipv4.route.flush=1