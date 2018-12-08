
#### 备份指定文件

	# 将1.log复制一份为1.log.1544248640(后面是当前时间戳)
	cp 1.log{,.$(date +%s)}

#### 自动加序号备份

	cp -f --backup=numbered 1.log 1.log

#### 复制目录及子目录及隐藏文件
	cp -rf yii2admin/. yii2

