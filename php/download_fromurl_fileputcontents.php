<?php
$file_url='http://images.bbc.shopex123.com/images/2c/eb/3c/0fa107ebe9aae522dbbee610f921abdd0f344341.jpg';
// windows
$save_to="e:/tddownload/".basename($file_url);
// linux
// $save_to="/data/ftp/".basename($file_url);

dlfile($file_url,$save_to);
echo 'Done.';

function dlfile($file_url, $save_to)
{
        $content = file_get_contents($file_url);
        file_put_contents($save_to, $content);
}