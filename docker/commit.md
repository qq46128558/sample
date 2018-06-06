Create a new image from a container's changes

#### 保存对容器的修改
    docker commit `容器id` `镜像名称`
    docker commit 689 learn/ping

#### 更新镜像
    # 从已经创建的容器中更新镜像，并且提交这个镜像
    # -m:提交描述信息
    # -a:指定镜像作者
    docker commit -m="has update" -a="peter" `容器id` peter/ubuntu:v2