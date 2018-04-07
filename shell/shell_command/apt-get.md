## Ubuntu

#### apt源文件
    vim /etc/apt/sources.list
    #参考内容
    deb http://mirrors.aliyun.com/ubuntu/ vivid main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ vivid-security main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ vivid-updates main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ vivid-proposed main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ vivid-backports main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ vivid main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ vivid-security main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ vivid-updates main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ vivid-proposed main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ vivid-backports main restricted universe multiverse

    #Archive type
    #条目的第一个词 deb 或是 deb-src 表明了所获取的软件包档案类型
    deb
    档案类型为二进制预编译软件包，一般我们所用的档案类型。
    deb-src
    档案类型为用于编译二进制软件包的源代码

    #Repository URL 
    #条目的第二个词则是软件包所在仓库的地址

    #Distribution
    #跟在仓库地址后的是发行版。
    发行版有两种分类方法，一类是发行版的具体代号，如 xenial, trusty, precise 等；还有一类则是发行版的发行类型，如 oldstable, stable, testing 和 unstable。
    另外，在发行版后还可能有进一步的指定，如 xenial-updates, trusty-security, stable-backports 等。

    #Component
    #跟在发行版之后的就是软件包的具体分类了，可以有一个或多个。
    	                自由软件	    非自由软件
        官方支持的	     Main	        Restricted
        非官方支持的	 Universe	    Multiverse


#### apt更新源
    cat /etc/apt/sources.list

#### 安装软件
    apt-get install `名称` -y

#### 刷新源列表
    apt-get update

#### 安装常用软件
    #nginx
    apt-get install nginx -y
    #mysql
    apt-get install mysql-server -y
    #redis
    apt-get install redis-server -y
    #tree(树形目录查看)
    apt-get install tree -y
    #sysv-rc-conf(开机服务启动管理)
    apt-get install sysv-rc-conf -y
    #screen(会话管理)
    apt-get install screen -y
    
#### 取得apt安装的nginx源码
    #最好先进入到家目录
    apt-get source nginx