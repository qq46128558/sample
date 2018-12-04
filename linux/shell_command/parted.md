# parted

parted命令是由GNU组织开发的一款功能强大的磁盘分区和分区大小调整工具，与fdisk不同，它支持调整分区的大小。作为一种设计用于Linux的工具，它没有构建成处理与fdisk关联的多种分区类型，但是，它可以处理最常见的分区格式，包括：ext2、ext3、fat16、fat32、NTFS、ReiserFS、JFS、XFS、UFS、HFS以及Linux交换分区。

## 语法

parted(选项)(参数)

## 选项

	-h：显示帮助信息；
	-i：交互式模式；(默认)
	-s：脚本模式，不提示用户；
	-v：显示版本号。

## 参数

* 设备：指定要分区的硬盘所对应的设备文件；
* 命令：要执行的parted命令。

## parted交互命令
	
	print: 输出disk信息
	mklabel gpt: 设置磁盘标签类型为gpt(还有msdos)
	mkpart primary 0 磁盘大小: 建立主分区?
	quit: 退出
	
## 实例

	# 脚本模式,设置磁盘标签
	parted -s /dev/sdd mklabel msdos
	# 脚本模式,建立主分区
	parted -s /dev/sdd mkpart primary 0% 100%
	
