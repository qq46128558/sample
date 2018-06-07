Return low-level information on a container or image

#### 查看Docker的底层信息
    docker inspect `镜像id`
    docker inspect f1b
    
#### 查看容器IP
    docker inspect `容器id`|grep "IPAddress"
    