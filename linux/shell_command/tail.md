
#### tailf

    tailf命令几乎等同于tail -f，严格说来应该与tail --follow=name更相似些。

    当文件改名之后它也能继续跟踪，特别适合于日志文件的跟踪（follow the growth of a log file）。与tail -f不同的是，如果文件不增长，它不会去访问磁盘文件。tailf特别适合那些便携机上跟踪日志文件，因为它能省电，因为减少了磁盘访问。tailf命令不是个脚本，而是一个用C代码编译后的二进制执行文件，某些Linux安装之后没有这个命令。

#### tailf和tail -f的区别

* tailf 总是从文件开头一点一点的读， 而tail -f 则是从文件尾部开始读
* tailf check文件增长时，使用的是文件名， 用stat系统调用；而tail -f 则使用的是已打开的文件描述符； 注：tail 也可以做到类似跟踪文件名的效果； 但是tail总是使用fstat系统调用，而不是stat系统调用；结果就是：默认情况下，当tail的文件被偷偷删除时，tail是不知道的，而tailf是知道的。

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

