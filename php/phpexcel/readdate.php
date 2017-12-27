<a href="https://www.cnblogs.com/cocowool/p/6074430.html">参考资料</a>

<?php
require_once '../../vendor/phpexcel/Classes/PHPExcel.php';
require_once '../../vendor/phpexcel/Classes/PHPExcel/IOFactory.php';
require_once '../../vendor/phpexcel/Classes/PHPExcel/Shared/Date.php';

// PHPExcel 读取Excel单元格内容为时间格式
// 读出的时间是天数
// excel 的日期是从 1900-01-01 开始计算的（php 是从 1970-01-01）
// 两者间有一个天数差 25569
// 时间是格林威治时间
// 所以有
$d = 25569;
$t = 24 * 60 * 60;

$filename='datesample.xlsx';
$objReader=PHPExcel_IOFactory::createReaderForFile($filename);
// 如果打开了setReadDataOnly这个选项，则getFormattedValue函数将总是返回数值
// $objReader->setReadDataOnly(true);
$objPHPExcel=$objReader->load($filename);
$data['sheetsinfo']=$objReader->listWorksheetInfo($filename);
// var_dump($data);
$objWriter='';

$objPHPExcel->setActiveSheetIndex(0);
$worksheet=$objPHPExcel->getActiveSheet();
$columnCount=PHPExcel_Cell::columnIndexFromString($worksheet->getHighestColumn());
// var_dump($columnCount);
$rowCount=$worksheet->getHighestRow();

echo "<table>";
for ($row=2;$row<=$rowCount;$row++){
    $cell=$worksheet->getCellByColumnAndRow(0,$row);
    $cellstyleformat=$worksheet->getStyle($cell->getCoordinate())->getNumberFormat();
    // 格式化代码
    $formatcode=$cellstyleformat->getFormatCode();
   
    // 读取格式化之后的数据，可以看到部分格式没有能够正常显示，是因为PHPExcel预置的日期格式没有匹配到，导致按照数值进行显示
    $f_value=$cell->getFormattedValue();
    // 直接获取数值
    $value=$cell->getValue();
    // 转化为PHP格式的时间
    $p_value=PHPExcel_Shared_Date::ExcelToPHP($value);

    if ($formatcode!='General'){
        $gm_value=gmdate('Y-m-d H:i:s', ($value - $d) * $t);
    }else{
        $gm_value=date('Y-m-d H:i:s',strtotime($value));
    }

    echo "<tr><td>$row</td><td>$f_value</td><td>$value</td><td>$formatcode</td><td>$p_value</td><td>$gm_value</td></tr>";
}
echo "</table>";
