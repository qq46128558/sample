
## [yii2admin](https://github.com/e282486518/yii2admin.git "https://github.com/e282486518/yii2admin.git")
yii2+metronic v4.5.6+bootstrap v3.3.6
+layui v2.4.3


- [yii2admin oschina]( http://git.oschina.net/ccdream/yii2admin "http://git.oschina.net/ccdream/yii2admin")

## 安装过程记录

### 系统安装
1. 系统Ubuntu 16.04 64位,远程shell连入
2. 可选: apt-get update (阿里云服务器初次使用需要更新源)
3. 安装screen工具: apt-get install screen
3. 启动一个会话: screen -S lnmp
4. 安装lnmp: wget -c http://soft.vpser.net/lnmp/lnmp1.5.tar.gz && tar zxf lnmp1.5.tar.gz && cd lnmp1.5 && ./install.sh lnmp
    - Install MySQL 5.7.22
    - 配置mysql密码如: 123456(自定义)
    - enable InnoDB: y
    - Install PHP 7.2.6
    - Don't install Memory Allocator. (Default)
    - 1核2G 1M宽带安装约需1个小时
4. 安装PHP fileinfo扩展模块(lnmp默认没开启)
    - 否则后面composer安装报错:  the requested PHP extension fileinfo is missing from your system.
    - cd /root/lnmp1.5/src/
    - tar jxf php-7.2.6.tar.bz2
    - cd php-7.2.6/ext/fileinfo/
    - /usr/local/php/bin/phpize
    - ./configure --with-php-config=/usr/local/php/bin/php-config
    - make && make install
    - 查看fileinfo.so是否存在：ls /usr/local/php/lib/php/extensions/no-debug-non-zts-20170718/
    - 编辑配置：vim /usr/local/php/etc/php.ini
        - 最后面增加: extension=/usr/local/php/lib/php/extensions/no-debug-non-zts-20170718/fileinfo.so
    - 重启服务：/etc/init.d/php-fpm restart
5. 安装Composer
    - 额外需要的工具：apt-get install zip unzip php-zip -y
    - mkdir -p /data/www && cd /data/www
    - 利用php来下载composer: php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
    - 安装composer: php composer-setup.php --install-dir=/usr/bin --filename=composer
    - 引入yii框架所需要的组件：composer global require "fxp/composer-asset-plugin:^1.2.0"
        - 有可能报错,但不影响安装: Unzip with unzip command failed, falling back to ZipArchive class

### 安装Yii2Admin
1. 下载安装
    - 切换工作目录: cd /data/www
    - 下载yii2admin源码: git clone  http://git.oschina.net/ccdream/yii2admin yii
    - cd /data/www/yii
2. 配置composer.json
    - config内对象增加fxp-asset以及github-oauth
    - extra内对象删除
    ~~~
    "config": {
        "fxp-asset":{
                "installer-paths":{
                        "npm-asset-library": "vendor/npm",
                        "bower-asset-library": "vendor/bower"
                }
        },
        "github-oauth":{
                "github.com":"填入你的github token"
        }
    },
    "extra": {
    },
    ~~~
    **如何获取github token**

    登入你的github账号>>右上角settings>>Developer settings>>Personal access tokens>>generate new token

2. 安装依赖库前, 修改配置 vim /usr/local/php/etc/php.ini
    - 否则后面composer会报错: Failed to download bower-asset/yii2-pjax from source: The Process class relies on proc_open, which is not available on your PHP installation / The Process class relies on proc_open, which is not available on your PHP installation.
    - 找到 disable_functions = passthru,exec,system,chroot,chgrp,... **这一段, 将proc_open以及proc_get_status删除**, 表示proc_open,proc_get_status可用
    - 重启php服务: /etc/init.d/php-fpm restart
    
3. 安装依赖库: composer install

4. 配置环境、配置数据库并安装数据库(开始安装): /usr/local/php/bin/php /data/www/yii/yii install
    
5. 配置nginx
    - 备份原配置文件 cp /usr/local/nginx/conf/nginx.conf /usr/local/nginx/conf/nginx.conf.bak
    - 修改配置文件 vim /usr/local/nginx/conf/nginx.conf
        - 删除 server{}段的内容
    - 新建配置文件/usr/local/nginx/conf/vhost/default.conf,贴入以下内容：
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
6. 测试 http://服务器IP地址/ 能打开前台页面, http://服务器IP地址/admin 能打开后台页面
7. 最后shell退出screen: exit



