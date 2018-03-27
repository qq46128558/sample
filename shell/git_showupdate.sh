#!/bin/bash
# 取第一个参数值
after=$1
# 如无值取当前日期
if [ -z ${after} ]; then after=`date +%Y-%m-%d`; fi
# 查看日期之后新增修改删除过的文件
git log --after=${after} --name-status --pretty=format:''|xargs -i echo {}

# 遗留问题:去重