Push an image or a repository to a Docker registry server

只能将镜像发布到自己的空间下面

[如何使用Docker部署一个web项目并打包成镜像文件](https://blog.csdn.net/JXYZH11/article/details/79112655)


#### 上传到hub.docker.com
    #先登录
    docker login
    #改TAG
    docker tag image username/repository:tag
    #再上传
    docker push username/repository:tag

#### 上传到私有仓
    #修改镜像TAG
    docker tag ubuntu/yii2:1.0 47.106.126.78:5000/ubuntu/yii2:1.0
    #再上传
    docker push 47.106.126.78:5000/ubuntu/yii2:1.0
