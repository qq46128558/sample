# [基于Docker搭建LNMP环境](https://blog.csdn.net/xy752068432/article/details/75975065 "https://blog.csdn.net/xy752068432/article/details/75975065")

1. docker安装mysql
	- docker pull mysql:5.6 (拉取)
	- docker images (查看)
2. 启动mysql
	- docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 --name mysql mysql:5.6 (运行)
	- docker ps (查看)
3. 进入mysql容器
	- docker exec -ti mysql /bin/bash (进入)

	> 容器中默认是没有vim的，所以我们首先要安装vim,需要注意的是安装前记得先执行apt update命令，不然安装会出现问题。 进入到mysql容器后，我们通过创建一个远程可以访问的用户，这样我们就能从别的主机访问到我们的数据库了

	> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456';

	> FLUSH PRIVILEGES

4. docker安装php-fpm 
	- docker pull php:7.0-fpm (拉取)
5. 启动php-fpm
	- docker run -d -v /var/nginx/www/html:/var/www/html -p 9000:9000 --link mysql:mysql --name phpfpm php:7.0-fpm

	> 这里如果不指定–link参数其实也是可以得，因为容易本身也是有ip的且唯一，所以我们也可以直接利用ip去访问容器。

6. 进入phpfpm容器
	- docker exec -ti phpfpm /bin/bash (进入)
	- docker-php-ext-install pdo_mysql (安装php扩展pdo_mysql)(因为后面我要使用pdo模块进行测试)
	- php -m  (查看我们的php的所有扩展模块，我们可以去看到我们刚刚安装的pdo_mysql扩展也在里面)
	- 还需修改一下php.ini pdo_mysql才能用(后面讲)

	> 然后进入到我们的容器，然后我们在/var/www/html目录下新建一个index.php文件 touch index.php 退出到主机:按 ctrl + p + q, 发现主机的/var/nginx/www/html目录中也存在该文件，因为在创建容器的时候，我们已经把主机中的目录挂载到了容器中去了

7. docker安装nginx 
	- docker pull nginx:1.10.3
8. 启动nginx
	- docker run -d -p 80:80 -v /var/nginx/www/html:/var/www/html --link phpfpm:php --name nginx nginx:1.10.3

	> -v 添加目录映射,这里最好nginx容器的根目录最好写成和php容器中根目录一样。但是不一定非要一模一样,如果不一样在配置nginx的时候需要注意 

9. 进入nginx容器
	- docker exec -ti nginx /bin/bash
	- vim /etc/nginx/conf.d/default.conf (修改配置文件)

	~~~
	location ~ \.php$ {
        root           /var/www/html;
        fastcgi_pass   phpfpm:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
    }
    ~~~
10. 退出到主机, 编辑 /var/nginx/www/html/index.php : <?php phpinfo(); ?>
11. 客户端打开页面测试, 查找pdo, 发现 PDO drivers 只有 sqlite
12. 进入phpfpm容器
	- 将 /usr/local/etc/php/php.ini-development 改为 /usr/local/etc/php/php.ini
	- vim /usr/local/etc/php/php.ini 增加:
	- extension=/usr/local/lib/php/extensions/no-debug-non-zts-20151012/pdo_mysql.so
	- pdo.mysql.so可用find查找
13. **重启服务即重启容器**
	- docker stop phpfpm
	- docker start phpfpm
13. 再次到客户端打开页面测试, 查找pdo, 发现 PDO drivers 多了 mysql
14. 编辑index.php
	~~~
	try {
    $con = new PDO('mysql:host=mysql;dbname=mysql', 'root', '123456');
    $con->query('SET NAMES UTF8');
    $res =  $con->query('select * from user');
    while ($row = $res->fetch(PDO::FETCH_ASSOC)) {
        echo "user:{$row['User']} host:{$row['Host']}";
    }
	} catch (PDOException $e) {
	     echo '错误原因：'  . $e->getMessage();
	}
	~~~
15. 测试index.php页面是否能正常打开

## 问题记录
- PHP Warning:  Module 'pdo_mysql' already loaded in Unknown on line 0
	- /usr/local/etc/php/中有php.ini
	- /usr/local/etc/php/conf.d中有docker-php-ext-pdo_mysql.ini
	- 两个ini中有重复的extension,注释其中一个即可