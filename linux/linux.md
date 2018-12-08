
## linux
- linux应用程序表现为2种特殊类型的文件：可执行文件和脚本文件
- linux使用:分隔PATH变量里的条目
- linux使用/分隔文件名里的目录名

### 隐藏linux进程的方法
    - 创建进程的时候，把pid设为0
    - 直接修改ps和top的代码
    - hook libc里的readdir和opendir等函数
    
### 常用目录说明
~~~
/bin: 二进制文件目录，用于存放启动系统时用到的程序
/usr/bin：用户二进制文件目录，用于存放用户使用的标准程序
/usr/local/bin：本地二进制文件目录，用于存放软件安装的程序
/sbin：系统管理程序
/usr/sbin：用户系统管理程序
/opt: 可选的操作系统组件和第三方应用程序
~~~

### ssh远程一段时间无操作后自动断开的解决

1. 修改/etc/ssh/sshd_config
2. 增加或修改 ClientAliveInterval 30 (表示每30秒发送一次心跳信号)
3. 增加或修改 ClientAliveCountMax 1 (表示客户端无回应次数大于该值时自动断开连接)
4. 重启ssh服务: /etc/init.d/ssh restart
5. 退出ssh远程后再次连入

### 七种文件类型

* - 普通文件
* d 目录文件
* c 字符设备文件,如:/dev/zero
* b 块设备文件,如:/dev/vda1
* s 套接口文件,如:/var/lib/mysql/mysql.sock
* p 管道文件 
* l 符号链接文件,有点像win下的快捷快式