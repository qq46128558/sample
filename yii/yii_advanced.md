
## Yii2 的高级应用程序模板

### 搭建过程记录
1. 安装lnmp环境
2. https://lnmp.org/
3. screen -S lnmp
4. wget -c http://soft.vpser.net/lnmp/lnmp1.5.tar.gz && tar zxf lnmp1.5.tar.gz && cd lnmp1.5 && ./install.sh lnmp
5. 安装完成后, ctrl+c退出
6. nginx配置: /usr/local/nginx/conf/nginx.conf
7. php配置: /usr/local/php/etc/php.ini
    ~~~
    display_errors = On
    html_errors = On
    ;open_basedir =
    ~~~
8. 下载yii高级模板: http://www.yiichina.com/download
9. 解压到 /home/www, 并将advance改名为yii2
10. 执行/home/www/yii2/init php脚本,进行环境初始化
10. 修改root目录
    ~~~
    /usr/local/nginx/conf/nginx.conf
    root  /home/www/yii2/frontend/web;
    ~~~
11. 打开地址: http://47.106.160.48/index.php
    ~~~
    报错: Failed opening required: XXX/../vendor/autoload.php
    修改配置文件: /usr/local/nginx/conf/fastcgi.conf
    fastcgi_param PHP_ADMIN_VALUE "open_basedir=/home/www/yii2/:/tmp/:/proc/";
    重新相关服务
    ~~~
12. yii2框架搭建完成