<?php
var_dump($_GET);
$code=$_GET['code'];
if ($code){
	file_put_contents(__DIR__.'/jd_code_info.log',"\n".date('Y-m-d H:i:s',time())."\n",FILE_APPEND);
	file_put_contents(__DIR__.'/jd_code_info.log',$code,FILE_APPEND);
}
