
## mysql

### 基本操作

#### 登入mysql
mysql -h`host` -u`user` -p`password` -P`port`

#### mysql命令行内不使用tab键的提示功能
	#-A, --no-auto-rehash 
	# No automatic rehashing. One has to use 'rehash' to get table and field completion. This gives a quicker start of mysql and disables rehashing on reconnect.
	mysql -A -h127.0.0.1 -uroot -p

### 还原逻辑备份(mysqldump备份的)

#### 还原MySQL数据库的命令
	
	mysql -h`host` -u`user` -p `database` < `filename`

#### 还原压缩的MySQL数据库
	
	gunzip < `filename` | mysql -h`host` -u`user` -p `database`

## mysqldump

### 逻辑备份(即脚本备份,没有索引)

#### 备份数据库
	#变量如host:127.0.0.1 user:root database:tp_website filename:tp_website1224.sql
	mysqldump -h`host` -u`user` -p `database` > `filename`

#### 备份为带删除表的格式，能够让该备份覆盖已有数据库而不需要手动删除原有数据库

	#--add-drop-table
	mysqldump --add-drop-table -h`host` -u`user` -p `database` > `filename`

#### 备份某个(些)表

	mysqldump -h`host` -u`user` -p `database` `table1` `table2` > `filename`

#### 同时备份多个数据库
	
	#--databases
	mysqldump -h`host` -u`user` -p --databases `database1` `database2` > `filename`

#### 仅仅备份数据库结构
	
	#--no-data
	mysqldump --no-data -h`host` -u`user` -p `database` > `filename`

#### 备份服务器上所有数据库

	--all-databases

#### 压缩备份
	
	mysqldump -h`host` -u`user` -p `database` | gzip > `filename`