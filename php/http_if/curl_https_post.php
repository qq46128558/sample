<?php
/* 
POST请求 CURL
php利用curl实现http/https post请求
实现自定义http头
*/

//初始化
$curl = curl_init();
//设置抓取的url
curl_setopt($curl, CURLOPT_URL, 'https://tmt.hoiyee.net/common/qiniu/token');
//设置头文件的信息作为数据流输出
curl_setopt($curl, CURLOPT_HEADER, 0);
//设置获取的信息以文件流的形式返回，而不是直接输出。
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
// 设置自定义的HTTP头
$headers = array();
$headers[] = 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36';
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

// 请求HTTPS协议接口api
// 跳过证书检查
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER,0);
// 从证书中检查SSL加密算法是否存在
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST,2);

$postData=array();
curl_setopt($curl,CURLOPT_POST,1);
// 全部数据使用HTTP协议中的"POST"操作来发送。要发送文件，在文件名前面加上@前缀并使用完整路径。这个参数可以通过urlencoded后的字符串类似'para1=val1&para2=val2&...'或使用一个以字段名为键值，字段数据为值的数组。如果value是一个数组，Content-Type头将会被设置成multipart/form-data。
curl_setopt($curl, CURLOPT_POSTFIELDS, $postData);

//执行命令
$data = curl_exec($curl);
//关闭URL请求
curl_close($curl);
//显示获得的数据
var_dump($data);

