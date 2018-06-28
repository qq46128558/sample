## mysql主从结构搭建和原理


1. 配置mysql的cnf文件  
    vim /usr/local/mysql/my.cnf  
    **master机**  
    ~~~
    [mysqld]
    #启用二进制日志
    log-bin=mysql-bin 
    #服务器唯一ID默认是1一般取IP最后一段
    server_id=1 
    ~~~

    **slave机**
    ~~~
    [mysqld]
    #服务器唯一ID默认是1一般取IP最后一段
    server_id=2 
    ~~~

3. 重启mysqld服务
    ~~~
    service mysqld restart
    ~~~

4. 开启3306端口
    ~~~
    #插入一条规则,使开放3306端口
    iptables -I INPUT -p tcp --dport 3306 -j ACCEPT
    #保存防火墙规则
    /etc/rc.d/init.d/iptables save
    service iptables restart
    ~~~

5. 登录MySQL删除空用户

    *初始安装后root为空密码, 注意修改*
    ~~~
    mysql -h localhost -u root
    delete from mysql.user where user='' and host='localhost';
    delete from mysql.user where user='' and host='localhost.localdomain';
    ~~~
    *修改root密码的其中一种方法(123456就是你的密码)*  
    *UPDATE mysql.user SET password=PASSWORD('123456') WHERE user='root';*  
    *重启服务后生效*  
    *service mysqld restart*

6. 给slave服务器授权

    **master机**
    ~~~
    #确认已登入mysql,然后执行授权
    #授权从机器通过ceslave用户进行同步(replication)
    grant replication slave on *.* to 'ceslave'@'从机IP' identified by 'ceslave@123';
    #ceslave是用户名,ceslave@123是密码
    ~~~

    查询并记录file与position值
    ~~~
    #查询主数据库状态
    show master status;
    ~~~

    **slave机**
    ~~~
    #确认已登入mysql
    #停止同步进程
    stop slave;
    #执行同步配置语句,用到上面记录的file与position值
    change master to master_host='主机IP',master_user='ceslave',master_password='ceslave@123',master_log_file='mysql-bin.xxxxxx',master_log_pos=xxx;
    #启动同步进程
    start slave;
    #主从同步检查
    show slave status\G;
    #如果以下两个均为Yes, 则表示同步正常运行
    #Slave_IO_Running: Yes
    #Slave_SQL_Running: Yes
    ~~~

7. 重启mysqld服务
        
        service mysqld restart
        #设置mysqld服务开机自启动
        chkconfig mysqld on


8. 测试同步效果

    在master创建数据库, 数据表, 插入记录
    ~~~
    create database mytest;
    create table mytest.user(id int, name varchar(50));
    insert into mytest.user (id,name) values (1, 'jason');
    ~~~
    
    在slave中能查询到新创建的
    ~~~
    select * from mytest.user;
    ~~~