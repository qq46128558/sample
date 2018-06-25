Run a command in a new container

在新容器中运行命令同时启动容器

#### 退出但不关闭容器
    按 ctrl + p + q

#### 如何让容器长期运行
    #因为容器的生命周期依赖于启动时执行的命令，只要该命令不结束，容器也就不会退出
    docker run -d ubuntu:15.10 /bin/bash -c "while true;do sleep 1;done"
    #容器常见的用途是运行后台服务

    #以下运行后,可通过attach进入
    docker run -dit -p 80:80 centos
    #经验证,关闭后,可使用start启动

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

#### 启动容器,进行目录挂载
    #-v:Bind mount a volume
    #-v $PWD/conf:/etc/nginx/conf.d 将主机当前目录下的conf挂载到容器的/etc/nginx/conf.d
    #-v $PWD/logs:/var/log/nginx 将主机当前目录下的logs挂载到容器的/var/log/nginx
    #-v $PWD/www:/usr/share/nginx/html 将主机当前目录下的www挂载到容器的/usr/share/nginx/html
    docker run -p 8001:80 --name mynginx  -v $PWD/conf:/etc/nginx/conf.d -v $PWD/logs:/var/log/nginx -v $PWD/www:/usr/share/nginx/html -d nginx
    #主机的挂载目录不存在则会自动创建,里面的文件需要手动添加或复制
    #建议:首先需要创建将要映射到容器中的目录以及.cnf文件，然后再创建容器

#### 启动容器,初始化 root 用户的密码
    #-e:Set environment variables
    #-e MYSQL_ROOT_PASSWORD=123456：初始化 root 用户的密码
    docker run -p 3306:3306 --name mymysql -v $PWD/conf:/etc/mysql/conf.d -v $PWD/logs:/logs -v $PWD/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.6

#### 启动容器,指定工作目录
    #-w:Working directory inside the container
    #-w /usr/src/myapp:指定容器的/usr/src/myapp目录为工作目录
    docker run  -v $PWD/myapp:/usr/src/myapp  -w /usr/src/myapp python:3.5 python helloworld.py