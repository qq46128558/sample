Push an image or a repository to a Docker registry server

只能将镜像发布到自己的空间下面

#### 上传到hub.docker.com
    #先登录
    docker login
    #再上传
    docker push `镜像名称`:TAG

#### 上传到私有仓
    #修改镜像TAG
    docker tag ubuntu/yii2:1.0 47.106.126.78:5000/ubuntu/yii2:1.0
    #再上传
    docker push 47.106.126.78:5000/ubuntu/yii2:1.0
