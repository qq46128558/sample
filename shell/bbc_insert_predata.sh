#!/bin/bash
echo -e "\033[33;1m准备将预置脚本写入数据库......\033[0m" 
echo -n -e "请输入执行的数据库名(如bbc):"; 
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

#此处加入你需要预置的脚本
printf "\n准备写入邮件短信消息模板数据......";
#前缀相同
sqlbegin=" INSERT INTO \`system_messenger_systmpl\` (\`tmpl_name\`, \`content\`, \`modified_time\`, \`active\`) select "
sqlend=" from dual where not exists (select 1 from  \`system_messenger_systmpl\` where tmpl_name="
#内容不同
sqlvalue1="'messenger:system_messenger_notification/tounick_messenger1'"
sqlvalue="'messenger:system_messenger_notification/tounick_messenger1', '『尊敬的 <{\$mobile}> 用户，您的企业认证已通过。因为该企业是首次在平台认证，您的账号已与“广州淘力”企业绑定管理员关系，如若需要解绑，请先联系客服。』', null, 1"
#合并成一条sql语句
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_notification/tounick_messenger2'"
sqlvalue="'messenger:system_messenger_notification/tounick_messenger2', '『尊敬的 <{\$mobile}> 用户，您的企业认证未能通过。请补充或修改后再次申请，谢谢。 补充说明：<{\$remark}>』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_notification/tounick_messenger3'"
sqlvalue="'messenger:system_messenger_notification/tounick_messenger3', '『尊敬的 <{\$mobile}> 用户，您的淘力云资金账户认证已通过。』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_notification/tounick_messenger4'"
sqlvalue="'messenger:system_messenger_notification/tounick_messenger4', '『尊敬的 <{\$mobile}> 用户，您的淘力云资金账户认证未能通过。』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger5'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger5', '『抱歉，您的<{\$tradename}>交易失败，流水号<{\$flow}>。资金将原路退回您的结算账户内』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger7'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger7', '『尊敬的用户，您有一份来自\"<{\$company_name}>\"未确认的<{\$month}>月应收工资确认表，请尽快操作并审核。』<{\$oplink}>', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger10'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger10', '『尊敬的用户，您已确认\"<{\$company_name}>\"的<{\$month}>月应收工资结算表，请及时上传相关人员工资结算表单。』<{\$oplink}>', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger11'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger11', '『尊敬的用户，\"<{\$company_name}>\"已完成<{\$month}>月工资结算，如有需补发工资的，请下载「应补发员工表」，从线下补发给相关员工。需补发的工资将一并汇入您的账户余额。请注意查收。』<{\$oplink}>', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_notification/tounick_messenger12'"
sqlvalue="'messenger:system_messenger_notification/tounick_messenger12', '『尊敬的用户，\"<{\$company_name}>\"的<{\$month}>月工资结算表相关联的人员工资结算表，贵司上传后有员工新反馈，请及时查看』<{\$oplink}>', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger15'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger15', '『尊敬的<{\$name}>，您已成功入职<{\$company_name}>。但因您尚未注册淘力网账户，您的企业工资结算将会在此平台上进行。请及时进入www.tounick.com/costumer或微信搜索「淘力」公众号进行账户激活，否则有可能无法及时收到工资款项』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger16'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger16', '『尊敬的用户，您的合作企业<{\$s_company_name}>驳回了<{\$month}>月<\$b_company_name}>工资结算表，驳回理由如下：未按合同约定填写应有管理费用。请及时修改后重新上传该表发送至合作企业』<{\$oplink}>', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger18'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger18', '『尊敬的用户，您有一份合作企业\"<{\$s_company_name}>\"需支付的工资结算单 - <{\$month}>月<{\$b_company_name}>』<{\$oplink}>', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger22'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger22', '『尊敬的用户，您申请的<{\$money}>元<{\$company_name}>的预付工资款项已成功发送。但因银行结算到账时间可能有延期的原因，请在1-2天后及时查看您的账户余额』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger23'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger23', '『尊敬的用户，因为您成功入职<{\$company_name}>公司的 <{\$position}>岗位，可获取<{\$money}>元奖励金。因银行结算到账时间可能有延期的原因，请在1-2天后及时查看您的账户余额』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_sms/tounick_messenger24'"
sqlvalue="'messenger:system_messenger_sms/tounick_messenger24', '『尊敬的用户，因为您推荐的<{name}>成功入职了<{\$company_name}>公司的<{\$position}>岗位，成功成为猎头/猎手，可获取<{\$money}>元奖励金。因银行结算到账时间可能有延期的原因，请在1-2天后及时查看您的账户余额』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_notification/tounick_messenger26'"
sqlvalue="'messenger:system_messenger_notification/tounick_messenger26', '『尊敬的<{\$mobile}>用户，您的淘力云账户已开通。您填写的公帐<{\$bank}>银行 尾号为<{\$bankid}>已绑定为企业对公账户，可用于提现。如若需要解绑，请先联系客服。』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"

sqlvalue1="'messenger:system_messenger_notification/tounick_messenger29'"
sqlvalue="'messenger:system_messenger_notification/tounick_messenger29', '『由于银行结算规定，需要在次日工作日下午五点才可成功到账您的银行卡。敬请留意，谢谢理解』', null, 1"
sql=${sql}${sqlbegin}${sqlvalue}${sqlend}${sqlvalue1}");"


mysql -h localhost -u root -p${password} -D ${database} -e"${sql}" >>insert_predata.sh.log 2>&1
CheckStatus;

unset password;
unset database;
rm -f insert_predata.sh.log

