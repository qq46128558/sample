
#### 用户授权
    # 授权yii_admin用户
    # 所有操作权限(all privileges:select/insert/update/delete)
    # 来自任意(%)主机
    # 使用密码yii_admin@123 连入
    # 操作yii2admin的所有表(.*)
    GRANT ALL PRIVILEGES ON yii2admin.* TO 'yii_admin'@'%' IDENTIFIED BY 'yii_admin@123';
    GRANT ALL PRIVILEGES ON 库名.表名 TO '用户名'@'IP地址' IDENTIFIED BY '密码' WITH GRANT OPTION;

#### 刷新权限
	FLUSH PRIVILEGES
	
#### 主从同步授权
    #授权从机器通过ceslave用户进行同步(replication)
    GRANT REPLICATION slave ON *.* TO 'ceslave'@'从机IP' IDENTIFIED BY 'ceslave@123';