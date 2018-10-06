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

#### server{} 配置nginx status
~~~
location /nginx_status
        {
            stub_status on;
            access_log   off;
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

#### server{} [nginx变量](https://blog.csdn.net/u012654882/article/details/70832850 "https://blog.csdn.net/u012654882/article/details/70832850")

~~~
location /echo{
    default_type text/plain;
}
~~~

Variable|Value|manual
-|-|-
url|http://192.168.239.136/echo?a=1&b=2&c=3#ABC|
$arg_name|- |(请求中的的参数名)
$args|a=1&b=2&c=3 |(请求中的参数值)
$binary_remote_addr|- |(客户端地址的二进制形式)
$bytes_sent|- |(传输给客户端的字节数)
$connection|- |(TCP连接的序列号)
$connection_requests|1  |(TCP连接当前的请求数量)
$content_length| - |(Content-Length请求头字段)
$content_type|- |(Content-Type请求头字段)
$cookie_name|- |(cookie名称)
$document_root|/home/wwwroot/yii2/web |(当前请求的文档根目录或别名)
$document_uri|/echo |(同 $uri)
`$host`|192.168.239.136 |(HTTP请求行的主机名>HOST请求头字段>符合请求的服务器名)
$hostname|ubuntu |(主机名)
$http_[name]|匹配任意请求头字段,|如:$http_accept_language=>zh-CN,zh;q=0.9
$https|- |(SSL安全模式，值为“on”，否则为空字符串)
$is_args|? |(请求中有参数，值为“?”，否则为空字符串)
$limit_rate|0 |(用于设置响应的速度限制)
$msec|1523428427.438 |(Unix时间戳)
$nginx_version|1.4.6 |(nginx版本)
$pid|2702 |(工作进程的PID)
$pipe|. |(请求来自管道通信，值为“p”，否则为“.”)
$proxy_protocol_addr|X |(代理访问服务器的客户端地址)
$query_string|a=1&b=2&c=3 |(同$args)
$realpath_root|/home/wwwroot/yii2/web |(当前请求的文档根目录或别名的真实路径，会将所有符号连接转换为真实路径)
$remote_addr|192.168.239.1 |(客户端地址)
$remote_port|49787 |(客户端端口)
$remote_user|- |(用于HTTP基础认证服务的用户名)
$request|GET /echo?a=1&b=2&c=3 HTTP/1.1 |(客户端的请求地址)
$request_body|- |(客户端的请求主体)
$request_body_file|- |(将客户端请求主体保存在临时文件中)
$request_completion|- |(如果请求成功，值为”OK”)
`$request_filename`|/home/wwwroot/yii2/web/echo |(当前连接请求的文件路径)
$request_length|425 |(请求的长度)
$request_method|GET |(HTTP请求方法)
$request_time|0.000 |(处理客户端请求使用的时间)
`$request_uri`|/echo?a=1&b=2&c=3 |(这个变量等于包含一些客户端请求参数的原始URI)
$scheme|http |(请求使用的Web协议)
$sent_http_[name]|- |(可以设置任意http响应头字段,如:$sent_http_content_length 4096)
$server_addr|192.168.239.136 |(服务器端地址)
$server_name|_ |(服务器名)
$server_port|80 |(服务器端口)
$server_protocol|HTTP/1.1 |(服务器的HTTP版本)
$status|000 |(HTTP响应代码)
$tcpinfo_rtt, $tcpinfo_rttvar, $tcpinfo_snd_cwnd, $tcpinfo_rcv_space|- |(客户端TCP连接的具体信息)
$time_iso8601|2018-04-11T14:53:36+08:00 |(服务器时间的ISO 8610格式)
$time_local|11/Apr/2018:14:53:36 +0800 |(服务器时间LOG Format 格式)
$uri|/echo |(请求中的当前URI)


#### 使nginx解析php
~~~
location ~ \.php$ {
                root           /var/www/html/taiping;
                fastcgi_pass   phpfpm:9000;
                fastcgi_index  index.php;
                fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
                include        fastcgi_params;
                fastcgi_param PHP_ADMIN_VALUE "open_basedir=/var/www/html/taiping/:/tmp/:/proc/";
        }
~~~