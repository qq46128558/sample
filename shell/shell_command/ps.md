####查看进程使用内存的情况
ps -eo 'rsz,cmd' |grep `"processname"`|grep -v "grep"

标题名称

- rsz,rss 内存
- cmd,command 进程命令
- user 用户
- pid 进程id
- %cpu cpu使用率
- %mem 内存使用率
- vsz 虚拟内存
- tty 连接终端
- stat 状态
- start 启动时间?
- time 运行时间?
