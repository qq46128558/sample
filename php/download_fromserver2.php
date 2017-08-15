<?php

// linux
// $serverfile='/data/ftp/export-1502767004.xls';
// windows
$serverfile='d:/projects/www/100009001000.pfx';

$filename=basename($serverfile);
$file=fopen($serverfile,"r");
header("Content-Type: application/octet-stream");
header("Accept-Ranges: bytes");
$filesize=filesize($serverfile);
header("Accept-Length: ".$filesize);
header("Content-Disposition: attachment; filename=".$filename);
echo fread($file,$filesize);
fclose($file);