# time

time命令用于统计给定命令所花费的总时间。

## 语法
	
	time(参数)

## 参数
	
	指令：指定需要运行的额指令及其参数。

## 实例

~~~html
[root@localhost ~]# time ls
anaconda-ks.cfg  install.log  install.log.syslog  satools  text

real    0m0.009s
user    0m0.002s
sys     0m0.007s
~~~

* real时间是指挂钟时间，也就是命令开始执行到结束的时间。这个短时间包括其他进程所占用的时间片，和进程被阻塞时所花费的时间。
* user时间是指进程花费在用户模式中的CPU时间，这是唯一真正用于执行进程所花费的时间，其他进程和花费阻塞状态中的时间没有计算在内。
* sys时间是指花费在内核模式中的CPU时间，代表在内核中执系统调用所花费的时间，这也是真正由进程使用的CPU时间。
