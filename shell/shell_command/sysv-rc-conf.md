#### 设置指定服务在指定运行等级的开机启动状态
	sysv-rc-conf [--level `levels`] `service` <on|off>
	如
	sysv-rc-conf --level 2 nginx on

#### 查看服务开机状态
	sysv-rc-conf --list [`service`]
	如
	sysv-rc-conf --list
	sysv-rc-conf --list nginx

#### 界面操作
	sysv-rc-conf


~~~
在Debian Linux中，下列路径对应不同的运行级别。当系统启动时，通过其中的脚本文件来启动相应的服务。 
/etc/rc0.d Run level 0 停机
/etc/rc1.d Run level 1 单用户
/etc/rc2.d Run level 2 多用户，无网络连接
/etc/rc3.d Run level 3 多用户，启动网络连接
/etc/rc4.d Run level 4 用户自定义
/etc/rc5.d Run level 5 多用户带图形界面
/etc/rc6.d Run level 6 重启

ls /etc/rc2.d/
README  S20mysql  S20nginx  S20php-fpm  S20postfix  S20rsync  S20screen-cleanup  S70dns-clean  S70pppd-dns  S99grub-common  S99ondemand  S99rc.local
其中的S20,S70,S99等， 20，70，99应该是优先级
~~~

Linux 系统主要启动步骤

~~~
1. 读取 MBR 的信息,启动 Boot Manager
        Windows 使用 NTLDR 作为 Boot Manager,如果您的系统中安装多个
        版本的 Windows,您就需要在 NTLDR 中选择您要进入的系统。
        Linux 通常使用功能强大,配置灵活的 GRUB 作为 Boot Manager。
2. 加载系统内核,启动 init 进程
        init 进程是 Linux 的根进程,所有的系统进程都是它的子进程。
3. init 进程读取 /etc/inittab 文件中的信息,并进入预设的运行级别,
   按顺序运行该运行级别对应文件夹下的脚本。脚本通常以 start 参数启
   动,并指向一个系统中的程序。
        通常情况下, /etc/rcS.d/ 目录下的启动脚本首先被执行,然后是
        /etc/rcN.d/ 目录。例如您设定的运行级别为 3,那么它对应的启动
        目录为 /etc/rc3.d/ 。
4. 根据 /etc/rcS.d/ 文件夹中对应的脚本启动 Xwindow 服务器 xorg
        Xwindow 为 Linux 下的图形用户界面系统。
5. 启动登录管理器,等待用户登录
        Ubuntu 系统默认使用 GDM 作为登录管理器,您在登录管理器界面中
        输入用户名和密码后,便可以登录系统。(您可以在 /etc/rc3.d/
        文件夹中找到一个名为 S13gdm 的链接)
~~~

