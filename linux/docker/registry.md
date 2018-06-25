## Docker私有仓库搭建

参考资料

[Docker私有仓库搭建](https://blog.csdn.net/wangtaoking1/article/details/44180901 "https://blog.csdn.net/wangtaoking1/article/details/44180901")
[push错误:server gave HTTP response to HTTPS client](https://www.cnblogs.com/hobinly/p/6110624.html "https://www.cnblogs.com/hobinly/p/6110624.html")
[docker 私有镜像仓库搭建](https://blog.csdn.net/wu_di_xiao_wei/article/details/54755475 "https://blog.csdn.net/wu_di_xiao_wei/article/details/54755475")


### 环境
- ubuntu 16.04,docker 1.13.1
- 47.106.160.48 开发机
- 47.106.126.78 私有仓库

### 搭建私有仓库(私有仓库机)
1. 下载registry镜像: docker pull registry
2. 启动registry容器: docker run -d -p 5000:5000 -v /opt/data/registry:/var/lib/registry registry
3. 测试地址: http://47.106.126.78:5000/v2/
4. 成功返回空白json说明搭建成功(阿里云安全组及linux防火墙需要开通5000端口)

### 上传镜像(开发机)
1. 假设已有本地镜像: ubuntu/yii2:1.0
2. 修改镜像tag: docker tag ubuntu/yii2:1.0 47.106.126.78:5000/ubuntu/yii2:1.0
3. 上传镜像到私有仓库: docker push 47.106.126.78:5000/ubuntu/yii2:1.0

### 上传错误1: connection refused
~~~
可能返回错误:connection refused
因为: 与docker registry交互默认使用的是https，然而此处搭建的私有仓库只提供http服务，所以当与私有仓库交互时就会报上面的错误
解决,在开发机中:
修改文件 /etc/init/docker.conf
增加: --insecure-registry 47.106.126.78:5000
修改完之后，重启Docker服务
~~~

~~~shell
script
        # modify these in /etc/default/$UPSTART_JOB (/etc/default/docker)
        DOCKERD=/usr/bin/dockerd
        DOCKER_OPTS=
        if [ -f /etc/default/$UPSTART_JOB ]; then
                . /etc/default/$UPSTART_JOB
        fi
        exec "$DOCKERD" $DOCKER_OPTS --raw-logs --insecure-registry 47.106.126.78:5000
end script
~~~

### 上传错误2: server gave HTTP response to HTTPS client
~~~
这个问题可能是由于客户端采用https，docker registry未采用https服务所致。一种处理方式是把客户对地址“47.106.126.78:5000”请求改为http。
解决,在开发机中:
增加文件 /etc/docker/daemon.json
{ "insecure-registries":["47.106.126.78:5000"] }
修改完之后，重启Docker服务
~~~

### 查询镜像
http://47.106.126.78:5000/v2/_catalog  
http://47.106.126.78:5000/v2/镜像名称/tags/list  

~~~
在Private Registry2中查看或检索Repository或images， 将不能用docker search,报错:
Error response from daemon: Unexpected status code 404 
~~~
