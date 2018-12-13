##### grep 需要用到转义的字符
    $
    "
    - 中线

#### 筛选dokcer image id
	
	# 列出docker iamges,指定空格分隔符,打印第三列,再忽略大小写,不抓取image行,排序,取唯一
	docker images|awk -F ' ' '{print $3}'|grep -v -i image|sort|uniq
		0346349a1a64
		1f47fade220d
		419f6c33af0e

#### 筛选使用中的image
	
	# 循环所有容器的id,逐一检查容器,取出image id,并只输出前12位,排序,取唯一(与上面的筛选对比,可查询冗余的镜像,即没有使用到的镜像)
	for i in `docker ps -aq`;do iid=`docker inspect -f {{.Image}} $i`;echo ${iid:0:12};done|sort|uniq
		sha256:03463
		sha256:1f47f
		sha256:419f6
	for i in `docker ps -aq`;do iid=`docker inspect -f {{.Image}} $i`;echo ${iid:7:12};done|sort|uniq
		0346349a1a64
		1f47fade220d
		419f6c33af0e
	
#### 正则表达式 [:digit:]

	# 数字开头 单个字符 数字(任意长度) G结尾
	du -h |grep "^[[:digit:]].[[:digit:]]*G"
		1.1G    ./taiping
		1.1G    .

##### 查找到的关键字显示颜色
    grep --color=auto

##### -n 查找并输出行号
    ls -l|grep -n "peter"
    grep -n "yii" ./xbh_plugin/*.php

##### -v 排除特定值
    ps aux|grep "redis-server"|grep -v grep

##### 或条件
    #用转义\|
    grep 'usrquota\|grpquota' /etc/fstab
    #加-E (扩展正则)
    netstat -an | grep -E "ESTABLISHED|WAIT"
    #加-e
    netstat -an | grep -e EST -e WAIT

* -q 不显示任何信息(一般用于脚本)
* -i 忽略字符大小写的差别
* -v 反转查找


#### 显示匹配某个结果之前的3行，使用 -B 选项：(反之:-A 显示匹配结果之后的行)
    seq 10|grep "5" -B3
    2
    3
    4
    5

~~~阿里运维应用示例
puadmin lscs|grep -B1 ERROR
# 则出现一行OK和一行ERROR
puadmin lscs|grep -v OK|grep -B1 ERROR
# 则先排除OK的,形成一个ERROR带一级标题的结果,再抓取ERROR的并多显示前面的一级标题
~~~