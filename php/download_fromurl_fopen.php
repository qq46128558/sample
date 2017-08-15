<?php
$file_url='http://images.bbc.shopex123.com/images/2c/eb/3c/0fa107ebe9aae522dbbee610f921abdd0f344341.jpg';
// $save_to="/data/ftp/".basename($file_url);
$save_to="e:/tddownload/".basename($file_url);
dlfile($file_url,$save_to);
echo '下载完成';

function dlfile($file_url, $save_to)
{
        $in=    fopen($file_url, "rb");
        $out=   fopen($save_to, "wb");
        while ($chunk = fread($in,8192))
        {
                fwrite($out, $chunk, 8192);
        }
        fclose($in);
        fclose($out);
}