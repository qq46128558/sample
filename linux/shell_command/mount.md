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