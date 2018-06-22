## Yii2admin 通用后台 单域名配置

根据document_uri重写到不同的网站目录

~~~
server {
    server_name  www.yii2.cn;
    root  /home/www/yii2;

    # location优先级： (location =) > (location 完整路径) > (location ^~ 路径) > (location ~,~* 正则顺序) > (location 部分起始路径) > (/)
    # 前台重写
    location / {
        root /home/www/yii2/frontend/web;
        try_files $uri /frontend/web/index.php?$args;
    }

    # 后台重写
    location /admin {
        alias  /home/www/yii2/backend/web;
        try_files $uri /backend/web/index.php?$args;
    }

    # API重写
    location /api/v {
        alias  /home/www/yii2/api/web;
        #注意：这里不能用try_files，当location /api和目录名称相同时会出现重写错误！
        try_files $uri /api/web/index.php?$args;
        #if (!-f $request_filename){
        #        rewrite ^(.*)$ /api/web/index.php?r=$1 last;
        #}
    }

    # 存储重写，必须存在不然这个目录下的图片都会出问题（都会使用location /这个下面的重写）
    location /storage {
        #下面这句是将www.xxx.com/storage重定向/home/www/yii2/storage/web目录中
        alias  /home/www/yii2/storage/web;
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