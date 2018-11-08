# nslookup

常用域名查询工具，就是查DNS信息用的命令

- 直接输入nslookup命令，不加任何参数，则直接进入交互模式，此时nslookup会连接到默认的域名服务器（即/etc/resolv.conf的第一个dns地址）
- 进入非交互模式，就直接输入nslookup 域名就可以了

## 语法

    nslookup(选项)(参数)
    选项：-sil：不显示任何警告信息。
    参数：域名：指定要查询域名。

## 实例

~~~html
[root@localhost ~]# nslookup www.linuxde.net
Server:         202.96.104.15
Address:        202.96.104.15#53

Non-authoritative answer:
www.linuxde.net canonical name = host.1.linuxde.net.
Name:   host.1.linuxde.net
Address: 100.42.212.8
~~~

