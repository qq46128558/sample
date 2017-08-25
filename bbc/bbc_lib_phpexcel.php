<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

/*PHPExcel应用简单示例*/
var_dump(sample());

function sample(){
	$db=app::get('base')->database();
	$sql="select * from base_apps";
	$rows=$db->executeQuery($sql)->fetchAll();
	if (count($rows)>0){
		$file='d:/base_apps.xlsx';
		export_excel($rows,'应用',$file);
	}
	return $file;
}

//序号转Excel列名
function toColName($col){
        $alpha=intval($col/27);
        $remainder=$col-($alpha*26);
        if ($alpha>0) $value=chr($alpha+64);
        if ($remainder>0) $value.=chr($remainder+64);
        return $value; 
}

//$rows 传入查询数据
//$title sheet标题
//写入文件 
function export_excel($rows,$title,$file){
        //创建excel类   
        $objPHPExcel=new PHPExcel();
        $num=1;$index=1;
        //创建标题
        $objPHPExcel->setActiveSheetIndex(0);
        foreach($rows[0] as $k=>$v){
                $objPHPExcel->getActiveSheet()
                        ->setCellValue(toColName($index++).$num,$k);
        }
        //写入内容
        foreach($rows as $k=>$v){
                $num+=1;$index=1;
                foreach ($v as $k2=>$v2){
                        $objPHPExcel->getActiveSheet()->setCellValueExplicit(toColName($index++).$num,$v2,PHPExcel_Cell_DataType::TYPE_STRING);
                }
        }
        $objPHPExcel->getActiveSheet()->setTitle($title);
        $objPHPExcel->setActiveSheetIndex(0);
        $objWriter=new PHPExcel_Writer_Excel2007($objPHPExcel);
        $objWriter->save($file);

}
