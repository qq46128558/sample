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