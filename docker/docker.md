## 什么是Docker?
Docker是一个开源的引擎，可以轻松的为任何应用创建一个轻量级的、可移植的、自给自足的容器。开发者在笔记本上编译测试通过的容器可以批量地在生产环境中部署，包括VMs（虚拟机）、bare metal、OpenStack 集群和其他的基础应用平台。 

- Docker 使用客户端-服务器 (C/S) 架构模式，使用远程API来管理和创建Docker容器。
- Docker 容器通过 Docker 镜像来创建。
- 容器与镜像的关系类似于面向对象编程中的对象与类。
- 因为容器的生命周期依赖于启动时执行的命令，只要该命令不结束，容器也就不会退出
- 容器常见的用途是运行后台服务

### 安装
    # centos
    yum -y install docker-io
    # ubuntu
    apt-get install docker-io

### 启动服务
service docker start


### 容器
- docker容器可以理解为在沙盒中运行的进程。
- 这个沙盒包含了该进程运行所必须的资源，包括文件系统、系统类库、shell 环境等等。
- 但这个沙盒默认是不会运行任何程序的。
- 你需要在沙盒中运行一个进程来启动某一个容器。
- 这个进程是该容器的唯一进程，所以当该进程结束的时候，容器也会完全的停止。

### 帮助
    docker
    docker `命令` --help
    docker ps --help


### 常用命令
    docker ps -a
    docker logs upbeat_khorana
    docker start upbeat_khorana
    docker stop upbeat_khorana
    docker exec upbeat_khorana ls -lh
    docker pull centos
    docker push XXX
    docker cp /root/yii-advanced-app-2.0.15.tgz upbeat_khorana:/home/www/
