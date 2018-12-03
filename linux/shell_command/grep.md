##### grep 需要用到转义的字符
    $
    "
    -

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
    #加-E
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