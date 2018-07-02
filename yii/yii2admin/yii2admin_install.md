
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
5. 
