<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

$objPHPExcel=new PHPExcel();
$objPHPExcel->setActiveSheetIndex(0);
for($row=1;$row<=1000;$row++){
        for($col=1;$col<=30;$col++){
                $objPHPExcel->getActiveSheet()->setCellValueExplicit(toColName($col).($row),"Col:$col,Row:$row",PHPExcel_Cell_DataType::TYPE_STRING);
        }   
}
$objPHPExcel->getActiveSheet()->setTitle('Test_Sheet');
$objPHPExcel->setActiveSheetIndex(0);
$objWriter=new PHPExcel_Writer_Excel2007($objPHPExcel);
$objWriter->save('./1.xlsx');
echo 'Export excel done.';

function toColName($col){
    if (($col % 26)==0){
        $alpha=intval(($col-1)/26);
    }else{
        $alpha=intval($col/26);
    }
    $remainder=$col-($alpha*26);
    if ($alpha>0) $value=chr($alpha+64);
    if ($remainder>0) $value.=chr($remainder+64);
    return $value;
}