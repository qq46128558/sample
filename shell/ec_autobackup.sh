#!/bin/bash
#取当前日期
dir1=`date "+%Y%m%d"`
#取30天前的日期
dir2=`date -d "-15 days" "+%Y%m%d"`

#开始备份,带计时
if [ ! -d /data/bak/${dir1} ]
then
mkdir -p /data/bak/${dir1}
time1=`date +%s`
cp /data/httpd /data/bak/${dir1} -r
cp /data/ftp /data/bak/${dir1} -r
cp /data/mysql /data/bak/${dir1} -r
time2=`date +%s`
timetotal=`expr ${time2} - ${time1}`
echo '['`date`']'${dir1}'备份用时:'${timetotal}'秒.'>>/data/bak/backup.log
fi

#开始删除旧的备份
if [ -d /data/bak/${dir2} ]; then rm -rf /data/bak/${dir2}; echo -e "["`date`"]""删除备份/data/bak/${dir2}成功.">>/data/bak/backup.log; fi


