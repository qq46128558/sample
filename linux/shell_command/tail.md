
#### 查看系統日志
	
	# 该日志文件是许多进程日志文件的汇总，从该文件可以看出任何入侵企图或成功的入侵
	tail -100 /var/log/messages

##### 显示最后50行数据
    tail -50 `filename`

##### 显示最后10行,并持续显示有追加的
    tail -f `filename`
    #使用Ctrl+c退出

##### 从第24680行开始显示后面的
    tail -n +24680 `filename`

##### 可以显示多个文件的尾部
    tail `filename1` `filename2`

##### 与tail对应的是head
    head为显示文件的头行信息

##### 文件改名后不追踪显示(默认是追踪)
    tail --follow=name `fileanme`

