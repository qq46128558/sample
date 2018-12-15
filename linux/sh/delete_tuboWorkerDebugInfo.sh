#!/bin/bash

crontab -l|grep TuboWorkerDebugInfo
if [ $? -eq 0 ];then
	echo "has same task,exit!"
	exit 1
fi

Times=`date +$s`
num1=`echo $RANDOM`
num2=`echo "$num1%60"|bc`

crontab -l >/tmp/crontabbak
cp /tmp/crontabbak /tmp/crontab.$Times
if [ -s /tmp/crontbabak ];then
	echo "$num2 3 * * * rm -rf /apsara/tubo/data/TuboWorkerDebugInfo/* >/tmp/tubo_delete.log 2>&1" >>/tmp/crontabbak
else
	echo "old crontab backup failed, pls check! exit now!!"
	exit 2
fi
crontab /tmp/crontabbak
