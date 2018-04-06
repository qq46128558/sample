
#### 全局安装
    curl -sS https://getcomposer.org/installer | php
    mv composer.phar /usr/local/bin/composer

#### 安装zip/unzip
    #否则可能报错：
    #Failed to download bower-asset/bootstrap from dist: The zip extension and unzip command are both missing, skipping.
    apt-get install zip unzip -y