##### 文件位置
    /usr/local/nginx/conf/nginx.conf
    或
    /etc/nginx/nginx.conf

##### 指定用户
    user www-data;

##### 加载监听的配置文件
~~~
#http{}的include,一般在最后一行,表示要加载的监听配置文件
include vhosts/*.conf;

#蟹宝盒服务器示例
include /data/services/nginx_vhost/*.conf

#其他示例
include /etc/nginx/conf.d/*.conf;
~~~

##### 日志文件位置
~~~
#http{}内
#访问日志
access_log /var/log/nginx/access.log;
#错误日志
error_log /var/log/nginx/error.log;
~~~

##### server{}配置 http+yii2
~~~
server {
    # 监听80端口
    listen 80;
    # 网站目录指向
    root /data/www/xbh/yii2/web;
    # 默认加载文件(如果使用php则加上index.php)
    index index.php index.html index.htm index.nginx-debian.html;
    # 指定域名
    server_name _;
    # 日志文件位置(需要有写权限,用户及组:www-data.adm)
    access_log /data/www/access.log;
    error_log /data/www/error.log;

    # 增加一个一级path:test(指向/data/www/test目录,支持php解释)
    location /test {
                root /data/www/;
                index index.php index.html;
                location ~ \.php$ {
                        include fastcgi_params;
                        fastcgi_index index.php;
                        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                        fastcgi_pass   127.0.0.1:9000;
                        #fastcgi_pass unix:/var/run/php5-fpm.sock;
                        try_files $uri =404;
                }
    }

    # yii2路由定位配置
    location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                # try_files $uri $uri/ =404;
                try_files $uri $uri/ /index.php?$args;
    }

    # 使nginx支持php(需要php-fpm监听9000端口)
    # ~ 表示正则匹配：区分大小写匹配
    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    location ~ \.php$ {
            include fastcgi_params;
            fastcgi_index index.php;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_pass   127.0.0.1:9000;
            #fastcgi_pass unix:/var/run/php5-fpm.sock;
            try_files $uri =404;
    }

}
~~~

#### server{} 配置 echo-nginx模块
~~~
server {
    location /hello{
        #基本使用
        #指定默认响应类型为无格式
        #发现不指定的话,变成直接下载文件
        default_type text/plain;
        echo "<h1>hello world</h1>";
    }
}
~~~

#### echo-nginx 关键字
Key|Remark
-|-
echo_reset_timer|重置计数器
echo_flush|
echo_sleep|暂停(秒)
echo_before_body|在body前显示
echo_after_body|在body后显示
echo_location_async|
echo_subrequest_async |
echo_duplicate|复制:echo_duplicate 10 A
echo_read_request_body|
echo_request_body|
$echo_timer_elapsed|运行时间(秒)
$echo_client_request_headers|请求头信息
$echo_request_method|
$echo_request_body|
set|set $res miss

#### server{} nginx变量

url sample: xxx

Variable|Value
-|-

