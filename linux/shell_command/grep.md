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