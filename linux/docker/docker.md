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
    apt-get install docker.io

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

### docker技术应用场景
    - 节省项目环境部署时间
        - 单项目打包：打包到镜像>>push>>pull>>启动容器
        - 整套项目打包：DockerCompose
        - 新开源技术试用：pull官方镜像
    - 环境一致性
    - 微服务：多个独立服务组成业务系统，一个容器一个服务，容器之间相互隔离
    - 弹性伸缩：集群模式下存在
        - 可以很快速启动上百个容器来提供更多并发和资源利用率

### docker特点
    - 开箱即用
    - 快速部署
    - 可移植性强
    - 环境隔离


