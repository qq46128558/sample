## curl
curl命令是一个利用URL规则在命令行下工作的文件传输工具。它支持文件的上传和下载，所以是综合传输工具，但按传统，习惯称curl为下载工具。作为一款强力工具，curl支持包括HTTP、HTTPS、ftp等众多协议，还支持POST、cookies、认证、从指定偏移处下载部分文件、用户代理字符串、限速、文件大小、进度条等特征。做网页处理流程和数据检索自动化，curl可以祝一臂之力。

##### 用curl进行认证
~~~
#使用curl选项 -u 可以完成HTTP或者FTP的认证，可以指定密码，也可以不指定密码在后续操作中输入密码
curl -u user:pwd http://man.linuxde.net
curl -u user http://man.linuxde.net
~~~

##### curl的带宽控制和下载配额
~~~
#使用--limit-rate限制curl的下载速度：
curl URL --limit-rate 50k
#使用--max-filesize指定可下载的最大文件大小：
curl URL --max-filesize bytes
#如果文件大小超出限制，命令则返回一个非0退出码，如果命令正常则返回0。
~~~

##### 用curl设置用户代理字符串
	#有些网站访问会提示只能使用IE浏览器来访问，这是因为这些网站设置了检查用户代理，可以使用curl把用户代理设置为IE，这样就可以访问了
	#-A, --user-agent STRING  Send User-Agent STRING to server (H)
	curl URL --user-agent "Mozilla/5.0"
	curl URL -A "Mozilla/5.0"

##### 用curl设置cookies
	#-b, --cookie STRING/FILE  Read cookies from STRING/FILE (H)
	#使用--cookie "COKKIES"选项来指定cookie，多个cookie使用分号分隔：
	curl http://man.linuxde.net --cookie "user=root;pass=123456"
	#将cookie另存为一个文件，使用--cookie-jar选项：
	#-c, --cookie-jar FILE  Write cookies to FILE after operation (H)
	curl URL --cookie-jar cookie_file

##### 使用curl设置参照页字符串
	# -e, --referer       Referer URL (H)
	#参照页是位于HTTP头部中的一个字符串，用来表示用户是从哪个页面到达当前页面的，如果用户点击网页A中的某个连接，那么用户就会跳转到B网页，网页B头部的参照页字符串就包含网页A的URL。
	curl --referer http://www.google.com http://man.linuxde.net

##### 断点续传
	#未测试
	#让curl自动推断出正确的续传位置使用-C -
	curl -C -`url_address`

##### 把输出写到该文件中
	#-o, --output FILE   Write to FILE instead of stdout
	#-s, --silent        Silent mode (don't output anything) 静默模式。不输出任何东西
	#curl是将下载文件输出到stdout，将进度信息输出到stderr，不显示进度信息使用
	curl http://mirrors.shopex.cn/shopex/shopex-lnmp/shopex-lnmp.repo -s -o shopex-lnmp.repo

##### HTTP POST方式传送数据
	#-X, --request COMMAND  Specify request command to use	指定什么命令
	#-H, --header LINE   Pass custom header LINE to server (H) 自定义头信息传递给服务器
	#-d, --data DATA     HTTP POST data (H)
	curl -X POST -H 'Content-Type:application/json' -d '{"activityId": "5ac321ebf8990b75fb3c7e7a","data": {"join": "+1"},"user": {"userId": "oRnBdwrRp9wGh_q-IZW8XvWjyJn4","nickName": "Peter","headImgUrl": "http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJGnPg0FD8qZ9s7iaacJJDPEOjViaARRWDXribP9P9UZ0AW1JFibFzQcIeeib9RTz0kAlFDwTFZYnnvqoQ/132"},"mobile": "","shareUserId": ""}' http://47.106.126.78/timinglottery/dev/main/join

##### 只打印响应头部信息
~~~
#通过-I或者-head可以只打印出HTTP头部信息
curl -I http://man.linuxde.net
~~~

##### 输出时包括protocol头信息
	#-i, --include       Include protocol headers in the output (H/F)
	curl http://47.106.126.78/timinglottery/dev/main/count?activityId=5ac321ebf8990b75fb3c7e7a -i
	#-I/--head	只显示请求头信息
	curl www.baidu.com -I

#####获取页面
	curl `url_address`

#####使用地址重定向
	#-L, --location      Follow redirects (H)
	curl -L `url_address`

#####查看帮助
	curl --help
