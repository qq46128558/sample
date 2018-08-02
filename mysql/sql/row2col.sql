

-- 淘力网项目,工资扩展项行转列
set @salary_id=2088395000160147 ;

set @str='';
SET @sql_main=''; 
-- 利用mysql的字符串转换函数CONVERT将参数格式化为char类型,可解决concat中文乱码
SELECT @str:=CONCAT(@str,'max(case when detail=\'',convert(detail,CHAR),'\' then detailvalue else \'\' end) AS `',CONVERT(detail,CHAR),'`,') as aa into @sql_main FROM (SELECT distinct detail FROM tounickfund_subsalarys where salary_id=@salary_id ) A order by length(aa) desc limit 1; 

SET @sql_full=CONCAT('SELECT b.rowno as `序号`,b.username as `姓名`,b.identity as `身份证号码`,b.actualtotal as `实发工资`, ',LEFT(@sql_main,char_length(@sql_main)-1),' FROM tounickfund_subsalarys a left join tounickfund_staffsalarys b on a.salarys_id=b.id where a.salary_id=',@salary_id,' group by b.rowno order by b.rowno'); 

PREPARE stmt FROM @sql_full; 
EXECUTE stmt ; 
deallocate prepare stmt;







-- 原始行转列示例参考
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` varchar(255) DEFAULT NULL,
  `score` double DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

INSERT INTO `score` VALUES ('1', 'math', '90', '1');
INSERT INTO `score` VALUES ('2', 'english', '90', '1');
INSERT INTO `score` VALUES ('3', 'computer', '80', '1');
INSERT INTO `score` VALUES ('4', 'sports', '90', '1');
INSERT INTO `score` VALUES ('5', 'math', '80', '2');
INSERT INTO `score` VALUES ('6', 'english', '85', '2');
INSERT INTO `score` VALUES ('7', 'computer', '100', '2');


SET @str=''; 
SET @sql_main=''; 
-- 拼接sum(if)字符串
SELECT @str:=CONCAT(@str,'SUM(IF(class=\'',class,'\'',',score,0)) AS ',class,',') as aa into @sql_main FROM (SELECT DISTINCT class FROM score) A order by length(aa) desc limit 1; 
-- 拼接整条查询语句
SET @sql_full=CONCAT('SELECT ifnull(score.userid,\'total\') as user,',LEFT(@sql_main,char_length(@sql_main)-1),' ,SUM(score) AS TOTAL FROM score GROUP BY userid WITH ROLLUP'); 

select @str;
select @sql_main;
select @sql_full;

PREPARE stmt FROM @sql_full; 
-- 执行语句
EXECUTE stmt ; 
deallocate prepare stmt;

-- SELECT ifnull(score.userid,'total') as user,SUM(IF(class='math',score,0)) AS math,SUM(IF(class='english',score,0)) AS english,SUM(IF(class='computer',score,0)) AS computer,SUM(IF(class='sports',score,0)) AS sports ,SUM(score) AS TOTAL FROM score GROUP BY userid WITH ROLLUP




