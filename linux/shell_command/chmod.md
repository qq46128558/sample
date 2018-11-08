# chmod权限修改

#### 用户,组,其他人赋予权限
	
	# 用户赋予写权限
	chmod u+w `filename`
	# u用户 g组 o其他人 a所有人 r读 w写 x执行 +赋予 -去除
	# chmod ug+rw `filename`