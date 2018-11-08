# dmesg

dmesg命令被用于检查和控制内核的环形缓冲区。kernel会将开机信息存储在ring buffer中。您若是开机时来不及查看信息，可利用dmesg来查看。开机信息保存在/var/log/dmesg文件里。

## 语法

dmesg(选项)

## 选项

* -c：显示信息后，清除ring buffer中的内容；
* -s<缓冲区大小>：预设置为8196，刚好等于ring buffer的大小；
* -n：设置记录信息的层级。

## 实例
	
	dmesg | head
	dmesg | tail

### 输出IO中比较高的进程

	# 启动block_dump: echo 1 >/proc/sys/vm/block_dump
	# 关闭block_dump: echo 0 >/proc/sys/vm/block_dump
	# vda1是磁盘类型
	echo 1 >/proc/sys/vm/block_dump;sleep 60;dmesg|awk '/vda1/ {print$2}'|sort|uniq -c|sort -rn;echo 0 >/proc/sys/vm/block_dump

~~~html
# 写入IO行如:
[341605.816850] jbd2/vda1-8(297): WRITE block 843200 on vda1 (8 sectors)
# print$2
jbd2/vda1-8(297):
# uniq -c 在每列旁边显示该行重复出现的次数

   2134 jbd2/vda1-8(297):
   1089 kworker/u2:0(6):
    207 systemd-journal(373):
    130 kworker/u2:2(2044):
     28 bash(1820):
      3 AliYunDun(1349):
      2 bash(2069):
      1 tail(2069):
~~~
