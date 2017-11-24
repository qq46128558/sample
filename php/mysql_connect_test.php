<?php
// mysql_connect(): The mysql extension is deprecated and will be removed in the future: use mysqli or PDO instead in 
error_reporting(E_ALL & ~E_DEPRECATED);
// error_reporting(E_ERROR);

$mysql_server_name='127.0.0.1:3306';
$mysql_username='root';
$mysql_password='root';
$mysql_database='information_schema';

$conn=mysql_connect($mysql_server_name,$mysql_username,$mysql_password) or die("[Error connecting]");
echo 'Connect succeed.';
/*
//数据库输出编码 应该与你的数据库编码保持一致
mysql_query("set names 'utf8'"); 
mysql_select_db($mysql_database);
$sql ="select * from schemata ";
$result = mysql_query($sql,$conn);
while($row=mysql_fetch_array($result)){
        echo $row['SCHEMA_NAME']."\n";
}
*/
mysql_close();