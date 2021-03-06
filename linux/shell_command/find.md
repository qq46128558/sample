
#### 循环删除查找出来指定位置的文件

~~~shell
# 删除前先手工备份
logs=$(find /var/nginx/www/html/test -name "*.log")
for log in $logs
do
rm -rf $log
done
~~~

    # 一行脚本
    for log in $(find /var/nginx/www/html/test -name "*.log");do rm -rf $log;done
    find /var/nginx/www/html/test/ -name "*.log" -exec rm -rf {} \;
    find /var/nginx/www/html/test/ -name "*.log"|xargs -i rm -rf {}

#### 查找当前目录及子目录下查找所有以.bat或.lock结尾的文件
    find . \( -name "*.bat" -o -name "*.lock" \)
    # 或
    find . -name "*.bat" -o -name "*.lock"

#### 查找文件并执行删除
    find /alidata/www/logs/java/ebs/sys -mtime +7 -type f \( -name "task.log.*" -o -name "dubbo.log.*" -o -name "task-removeSnashot.log.*" -o -name "service.log.*" -o -name "grandcanal_heartbeat.log.*" -o -name "grandcancal_thread.log.*" \) -exec rm -f {} \;

#### 查找并显示文件
    find . -name "testweb.php" -ls

#### 查找filename指定文件
    find . -name `filename`

#### 按文件属主查找
    find . -user `username`

#### 按文件属组查找
    find . -group `groupname`

#### 查找1分钟以内修改过的文件
    find . -mmin -1

#### 查找15天以前修改过的文件
    find . -mtime +15

#### 按文件类型查找
- 查找块设备
	~~~
	find . -type b
	~~~
- 查找目录
	~~~
	find . -type d
	~~~
- 查找字符设备
    ~~~
    find . -type c
    ~~~
- 查找管道
    ~~~
    find . -type p
    ~~~
- 查找符号链接
    ~~~
    find . -type l
    ~~~
- 查找普通文件
    ~~~
    find . -type f
    ~~~

#### 配合正则查找大写字母开头的普通文件
    find . -name "[A-Z]*"

#### 查找大小为0的文件或空目录
    find . -empty

#### 查找小于10k的文件
    find . -size -10k
    大于10k的改用+号

#### 查找权限为775(rwx rwx r-x)的文件
	find . -perm 775

#### 查找属主为peter的文件并执行chown命令
	find . -user peter -exec sudo chown www.www {} \;

#### 查找属主不是www的文件
	find . ! -user www

#### 查找名为controller或member的文件
	find . -name "controller" -or -name "member"

#### 查找普通文件内容包含getSql的文件
	find . -type f |xargs grep "getSql"

#### 其他记录
    # 同-xdev: 将范围局限在先行的文件系统中
    find . -mount



