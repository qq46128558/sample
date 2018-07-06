
## [yii2admin](https://github.com/e282486518/yii2admin.git "https://github.com/e282486518/yii2admin.git")

- [yii2admin oschina]( http://git.oschina.net/ccdream/yii2admin "http://git.oschina.net/ccdream/yii2admin")
- [全站打包](https://share.weiyun.com/b0d11485e993bce1ee3398cbbf07e1e4 "https://share.weiyun.com/b0d11485e993bce1ee3398cbbf07e1e4") (安装出错的可以试试这个)


## 安装过程记录

### 系统安装
1. 系统Ubuntu 16.04 64位
2. 可选: apt-get update (如安装screen失败,更新源)
3. 安装screen工具: apt-get install screen
3. 启动一个会话: screen -S lnmp
4. 安装lnmp: wget -c http://soft.vpser.net/lnmp/lnmp1.5.tar.gz && tar zxf lnmp1.5.tar.gz && cd lnmp1.5 && ./install.sh lnmp
    - Install MySQL 5.7.22
    - 配置mysql密码如: 123456
    - enable InnoDB: y
    - Install PHP 7.2.6
    - Don't install Memory Allocator. (Default)
    - Install lnmp takes 63 minutes.
    - Install lnmp V1.5 completed! enjoy it.
4. 安装PHP fileinfo扩展模块(lnmp默认没开启)
    - 否则后面composer安装报错:  the requested PHP extension fileinfo is missing from your system.
    - cd /root/lnmp1.5/src/
    - tar jxf php-7.2.6.tar.bz2
    - cd php-7.2.6/ext/fileinfo/
    - /usr/local/php/bin/phpize
    - ./configure --with-php-config=/usr/local/php/bin/php-config
    - make && make install
    - ls /usr/local/php/lib/php/extensions/no-debug-non-zts-20170718/
    - vim /usr/local/php/etc/php.ini
        - 最后面增加: extension=/usr/local/php/lib/php/extensions/no-debug-non-zts-20170718/fileinfo.so
    - /etc/init.d/php-fpm restart
5. 安装Composer
    - apt-get install zip unzip php-zip -y
    - mkdir -p /data/www && cd /data/www
    - php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
    - php composer-setup.php --install-dir=/usr/bin --filename=composer
    - composer global require "fxp/composer-asset-plugin:^1.2.0"
        - 有可能报错,但不影响安装: Unzip with unzip command failed, falling back to ZipArchive class





### 安装 Yii2 advanced **(后来发现不用装)**
1. composer  create-project yiisoft/yii2-app-advanced yii 2.0.14
    - cd /data/www/yii
    - php init
2. 修改配置: vim /usr/local/nginx/conf/nginx.conf 
    - root  /data/www/yii/frontend/web/
    - 修改fastcgi配置: vim /usr/local/nginx/conf/fastcgi.conf 
        - fastcgi_param PHP_ADMIN_VALUE "open_basedir=/home/www/yii/:/tmp/:/proc/";
    - 重启服务: /etc/init.d/nginx restart
3. 测试 http://47.106.160.48/index.php 页面能打开则frontend已正确安装
4. 创建数据库
    - 进入数据库: mysql -hlocalhost -p123456
    - 创建数据库: mysql>create database yii2;
    - 退出数据库: mysql>quit
5. 修改配置:
    - 修改数据库连接配置: vim common/config/main-local.php
        - 配置 'db' 连接
        ~~~
        'db' => [
            'class' => 'yii\db\Connection',
            'dsn' => 'mysql:host=localhost;dbname=yii2',
            'username' => 'root',
            'password' => '123456',
            'charset' => 'utf8',
        ~~~
    - 数据迁移: /usr/local/php/bin/php /data/www/yii/yii migrate
    - 修改网站目录指向: vim /usr/local/nginx/conf/nginx.conf 
        - root  /data/www/yii/backend/web/
    - 重启服务: /etc/init.d/nginx restart
6. 测试 http://47.106.160.48/index.php 页面能打开则backend已正确安装




### 安装Yii2Admin
1. 下载安装
    - 切换工作目录: cd /data/www
    - 下载yii2admin源码: git clone  http://git.oschina.net/ccdream/yii2admin yii
    - ~~(不用装yii2 advanced)复制目录及子目录及隐藏文件: cp -rf yii2admin/. yii~~
    - cd /data/www/yii
2. 配置composer.json
    ~~~
    "config": {
        "fxp-asset":{
                "installer-paths":{
                        "npm-asset-library": "vendor/npm",
                        "bower-asset-library": "vendor/bower"
                }
        },
        "github-oauth":{
                "github.com":"填入你的github授权码"
        }
    },
    "extra": {
    },
    ~~~
    **b239145879923993bc168860e4f37286676cf617**
2. 安装依赖库前, 修改配置 vim /usr/local/php/etc/php.ini
    - 否则后面composer会报错: Failed to download bower-asset/yii2-pjax from source: The Process class relies on proc_open, which is not available on your PHP installation / The Process class relies on proc_open, which is not available on your PHP installation.
    - 找到 disable_functions = passthru,exec,system,chroot,chgrp,... 这一段, 将proc_open以及proc_get_status删除, 表示proc_open,proc_get_status可用
    - 重启php服务: /etc/init.d/php-fpm restart
3. 安装依赖库: composer install(or composer update)
    > **安装到此处发现问题,可以不用安装yii2 advanced 记录一下**

    ~~- 由于原yii2 advanced框架有一个脚本在里面, 所以第4步install出错提示user表已存在~~  
    ~~- cd console/migrations/~~  
    ~~- mv m130524_201442_init.php m130524_201442_init.php.bak~~
    
4. 配置环境、配置数据库并安装数据库(开始安装): /usr/local/php/bin/php /data/www/yii/yii install
    The archive may contain identical file names with different capitalization (which fails on case insensitive filesystems)
5. 配置nginx
    - 备份原配置文件 cp /usr/local/nginx/conf/nginx.conf /usr/local/nginx/conf/nginx.conf.bak
    - 修改配置文件 vim /usr/local/nginx/conf/nginx.conf
        - 删除 server{}段的内容
    - 新建配置文件/usr/local/nginx/conf/vhost/default.conf
    ~~~
    # ======================= Nginx Yii2通用后台 单域名配置=================================
    server {
        charset      utf-8;
        client_max_body_size  32M;
        listen       80; ## listen for ipv4
        #listen       [::]:80 default_server ipv6only=on; ## listen for ipv6
        server_name  _;
        root  /data/www/yii;
        index index.php index.html;
        access_log off;
        #access_log   /path/to/logs/advanced.access.log main buffer=50k;
        #error_log    /path/to/logs/advanced.error.log warn;
        # location优先级： (location =) > (location 完整路径) > (location ^~ 路径) > (location ~,~* 正则顺序) > (location 部分起始路径) > (/)
        # 前台重写
        location / {
            root /data/www/yii/frontend/web;
            try_files $uri /frontend/web/index.php?$args;
        }
        # 后台重写
        location /admin {
            alias  /data/www/yii/backend/web;
            try_files $uri /backend/web/index.php?$args;
        }
        # API重写
        location /api/v {
            alias  /data/www/yii/api/web;
            #注意：这里不能用try_files，当location /api和目录名称相同时会出现重写错误！
            try_files $uri /api/web/index.php?$args;
            #if (!-f $request_filename){
            #        rewrite ^(.*)$ /api/web/index.php?r=$1 last;
            #}
        }
        # 存储重写，必须存在不然这个目录下的图片都会出问题（都会使用location /这个下面的重写）
        location /storage {
            #下面这句是将www.xxx.com/storage重定向/vagrant/yii2admin/storage/web目录中
            alias  /data/www/yii/storage/web;
            #注意：这里不能用try_files，当location /storage和目录名称相同时会出现重写错误！
            #try_files $uri /storage/web/index.php?$args;
            #下面是隐藏index.php的重写
            #if (!-f $request_filename){
            #        rewrite ^(.*)$ /storage/web/index.php?$args last;
            #}
        }
        include enable-php.conf;
        #error_page  404 /404.html;
        # 排除文件
        location = /requirements.php {
            deny all;
        }
        location ~ \.(ht|svn|git|env) {
            deny all;
        }
    }
    ~~~
    - 重启服务: /etc/init.d/nginx restart
6. 测试 http://47.106.160.48/ 能打开前台页面, http://47.106.160.48/admin 能打开后台页面


