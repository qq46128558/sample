#!/bin/bash
# 取第一个参数值,支持时间,如: "2018-03-27 09:00"
after=$1
# 如无值取当前日期
if [ -z "${after}" ]
then 
    after=`date +"%Y-%m-%d 00:00"`
fi
# 查看日期之后新增修改删除过的文件,结果存入临时文件
git log --after="${after}" --name-only --pretty=format:''|xargs -i echo {}>>temp.log
# 按行读取临时文件入files变量,为了可以for循环
files=`xargs -a temp.log -n 1`
# 置空临时文件,为了复用
echo ''>temp.log

for file in ${files}
do
    # 查找该文件是否已记录
    cat temp.log|grep ${file} >/dev/nul
    if [ $? == 1 ]
    then
        # 记录该文件
        echo ${file}>>temp.log
    fi
done
# 输出结果
cat temp.log
rm -rf temp.log