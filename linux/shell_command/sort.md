# sort

它将文件进行排序，并将排序结果标准输出。sort命令既可以从特定的文件，也可以从stdin中获取输入。

## 语法

sort(选项)(参数)

## 选项

* -b：忽略每行前面开始出的空格字符；
* -c：检查文件是否已经按照顺序排序；
* -d：排序时，处理英文字母、数字及空格字符外，忽略其他的字符；
* -f：排序时，将小写字母视为大写字母；
* -i：排序时，除了040至176之间的ASCII字符外，忽略其他的字符；
* -m：将几个排序号的文件进行合并；
* -M：将前面3个字母依照月份的缩写进行排序；
* -n：依照数值的大小排序；
* -o<输出文件>：将排序后的结果存入制定的文件；
* -r：以相反的顺序来排序；
* -t<分隔字符>：指定排序时所用的栏位分隔字符；
* +<起始栏位>-<结束栏位>：以指定的栏位来排序，范围由起始栏位到结束栏位的前一栏位。
* -u: 忽略相同行
* -k: 指定需要排序的栏位

## 参数

文件：指定待排序的文件列表。

## 实例
	
	# 查找大于1M的文件,以du格式显示(使文件大小在第1列)
	# 然后按数值大小的倒序排列
	# 显示前5行记录
	find taiping/ -type f -size +1M|xargs -n1 -i du -sh {}|sort -nr|head -5
	# 显示结果参考
	54M     taiping/vendor/codeception/base/.git/objects/pack/pack-ba5482e0d0c2f4812e4f28cbbf34dac36ad8d184.pack
	36M     taiping/vendor/yiisoft/yii2/.git/objects/pack/pack-8318257d10d2a62349a7c1870ec3ff1d372b8bd2.pack
	30M     taiping/vendor/phpunit/phpunit/.git/objects/pack/pack-c687afa2ffad7423571d41d6a087fc2446bd2a4b.pack
	14M     taiping/.git/objects/pack/pack-eb0b97f914d7a24b8c22af7686eef69a12ba6b12.pack
	12M     taiping/vendor/kartik-v/bootstrap-fileinput/.git/objects/pack/pack-a18037763ec2c35f14ae9a2419c987a40f72fbf4.pack
	# 指定按第7列数值排序
	root@iZwz9ez6s5dkap404mwg8iZ:~# ls -l|sort -nk7
	total 3432
	-rw-r--r-- 1 root root 3350555 Oct 15 18:32 lnmp-install.log
	drwxr-xr-x 7 root root    4096 Jul 22 08:54 lnmp1.5
	-rw-r--r-- 1 root root  149744 Aug 24 21:36 lnmp1.5.tar.gz

## -k选项的具体语法格式

	FStart.CStart Modifie,FEnd.CEnd Modifier
	-------Start--------,-------End--------
	FStart.CStart 选项  ,  FEnd.CEnd 选项

这个语法格式可以被其中的逗号,分为两大部分，Start部分和End部分。Start部分也由三部分组成，其中的Modifier部分就是我们之前说过的类似n和r的选项部分。我们重点说说Start部分的FStart和C.Start。C.Start也是可以省略的，省略的话就表示从本域的开头部分开始。FStart.CStart，其中FStart就是表示使用的域，而CStart则表示在FStart域中从第几个字符开始算“排序首字符”。同理，在End部分中，你可以设定FEnd.CEnd，如果你省略.CEnd，则表示结尾到“域尾”，即本域的最后一个字符。或者，如果你将CEnd设定为0(零)，也是表示结尾到“域尾”。

示例: 从公司英文名称的第二个字母开始进行排序：

	$ sort -t ' ' -k 1.2 facebook.txt
	baidu 100 5000
	sohu 100 4500
	google 110 5000
	guge 50 3000

**使用了-k 1.2，表示对第一个域的第二个字符开始到本域的最后一个字符为止的字符串进行排序**。你会发现baidu因为第二个字母是a而名列榜首。sohu和 google第二个字符都是o，但sohu的h在google的o前面，所以两者分别排在第二和第三。guge只能屈居第四了。

只针对公司英文名称的第二个字母进行排序，如果相同的按照员工工资进行降序排序：

	$ sort -t ' ' -k 1.2,1.2 -nrk 3,3 facebook.txt
	baidu 100 5000
	google 110 5000
	sohu 100 4500
	guge 50 3000

由于**只对第二个字母进行排序** ，所以我们使用了-k 1.2,1.2的表示方式，表示我们“只”对第二个字母进行排序。（如果你问“我使用-k 1.2怎么不行？”，当然不行，因为你省略了End部分，这就意味着你将对从第二个字母起到本域最后一个字符为止的字符串进行排序）。对于员工工资进行排 序，我们也使用了-k 3,3，这是最准确的表述，表示我们“只”对本域进行排序，因为如果你省略了后面的3，就变成了我们“对第3个域开始到最后一个域位置的内容进行排序” 了。