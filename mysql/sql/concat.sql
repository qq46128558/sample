
-- CONCAT(str1,str2,…)  
-- 返回结果为连接参数产生的字符串。

-- CONCAT_WS(separator,str1,str2,...)
-- CONCAT_WS() 代表 CONCAT With Separator ，是CONCAT()的特殊形式。第一个参数是其它参数的分隔符。分隔符的位置放在要连接的两个字符串之间。分隔符可以是一个字符串，也可以是其它参数。

-- MySQL中group_concat函数
-- 完整的语法如下：
-- group_concat([DISTINCT] 要连接的字段 [Order BY 排序字段 ASC/DESC],[Separator '分隔符'])

-- repeat()函数
-- 用来复制字符串,如下'ab'表示要复制的字符串，2表示复制的份数

select salarys_id , GROUP_CONCAT(detail ORDER BY id asc,',') as detail 
,GROUP_CONCAT(detailvalue ORDER BY id asc,',') as detailvalue
from tounickfund_subsalarys where salary_id='2088395000160147' group by salarys_id
