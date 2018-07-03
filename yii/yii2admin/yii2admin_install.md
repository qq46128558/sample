
## [yii2admin](https://github.com/e282486518/yii2admin.git "https://github.com/e282486518/yii2admin.git")

- [yii2admin oschina]( http://git.oschina.net/ccdream/yii2admin "http://git.oschina.net/ccdream/yii2admin")
- [全站打包](https://share.weiyun.com/b0d11485e993bce1ee3398cbbf07e1e4 "https://share.weiyun.com/b0d11485e993bce1ee3398cbbf07e1e4") (安装出错的可以试试这个)


### 安装过程记录
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
5. 安装Composer
    - mkdir -p /data/www && cd /data/www
    - php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
    - php composer-setup.php --install-dir=/usr/bin --filename=composer
6. 安装Yii2 advanced
    - apt-get install zip unzip php-zip -y
    - composer global require "fxp/composer-asset-plugin:^1.2.0"
        - (未解决)报错但不影响安装: Unzip with unzip command failed, falling back to ZipArchive class
    - composer  create-project yiisoft/yii2-app-advanced yii 2.0.14
    - cd /data/www/yii
    - php init
    - vim /usr/local/nginx/conf/nginx.conf 修改网站目录指向
        - root  /data/www/yii/frontend/web/
    - vim /usr/local/nginx/conf/fastcgi.conf 修改
        - fastcgi_param PHP_ADMIN_VALUE "open_basedir=/home/www/yii/:/tmp/:/proc/";
    - /etc/init.d/nginx restart
    - 测试 http://47.106.160.48/index.php 页面能打开为正确安装
    
