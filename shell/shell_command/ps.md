#### 查看进程使用内存的情况
ps -eo 'rsz,cmd' |grep `"processname"`|grep -v "grep"

标题名称

- rsz,rss 内存
- cmd,command 进程命令
- user 用户
- uid 
- pid 进程id
- %cpu,pcpu cpu使用率
- %mem 内存使用率
- vsz 虚拟内存
- tty 连接终端
- stat 状态
- start,stime 启动时间?
- time 运行时间?
- args

#### 查看php-fpm进程数
ps aux|grep "php-fpm"|grep -v "grep"|wc -l

- -A, -e               all processes

- a                   all with tty, including other users
- u                   user-oriented format
- x                   processes without controlling ttys

#### 查看全部进程
    ps -e u
    ps axu
    