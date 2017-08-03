<?php
//Unicode解码函数
function replace_unicode_escape_sequence($match) {
    return mb_convert_encoding(pack('H*', $match[1]), 'UTF-8', 'UCS-2BE');
}

function unicode_decode($str) {
 return preg_replace_callback('/\\\u([0-9a-f]{4})/i', 'replace_unicode_escape_sequence', $str); 
}

var_dump(unicode_decode("\\u4e0a\\u6d77\\u690d\\u7530\\u5229\\u679d\\u8d38\\u6613\\u6709\\u9650\\u516c\\u53f8"));
//D:\Projects\WWW\sample\php\unicode.php:11:string '上海植田利枝贸易有限公司' (length=36)