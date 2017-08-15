<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

require_once __DIR__.'/../php/excel.php'; 

$data = new Spreadsheet_Excel_Reader();  
$data->setOutputEncoding('utf-8');
$data->read(__DIR__.'/import-1502767004.xls');  
error_reporting(E_ALL ^ E_NOTICE);  

$model=app::get('system')->model('adminlog');
$sheets=$data->sheets[0];
$cells=$sheets['cells'];

try{
	db::connection()->beginTransaction();
	//循环表格,根据实际表情况处理赋值
	for ($i=2; $i<=$sheets['numRows'];$i++){
		for($j=1;$j<=$sheets['numCols'];$j++){
			$name=$cells[1][$j];
			if ($cells[$i][$j]) $value[$name]=$cells[$i][$j];
		}
		$result=$model->insert($value);
		$value=array();
		if (!$result) {
			db::connection()->rollback();
			echo '导入失败.';
			exit();
		}
	}
	db::connection()->commit();
	echo '导入成功.';
} catch(Exception $e){
	db::connection()->rollback();
	echo '导入失败:'.$e->getMessage();
}

/* Excel取值示例
echo "<table border=1>";  
for ($i = 1; $i <= $data->sheets[0]['numRows']; $i++) {   
echo "<tr>";  
for ($j = 1; $j <= $data->sheets[0]['numCols']; $j++) {   
echo "<td>".$data->sheets[0]['cells'][$i][$j]."</td>";  
}  
echo "</tr>";  
}  
echo "</table>";
*/
