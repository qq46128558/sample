# umount

umount命令用于卸载已经加载的文件系统。利用设备名或挂载点都能umount文件系统，不过最好还是通过挂载点卸载，以免使用绑定挂载（一个设备，多个挂载点）时产生混乱。

## 语法

umount(选项)(参数)

## 选项

	-a：卸除/etc/mtab中记录的所有文件系统；
	-h：显示帮助；
	-n：卸除时不要将信息存入/etc/mtab文件中；
	-r：若无法成功卸除，则尝试以只读的方式重新挂入文件系统；
	-t<文件系统类型>：仅卸除选项中所指定的文件系统；
	-v：执行时显示详细的信息；
	-V：显示版本信息。
	-l, --lazy              detach the filesystem now, clean up things later

## 参数
	
文件系统：指定要卸载的文件系统或者其对应的设备文件名。(最好还是通过挂载点卸载)

## 实例

下面两条命令分别通过设备名和挂载点卸载文件系统，同时输出详细信息：

### 通过设备名卸载
	
	umount -v /dev/sda1
		/dev/sda1 umounted

### 通过挂载点卸载

	umount -v /mnt/mymount/
		/tmp/diskboot.img umounted

#### 如果设备正忙，卸载即告失败。卸载失败的常见原因是，某个打开的shell当前目录为挂载点里的某个目录
	
	umount -v /mnt/mymount/
		umount: /mnt/mymount: device is busy

有时，导致设备忙的原因并不好找。碰到这种情况时，可以用lsof列出已打开文件，然后搜索列表查找待卸载的挂载点：

	lsof | grep mymount         # 查找mymount分区里打开的文件
		bash   9341  francois  cwd   DIR   8,1   1024    2 /mnt/mymount

从上面的输出可知，mymount分区无法卸载的原因在于，francois运行的PID为9341的bash进程。

#### 对付系统文件正忙的另一种方法是执行延迟卸载

	umount -vl /mnt/mymount/     # 执行延迟卸载

延迟卸载（lazy unmount）会立即卸载目录树里的文件系统，等到设备不再繁忙时才清理所有相关资源。卸载可移动存储介质还可以用eject命令。下面这条命令会卸载cd并弹出CD：

	eject /dev/cdrom      # 卸载并弹出CD 