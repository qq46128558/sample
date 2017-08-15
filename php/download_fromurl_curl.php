<?php
$file_url='http://images.bbc.shopex123.com/images/2c/eb/3c/0fa107ebe9aae522dbbee610f921abdd0f344341.jpg';
// $save_to="/data/ftp/".basename($file_url);
$save_to='e:/tddownload/'.basename($file_url);
dlfile($file_url,$save_to);
echo '下载完成';

function dlfile($file_url, $save_to)
{
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_POST, 0);
        curl_setopt($ch,CURLOPT_URL,$file_url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $file_content = curl_exec($ch);
        curl_close($ch);
        $downloaded_file = fopen($save_to, 'w');
        fwrite($downloaded_file, $file_content);
        fclose($downloaded_file);
}