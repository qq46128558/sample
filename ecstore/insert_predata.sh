#!/bin/bash
echo -e "\033[33;1m准备将预置脚本写入数据库......\033[0m" 
echo -n -e "请输入执行的数据库名(如ecstore):"; 
read database;

#此段代码为输入密码显示*号.
echo -n "请输入Mysql的root密码:";
while : ;do  
    char=`  
        stty cbreak -echo  
        dd if=/dev/tty bs=1 count=1 2>/dev/null  
        stty -cbreak echo  
    `  
    if [ "$char" =  "" ];then  
        break  
    fi  
    password="$password$char"  
    echo -n "*"  
done

#检查是否执行成功
function CheckStatus(){
if [ $? == 0 ]
then
echo -e "[\033[32;1m成功\033[0m]";
else 
echo -e "[\033[31;1m失败\033[0m]";
unset password;
unset database;
echo -e "\033[31;1m失败日志记录如下:\033[0m"
cat insert_predata.sh.log
rm -f insert_predata.sh.log
exit;
fi
}

#预置脚本写法可参考此处
printf "\n准备写入U8订单同步定时任务数据......";
mysql -h localhost -u root -p${password} -D ${database} -e"INSERT INTO \`sdb_base_crontab\` (id,description,enabled,\`schedule\`,last,app_id,class,type) select 'b2c_tasks_sosynchronization', 'U8定时任务_订单同步', 'false', '*/5 * * * *', NULL, 'b2c', 'b2c_tasks_sosynchronization', 'custom' from dual where not exists (select 1 from \`sdb_base_crontab\` where id='b2c_tasks_sosynchronization');" >>insert_predata.sh.log 2>&1
CheckStatus;

#此处加入你需要预置的脚本

unset password;
unset database;
rm -f insert_predata.sh.log
