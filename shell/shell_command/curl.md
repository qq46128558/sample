## curl
curl命令是一个利用URL规则在命令行下工作的文件传输工具。它支持文件的上传和下载，所以是综合传输工具，但按传统，习惯称curl为下载工具。作为一款强力工具，curl支持包括HTTP、HTTPS、ftp等众多协议，还支持POST、cookies、认证、从指定偏移处下载部分文件、用户代理字符串、限速、文件大小、进度条等特征。做网页处理流程和数据检索自动化，curl可以祝一臂之力。


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

##### 输出时包括protocol头信息
	#-i, --include       Include protocol headers in the output (H/F)
	curl http://47.106.126.78/timinglottery/dev/main/count?activityId=5ac321ebf8990b75fb3c7e7a -i

#####获取页面
	curl `url_address`

#####使用地址重定向
	#-L, --location      Follow redirects (H)
	curl -L `url_address`

#####查看帮助
	curl --help
