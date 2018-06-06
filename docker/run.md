Run a command in a new container

在新容器中运行命令

#### 在docker容器中运行hello world
    docker run `指定要运行的镜像` `在启动的容器里执行的命令`
    docker run learn/tutorial echo "hello world"
    docker run ubuntu:15.10 /bin/echo "Hello world"

#### 在容器中安装新的程序
    # 如果不指定-y参数的话,docker环境中是无法响应这种交互的
    docker run learn/tutorial apt-get install -y ping
    # 然后可用commit保存成镜像
    docker commit 689 learn/ping
    #运行(新)镜像中的ping命令
    docker run learn/ping ping www.baidu.com

#### 运行交互式的容器
    # -t:在新容器内指定一个伪终端或终端
    # -i:允许你对容器内的标准输入 (STDIN) 进行交互
    docker run -it ubuntu:15.10 /bin/bash

#### 启动容器（后台模式）
    # -d:Run container in background and print container ID
    docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
    
#### 启动容器,将容器内部使用的网络端口映射到我们使用的主机上
    # -P:Publish all exposed ports to random ports
    docker run -d -P training/webapp python app.py

#### 启动容器,容器内部的 5000 端口映射到我们本地主机的 5000 端口上
    # -p:Publish a container's port(s) to the host
    docker run -d -p 5000:5000 training/webapp python app.py

#### 启动容器,可以指定容器绑定的网络地址
    # 这样我们就可以通过访问127.0.0.1:5001来访问容器的5000端口
    docker run -d -p 127.0.0.1:5001:5000 training/webapp python app.py

#### 启动容器,绑定 UDP 端口
    docker run -d -p 127.0.0.1:5001:5000/udp training/webapp python app.py

#### 启动容器,命名容器
    docker run -d -P --name runoob training/webapp python app.py
    