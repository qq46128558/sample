# psftp

是一个使用命令提示列的软件,它提供sftp_client功能

* help: 查看命令的作用
* !: run a local command
* bye: finish your sftp session
* cd: change your remote working directory
* chmod: change file permissions and modes
* close: finish your sftp session but do not quit psftp
* del: delete files on the remote server
* dir: list remote files
* exit: finish your sftp session
* get: download a file from the server to your local machine
* help: give help
* lcd: change local working directory
* lpwd: print local working directory
* ls: list remote files
* mget: download multiple files at once
* mkdir: create directories on the remote server
* mput: upload multiple files at once
* mv: move or rename files on the remote server
* open: connect to a host
* put: upload a file from your local machine to the server
* pwd: print your remote working directory
* quit: finish your sftp session
* reget: continue downloading files
* ren: move or rename files on the remote server
* reput: continue uploading files
* rm: delete files on the remote server
* rmdir: remove directories on the remote server


## 常用指令
	
	# 连接主机
	open 10.210.1.130

	# 本地机操作:切换目录
	lpwd
	lcd c:\peter
	!dir

	# 远程机操作:切换目录,下载文件
	cd /usr/local/rds/log
	ls
	get misc_service.log

	# 关闭连接
	bye
