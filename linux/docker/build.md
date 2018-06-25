Build an image from a Dockerfile

从零开始来创建一个新的镜像,我们需要创建一个 Dockerfile 文件

```
runoob@runoob:~$ cat Dockerfile 
FROM    centos:6.7
MAINTAINER      Fisher "fisher@sudops.com"

RUN     /bin/echo 'root:123456' |chpasswd
RUN     useradd runoob
RUN     /bin/echo 'runoob:123456' |chpasswd
RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
EXPOSE  22
EXPOSE  80
CMD     /usr/sbin/sshd -D
```

#### 构建一个镜像
    # -t:指定要创建的目标镜像名
    # .:Dockerfile 文件所在目录，可以指定Dockerfile 的绝对路径
    docker build -t peter/centos:6.7 .
