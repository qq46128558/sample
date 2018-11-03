
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