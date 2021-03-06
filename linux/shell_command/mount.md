# mount

mount命令用于加载文件系统到指定的加载点。此命令的最常用于挂载cdrom，使我们可以访问cdrom中的数据，因为你将光盘插入cdrom中，Linux并不会自动挂载，必须使用Linux mount命令来手动完成挂载。

## 语法

mount(选项)(参数)

## 选项

	-V：显示程序版本；
	-l：显示已加载的文件系统列表；
	-h：显示帮助信息并退出；
	-v：冗长模式，输出指令执行的详细信息；
	-n：don't write to /etc/mtab
	-r：将文件系统加载为只读模式；
	-a：加载文件“/etc/fstab”中描述的所有文件系统。
	-t, --types <list>      limit the set of filesystem types

## 参数

* 设备文件名：指定要加载的文件系统对应的设备名；
* 加载点：指定加载点目录。

## 实例
	# 挂载cdrom
	mount -t auto /dev/cdrom /mnt/cdrom   
		mount: block device /dev/cdrom is write-protected, mounting read-only     # 挂载成功

#### 将盘（如数据盘）挂载到指定目录
mount `diskname` `path`

**示例**

mount /dev/sdb1 /data

> 注意阿里云实例回滚后需要重新挂载


#### 取消挂载
    umount /dev/vdb1
    或
    umount /data

#### 阿里云数据盘扩容后处理
```shell
# 卸载主分区
umount /dev/vdb1
# 查看是否成功
df -h
# 删除原来分区并创建新分区
# 删除分区不会造成数据盘内数据的丢失
fdisk -l
fdisk /dev/vdb
# 输入d,n,p,1,enter,enter,wq后,开始分区
# 再次查看一下磁盘情况,如挂载了则卸载
df -h 
e2fsck -f /dev/vdb1 # 检查文件系统
resize2fs /dev/vdb1 # 变更文件系统大小
# 重新挂载
mount /dev/vdb1 /data
# 查看是否挂载成功
df -h 
```