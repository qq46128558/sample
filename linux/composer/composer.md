
[中文文档](http://docs.phpcomposer.com/ "http://docs.phpcomposer.com/")

####  下载并安装composer(使用php命令行)
~~~
官网:https://getcomposer.org/download/

php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"

--install-dir
php composer-setup.php --install-dir=bin

--filename
php composer-setup.php --filename=composer

--version
php composer-setup.php --version=1.0.0-alpha8
~~~

#### 全局安装
    curl -sS https://getcomposer.org/installer | php
    mv composer.phar /usr/local/bin/composer

#### 安装zip/unzip
    #否则可能报错：
    #Failed to download bower-asset/bootstrap from dist: The zip extension and unzip command are both missing, skipping.
    apt-get install zip unzip -y



### 常见问题
~~~
Q: The "extra.asset-installer-paths" option is deprecated, use the "config.fxp-asset.installer-paths" option
(extra.asset-installer-paths已弃用)
A: 修改vim composer.json中对应路径的配置
"config": {
        "process-timeout": 1800,
        "fxp-asset":{
                "installer-paths":{
                        "npm-asset-library": "vendor/npm",
                        "bower-asset-library": "vendor/bower"
                }
        }
    },
~~~

~~~
Q: No valid bower.json was found in any branch or tag of https://github.com/jquery/jquery-dist.git, could not load a package from it
A: 需要配置github授权码
composer.json
"config": {
        "process-timeout": 1800,
        "github-oauth": {
          "github.com": "此处输入您的github授权码"
          }
    },

Q: 如何生成github授权码?
A: 登入github>>右上角settings>>Developer settings>>Personal access tokens>>generate new token
~~~