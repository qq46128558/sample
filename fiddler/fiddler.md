# fiddler

[fiddler抓包工具总结](https://www.cnblogs.com/yyhh/p/5140852.html "https://www.cnblogs.com/yyhh/p/5140852.html")

## 简介

- Fiddler想要抓到数据包，要确保Capture Traffic是开启(F12)
- 字段说明
  - #: 抓取HTTP Request的顺序，从1开始，以此递增
  - Result: HTTP状态码
  - Protocol: 请求使用的协议，如HTTP/HTTPS/FTP等
  - Host: 请求地址的主机名
  - Url: 请求资源的位置
  - Body: 该请求的大小
  - Caching: 请求的缓存过期时间或者缓存控制值
  - Content-Type: 请求响应的类型
  - Process: 发送此请求的进程：进程ID
  - Comments: 允许用户为此回话添加备注
  - Custom: 允许用户设置自定义值
- Statistics 请求的性能数据分析
- Inspectors 查看数据内容
  - 上半部分是请求的内容，下半部分是响应的内容
- AutoResponder 允许拦截指定规则的请求
  - AutoResponder允许你拦截指定规则的求情，并返回本地资源或Fiddler资源，从而代替服务器响应
  - 字符串匹配（默认）：只要包含指定字符串（不区分大小写），全部认为是匹配: baidu
  - 正则表达式匹配：以“regex:”开头，使用正则表达式来匹配，这个是区分大小写的
- Composer 自定义请求发送服务器
- Filters 请求过滤规则: 通过过滤规则来过滤掉那些不想看到的请求
- Timeline 请求响应时间

## Fiddler 设置解密HTTPS的网络数据

大概原理就是在浏览器面前Fiddler伪装成一个HTTPS服务器，而在真正的HTTPS服务器面前Fiddler又装成浏览器，从而实现解密HTTPS数据包的目的

> tools>options>https>decrypt https traffic

## Fiddler 抓取Iphone / Android数据包

移动端的数据包，都是要走wifi出去，所以我们可以把自己的电脑`开启热点`，将手机连上电脑

1. tools>options>connections>fiddler listens on port & allow remote computers to connect  
2. 手机连接pc的wifi，并设置代理ip(fiddler)与port
3. 手机网页访问代理ip和端口，下载fiddler证书（fiddlerroot certificate）

## Fiddler 内置命令与断点

- Fiddler还有一个藏的很深的命令框: alt+q

|命令|对应请求项|介绍|示例
|-|-|-|-
|help|-|帮助|help
|?|all|问号后边跟一个字符串，可以匹配出包含这个字符串的请求|?google
|>|body|大于号后面跟一个数字，可以匹配出请求大小，大于这个数字请求|>1000
|<|body|小于号跟大于号相反，匹配出请求大小，小于这个数字的请求|<100
|=|result|等于号后面跟数字，可以匹配HTTP返回码|=200
|@|host|@后面跟Host，可以匹配域名|@www.baidu.com
|select|content-type|select后面跟响应类型，可以匹配到相关的类型|select image
|cls|all|清空当前所有请求|cls
|dump|all|将所有请求打包成saz压缩包，保存到“我的文档\Fiddler2\Captures”目录下
|start|all|开始监听请求|start
|stop|all|停止监听请求|stop

- FIddler断点功能就是将请求截获下来，但是不发送，这个时候你可以干很多事情，比如说，把包改了，再发送给服务器

### 断点命令

|命令|对应请求项|介绍|示例
|-|-|-|-
|bpafter|all|bpafter后边跟一个字符串，表示中断所有包含该字符串的请求|bpafter baidu（输入bpafter解除断点）
|bpu|all|跟bpafter差不多，只不过这个是收到请求了，中断响应|bpu baidu（输入bpu解除断点）
|bps|result|后面跟状态吗，表示中断所有是这个状态码的请求|bps 200（输入bps解除断点）
|bpv/bpm|http方法|只中断HTTP方法的命令，HTTP方法如POST、GET|bpv get（输入bpv解除断点）
|g/go|all|放行所有中断下来的请求|g

### 断点位置

fiddler窗口左下角，allprocesses与number of sessions之间

> 点一下截获全部请求  
> 点两下截获全部请求响应  
> 点三下解除断点设置