# fdisk命令

fdisk命令用于观察硬盘实体使用情况，也可对硬盘分区。它采用传统的问答式界面，而非类似DOS fdisk的cfdisk互动式操作界面，因此在使用上较为不便，但功能却丝毫不打折扣。

## 语法

fdisk(选项)(参数)

## 选项

	-b<分区大小>：指定每个分区的大小；
	-l：列出指定的外围设备的分区表状况；
	-s<分区编号>：将指定的分区大小输出到标准输出上，单位为区块；
	-u：搭配"-l"参数列表，会用分区数目取代柱面数目，来表示每个分区的起始地址；
	-v：显示版本信息。

## 参数

设备文件：指定要进行分区或者显示分区的硬盘设备文件。

## 实例

### 分区,格式化,挂载

首先选择要进行操作的磁盘：
	
	fdisk /dev/sdb

输入m列出可以执行的命令：

	command (m for help): m
	Command action
	   a   toggle a bootable flag
	   b   edit bsd disklabel
	   c   toggle the dos compatibility flag
	   d   delete a partition
	   l   list known partition types
	   m   print this menu
	   n   add a new partition
	   o   create a new empty DOS partition table
	   p   print the partition table
	   q   quit without saving changes
	   s   create a new empty Sun disklabel
	   t   change a partition's system id
	   u   change display/entry units
	   v   verify the partition table
	   w   write table to disk and exit
	   x   extra functionality (experts only)

输入p列出磁盘目前的分区情况

输入d然后选择分区，删除现有分区

输入n建立新的磁盘分区，首先建立两个主磁盘分区：

	p    //建立主分区
		1  //分区号
		1 //分区起始位置
		100  //分区结束位置，单位为扇区

输入n  //再建立一个分区

	p    //建立主分区
		2  //分区号为2
		101 //分区起始位置
		+200M  //分区结束位置，单位为M

确认分区建立成功：p

再建立一个逻辑分区：n
	
	e  //选择扩展分区
	Partition number (1-4): 3
	First cylinder (126-391, default 126):126
	Last cylinder or +size or +sizeM or +sizeK (126-391, default 391):391

确认扩展分区建立成功：p

在扩展分区上建立两个逻辑分区：n

	l //选择逻辑分区
	First cylinder (126-391, default 126):126
	Last cylinder or +size or +sizeM or +sizeK (126-391, default 391): +400M 
	Command (m for help): n
	l //选择逻辑分区
	First cylinder (176-391, default 176):176
	Last cylinder or +size or +sizeM or +sizeK (176-391, default 391):391

确认逻辑分区建立成功：p

从上面的结果我们可以看到，在硬盘sdb我们建立了2个主分区（sdb1，sdb2），1个扩展分区（sdb3），2个逻辑分区（sdb5，sdb6）

注意：主分区和扩展分区的磁盘号位1-4，也就是说最多有4个主分区或者扩展分区，**逻辑分区开始的磁盘号为5** ，因此在这个实验中是没有sdb4的。

最后对分区操作进行保存：w

### 建立好分区之后我们还需要对分区进行格式化才能在系统中使用磁盘。

在sdb1上建立ext2分区：
	
	mkfs.ext2 /dev/sdb1

在sdb6上建立ext3分区：
	
	mkfs.ext3 /dev/sdb6

建立两个目录/oracle和/web，将新建好的两个分区挂载到系统：

	mkdir /oracle
	mkdir /web
	mount /dev/sdb1 /oracle
	mount /dev/sdb6 /web

如果需要每次开机自动挂载则需要修改/etc/fstab文件，加入两行配置：

	vim /etc/fstab

	/dev/sdb1               /oracle                 ext2    defaults        0 0
	/dev/sdb6               /web                    ext3    defaults        0 0