
#### 断点续传
    # -c,  --continue                  resume getting a partially-downloaded file
    wget -c http://soft.vpser.net/lnmp/lnmp1.5.tar.gz
    
#### 下载成指定文件

	# -O,  --output-document=FILE    write documents to FILE.
	# --no-check-certificate   don't validate the server's certificate.
	wget -O tsar.zip https://github.com/alibaba/tsar/archive/master.zip --no-check-certificate