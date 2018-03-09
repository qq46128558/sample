##### 文件位置
    /usr/local/nginx/conf/nginx.conf
    或
    /etc/nginx/nginx.conf

##### 加载监听的配置文件
~~~
#http{}的include,一般在最后一行,表示要加载的监听配置文件
include vhosts/*.conf;

#蟹宝盒服务器示例
include /data/services/nginx_vhost/*.conf
~~~
