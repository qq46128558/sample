## nginx配置: location配置方法


#### location匹配的是nginx的哪个变量？
	$request_uri
	如：http://192.168.239.136/echo?a=1&b=2&c=3#ABC
	/echo?a=1&b=2&c=3
	(这个变量等于包含一些客户端请求参数的原始URI)

#### location的匹配种类有哪些?
	格式 location [ 空格 | = | ~ | ~* | !~ | !~* ] /uri/ {}
	# 精确匹配: 相等(=)
	# 字符串匹配: 字符串匹配(空格) 匹配开头(^~)
	# 正则匹配: 区分大小写匹配(~) 不区分大小写匹配(~*) 区分大小写不匹配(!~) 不区分大小写不匹配(!~*)

#### location搜索优先级优先级如何?
	精确匹配 > 字符串匹配( 长 > 短 [ 注: ^~ 匹配则停止匹配 ]) > 正则匹配( 上 > 下 )
	# 精确匹配只能命中一个
	# 字符串匹配使用匹配最长的作为匹配结果
	# 正则匹配按照location定义的顺序进行匹配，先定义具有高优先级


	# location优先级： (location =) > (location 完整路径) > (location ^~ 路径) > (location ~,~* 正则顺序) > (location 部分起始路径) > (/)

**特别注意**： 字符串匹配优先搜索，但是只是记录下最长的匹配 ( 如果 ^~ 是最长的匹配，则会直接命中，停止搜索正则 )，然后继续搜索正则匹配，如果有正则匹配，则命中正则匹配，如果没有正则匹配，则命中最长的字符串匹配.

#### 403 Forbidden
~~~
root /var/www/html/taiping;
location /tpadmin {
	alias /var/www/html/taiping/backend/layuiadmin/start;
}
location ~ \.(ht|svn|git|env) {
	deny all;
}

则访问http://xxx/tpadmin/index.html 时返回 403 Forbidden
~~~
