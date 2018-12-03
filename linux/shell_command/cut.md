# cut

cut命令用来显示行中的指定部分，删除文件中指定字段。cut经常用来显示文件的内容。

说明：该命令有两项功能，其一是用来显示文件的内容，它依次读取由参数file所指 明的文件，将它们的内容输出到标准输出上；其二是连接两个或多个文件，如cut fl f2 > f3将把文件fl和几的内容合并起来，然后通过输出重定向符“>”的作用，将它们放入文件f3中。

## 语法

cut(选项)(参数)

## 选项

	-b：仅显示行中指定直接范围的内容；(字节)
	-c：仅显示行中指定范围的字符；(字符) (cut -c1-3 test.txt 打印第1个到第3个字符)
	-d：指定字段的分隔符，默认的字段分隔符为“TAB”；
	-f：显示指定字段的内容；(字段)
	-n：与“-b”选项连用，不分割多字节字符；
	--complement：补足被选择的字节、字符或字段；(提取指定字段之外的列?)
	--out-delimiter=<字段分隔符>：指定输出内容是的字段分割符；
	--help：显示指令的帮助信息；
	--version：显示指令的版本信息。

## 参数

文件：指定要进行内容过滤的文件。

## 实例
	
	# 显示cpu名称
	cat /proc/cpuinfo | grep name
		model name      : Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz
	cat /proc/cpuinfo | grep name | cut -d: -f2
		 Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz
