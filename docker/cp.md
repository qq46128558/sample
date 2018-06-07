Copy files/folders from a container's filesystem to the host path

**经测试不支持通配符**

**复制文件需指定文件全名**

#### 将主机/www/runoob目录拷贝到容器96f7f14e99ab的/www目录下
    docker cp /www/runoob 96f7f14e99ab:/www/

#### 将主机/www/runoob目录拷贝到容器96f7f14e99ab中，目录重命名为www
    docker cp /www/runoob 96f7f14e99ab:/www

#### 将容器96f7f14e99ab的/www目录拷贝到主机的/tmp目录中
    docker cp  96f7f14e99ab:/www /tmp/

    
