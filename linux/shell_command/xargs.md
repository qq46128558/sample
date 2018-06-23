xargs 可以 **读入 stdin(标准输入) 的资料，并且以空白字元或断行字元作为分辨，将 stdin 的资料分隔成为 arguments** 。 因为是以空白字元作为分隔，所以，如果有一些档名或者是其他意义的名词内含有空白字元的时候， xargs 可能就会误判.

> 这个命令(效果)是错误的 (只显示出当前目录的内容)  
> find /sbin -perm +700 |ls -l  
> 这样才是正确的  
> find /sbin -perm +700 |xargs ls -l 

> 这句:  
> $find ./ -exec grep "app" {} \;  
> 效果同这句:  
> $find ./ |xargs grep "app"

#### -a 从文件(test.php)中读入作为stdin
	xargs -a test.php echo -e '\033[33;1m'

读取的内容以黄色粗体显示. 改进一版,结束后还原:

	xargs -a test.php echo -e '\033[33;1m' && echo -e '\033[0m'

#### -E flag 有flag这个标志的时候就停止
有时候可能会是 -e  

	ls -l|xargs -E "www" echo


#### -p 每次执行一个argument的时候询问一次用
	ls -d */|xargs -p ls

#### -n num 命令在执行的时候一次用的argument的个数
默认是用所有的

	ls -d */|xargs -p -n 1 ls

#### -t 先打印命令然后再执行
	xargs -a test.php -t echo -e "\033[33;1m"&& echo -e '\033[0m'

#### -i 将xargs的每项名称一行行赋值给{}用{}代替
	ls test.txt|xargs -t -i mv {} {}.bak

#### -r 当xargs的输入为空的时候则停止xargs
	echo ""|xargs -t mv
	echo ""|xargs -t -r mv

#### -x exit的意思主要配合-s使用
	略

#### -s num xargs后面那个命令的最大命令行字符数
超出则无法显示  
xargs: argument list too long

	ls -d */|xargs -t -i -x -s 33  echo -e "\033[33;1m{}\033[0m"

#### -d delim 修改xargs的分隔符
	ls -d */|xargs -t -d "_" -i echo -e "\033[33;1m{}\033[0m"

---
#### -P 修改最大的进程数,默认是1,为0时候为as many as it can
	(未研究)

#### -L或-l num Use at most max-lines nonblank input lines per command line
	(未研究)
