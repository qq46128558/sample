## php-fpm.conf 配置

#### 文件位置
    /usr/local/php/etc/php-fpm.conf
    ;或
    /etc/php/7.2/fpm/php-fpm.conf
    ;or
    /etc/php/7.1/fpm/php-fpm.conf

#### 加载其他文件的配置
    include=/etc/php/7.2/fpm/pool.d/*.conf

#### 服务的错误日志文件
    #用户及组:root.root
    error_log = /var/log/php7.2-fpm.log

#### 监听9000端口
~~~
; Start a new pool named 'www'.
[www]
listen=127.0.0.1:9000
; 注意注释这句
; listen = /run/php/php7.2-fpm.sock
~~~

#### php-fpm使用的用户及组
~~~
[www]
user = www-data
group = www-data
~~~

#### 进程配置
~~~
[www]
# 动态(最好看原注释)
pm = dynamic
# 最大子进程数
pm.max_children = 5
# 每个进程限制的内存数
;php_admin_value[memory_limit] = 32M
~~~