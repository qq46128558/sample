
#### 查看提示符格式

	echo $PS1
	# ${debian_chroot:+($debian_chroot)}\u@\h:\w\$
	# root@iZwz9eqxyns1r4q5wr19ijZ:/var/nginx/www/html/test#

#### 修改提示符颜色
	
	# [\e[F;Bm]要改变颜色的部分[\e[0m] F前景30~37 B背景40~47
	# 颜色顺序 black red green yellow blue magenta cyan white。
	export PS1='${debian_chroot:+($debian_chroot)}\u@\h:\[\e[33;40m\]\w\[\e[0m\]\$'
	# root@iZwz9eqxyns1r4q5wr19ijZ:/var/nginx/www/html/test# (路径带颜色)
	\d 代表日期
	\H 完整的主机名称
	\h 仅取主机的第一个名字
	\t 显示时间为24小时格式(带秒)
	\T 示时间为12小时格式
	\A 显示时间为24小时格式
	\u 当前用户的账号名称
	\v BASH的版本信息
	\w 完整的工作目录名称
	\W 列出最后一个目录
	\# 下达的第几个命令
	\$ 提示字符，如果是root时，提示符为：# ，普通用户则为：$

#### 释放被cache的内存 /proc/sys/vm/drop_caches
	
	# 释放前先sync,防止数据丢失
	sync
	# 释放
	echo 3 >/proc/sys/vm/drop_caches
	# to free pagecache
	# echo 1 >/proc/sys/vm/drop_caches
	# to free dentries and inodes
	# echo 2 >/proc/sys/vm/drop_caches
	# to free pagecache,dentries and inodes
	# echo 3 >/proc/sys/vm/drop_caches

#### 输出IO中比较高的进程 /proc/sys/vm/block_dump
	
	# 启动block_dump: echo 1 >/proc/sys/vm/block_dump
	# 关闭block_dump: echo 0 >/proc/sys/vm/block_dump
	# vda1是磁盘类型
	echo 1 >/proc/sys/vm/block_dump;sleep 60;dmesg|awk '/vda1/ {print$2}'|sort|uniq -c|sort -rn;echo 0 >/proc/sys/vm/block_dump

#### 给指定终端发消息
	echo "some message from peter">/dev/pts/2

#### 查看当前终端
	tty

#### 查看登入者
	w
	who