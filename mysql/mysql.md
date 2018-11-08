
#### 登入mysql
mysql -h`host` -u`user` -p`password` -P`port`

#### mysql命令行内不使用tab键的提示功能
	#-A, --no-auto-rehash 
	# No automatic rehashing. One has to use 'rehash' to get table and field completion. This gives a quicker start of mysql and disables rehashing on reconnect.
	mysql -A -h127.0.0.1 -uroot -p