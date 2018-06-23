#### （终端内）创建一个带名字的作业
    screen -S `sessionName`
    #自动开一个窗口
    #不建议在作业内开启新作业

#### （作业内）常用快捷键
    #C-a(表示Ctrl+a，screen内的所有快捷键都是先按这个)
    
    #给窗口命名
    C-a A
    #创建一个新的运行shell的窗口并切换到该窗口
    C-a c
    #显示所有键绑定信息
    C-a ?
    #切换到第 0..9 个 window
    C-a 0..9
    #在两个最近使用的 window 间切换
    C-a C-a
    #分割一个竖屏
    C-a |
    #切换屏幕（然后C-a 0..9）
    C-a tab
    #分割一个横屏
    C-a S
    #关掉当前分屏
    C-a X

    #离线，暂时离开当前session，将目前的 screen session (可能含有多个 windows) 丢到后台执行，并会回到还没进 screen 时的状态，此时在 screen session 里，每个 window 内运行的 process (无论是前台/后台)都在继续执行，即使 logout 也不影响
    C-a d

    #锁住当前的 window，需用用户密码解锁
    C-a x
    #把当前session放到后台执行，用 shell 的 fg 命令则可回去
    C-a z
    #kill window，强行关闭当前的 window
    C-a k

    #进入 copy mode，在 copy mode 下可以回滚、搜索、复制就像用使用 vi 一样
    C-a [
        #Space 第一次按为标记区起点，第二次按为终点 
        #Esc 结束 copy mode
    #paste，把刚刚在 copy mode 选定的内容贴上
    C-a ]


#### 列出当前所有的session
    screen -ls

#### 恢复离线的screen作业
    screen -r `sessionName`

#### 将指定的screen作业离线
    screen -d `sessionName`

#### 先试图恢复离线的作业。若找不到离线的作业，即建立新的screen作业
    screen -R

#### 指定建立新视窗时，所要执行的shell
    screen -s

#### 检查目前所有的screen作业，并删除已经无法使用的screen作业
    screen -wipe


## 高级应用

#### 恢复之前离线的screen作业
    screen -x [sessionName]
    #假设你在和朋友在不同地点以相同用户登录一台机器，然后你创建一个screen会话
    #这个命令会将你朋友的终端Attach到你的Screen会话上，并且你的终端不会被Detach。这样你就可以和朋友共享同一个会话了，如果你们当前又处于同一个窗口，那就相当于坐在同一个显示器前面，你的操作会同步演示给你朋友，你朋友的操作也会同步演示给你。当然，如果你们切换到这个会话的不同窗口中去，那还是可以分别进行不同的操作的。

#### 发送命令到screen会话
    screen -S sandy -X screen ping www.baidu.com
    #这个命令在一个叫做sandy的screen会话中创建一个新窗口，并在其中运行ping命令


