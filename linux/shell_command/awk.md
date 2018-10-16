# awk

awk是一种编程语言，用于在linux/unix下对文本和数据进行处理。数据可以来自标准输入(stdin)、一个或多个文件，或其它命令的输出。它支持用户自定义函数和动态正则表达式等先进功能，是linux/unix下的一个强大编程工具。它在命令行中使用，但更多是作为脚本来使用。awk有很多内建的功能，比如数组、函数等，这是它和C语言的相同之处，灵活性是awk最大的优势。

## 语法

	awk [options] 'script' var=value file(s)
	awk [options] -f scriptfile var=value file(s)

## 常用命令选项

	-F fs   fs指定输入分隔符，fs可以是字符串或正则表达式，如-F:
	-v var=value   赋值一个用户定义变量，将外部变量传递给awk
	-f scripfile  从脚本文件中读取awk命令
	-m[fr] val   对val值设置内在限制，-mf选项限制分配给val的最大块数目；
	-mr选项限制记录的最大数目。这两个功能是Bell实验室版awk的扩展功能，在标准awk中不适用。

## awk模式和操作

	awk脚本是由模式和操作组成的。

### 模式

* /正则表达式/：使用通配符的扩展集。
* 关系表达式：使用运算符进行操作，可以是字符串或数字的比较测试。
* 模式匹配表达式：用运算符~（匹配）和~!（不匹配）。
* BEGIN语句块、pattern语句块、END语句块：参见awk的工作原理

### 操作

操作由一个或多个命令、函数、表达式组成，之间由换行符或分号隔开，并位于大括号内，主要部分是：

* 变量或数组赋值
* 输出命令
* 内置函数
* 控制流语句

## awk脚本基本结构

	awk 'BEGIN{ print "start" } pattern{ commands } END{ print "end" }' file

一个awk脚本通常由：BEGIN语句块、能够使用模式匹配的通用语句块、END语句块3部分组成，这三个部分是可选的。任意一个部分都可以不出现在脚本中，脚本通常是被单引号或双引号中，例如：

	awk 'BEGIN{ i=0 } { i++ } END{ print i }' filename
	awk "BEGIN{ i=0 } { i++ } END{ print i }" filename
	#测试
	awk 'BEGIN{i=0}{i++}END{print i}' test.php
	#结果
	19

## awk的工作原理

	awk 'BEGIN{ commands } pattern{ commands } END{ commands }'

* 第一步：执行BEGIN{ commands }语句块中的语句；
* 第二步：从文件或标准输入(stdin)读取一行，然后执行pattern{ commands }语句块，它逐行扫描文件，从第一行到最后一行重复这个过程，直到文件全部被读取完毕。
* 第三步：当读至输入流末尾时，执行END{ commands }语句块。

BEGIN语句块在awk开始从输入流中读取行之前被执行，这是一个可选的语句块，比如变量初始化、打印输出表格的表头等语句通常可以写在BEGIN语句块中。

END语句块在awk从输入流中读取完所有的行之后即被执行，比如打印所有行的分析结果这类信息汇总都是在END语句块中完成，它也是一个可选语句块。

pattern语句块中的通用命令是最重要的部分，它也是可选的。如果没有提供pattern语句块，则默认执行{ print }，即打印每一个读取到的行，awk读取的每一行都会执行该语句块。

	# 示例
	echo -e "A line 1\nA line 2" | awk 'BEGIN{ print "Start" } { print } END{ print "End" }'
	# 结果
	Start
	A line 1
	A line 2
	End

当使用不带参数的print时，它就打印当前行，当print的参数是以逗号进行分隔时，打印时则以空格作为定界符。在awk的print语句块中双引号是被当作拼接符使用，例如：
	
	# 示例
	echo | awk '{ var1="v1"; var2="v2"; var3="v3"; print var1,var2,var3; }' 
	# 结果
	v1 v2 v3

双引号拼接使用：
	
	# 示例
	echo | awk '{ var1="v1"; var2="v2"; var3="v3"; print var1"="var2"="var3; }'
	# 结果
	v1=v2=v3

{ }类似一个循环体，会对文件中的每一行进行迭代，通常变量初始化语句（如：i=0）以及打印文件头部的语句放入BEGIN语句块中，将打印的结果等语句放在END语句块中。

## awk内置变量（预定义变量）





## 应用实例
	# 查找taiping目录内大于1M的文件, 并以du格式显示出其大小
	# 再通过awk合计后输出合计值
	find ./taiping/ -type f -size +1M |xargs -n1 -i du -sm {}|awk '{sum+=$1}END{print sum"M"}'
	# 输出结果参考
	298M