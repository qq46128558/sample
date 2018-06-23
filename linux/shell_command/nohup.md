#### nohup和&的区别
nohup是永久执行(终端连线断开仍执行)
&是指在后台运行(终端连线断开后不继续执行)

#### 使命令一直在后台执行
    nohup `command` &

#### nohup.out
    nohup自动将输出追加到当前目录的nohup.out
    如无权限,则追加到 用户家目录/nohup.out

#### 示例
    nohup tail -f nohup.out
    #退出终端再进入后, 用ps aux|grep "tail" 仍然看到该进程

nohup在运行命令和脚本中常用到的