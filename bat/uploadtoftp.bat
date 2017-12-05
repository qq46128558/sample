@echo off
set commandfile=command.ftp
set logfile=upload.log

REM 创建ftp命令文件
REM 连接ftp服务器
echo open 192.168.239.138>%commandfile%
echo user ec_ftp ec_ftp@123>>%commandfile%
REM 设置为二进制传输
echo binary>>%commandfile%
REM 更改本地路径(注意最后不要再加 / 符号)
echo lcd d:/projects/www/sd_tounick>>%commandfile%
REM 更改远程目录(按需)
REM echo cd /data/httpd/b2b2c
REM 上传文件
echo mput custom/base/lib/tounickpub.php>>%commandfile%
echo quit>>%commandfile%

REM 记录执行时间
REM 使用for将命令的执行结果赋给变量
for /f "usebackq" %%i in (`date /t`) do @set a=%%i
for /f "usebackq" %%i in (`time /t`) do @set b=%%i
REM 创建日志文件
echo [%a% %b%]>>%logfile%

REM 执行ftp
REM -n 禁止在初始连接时自动登录
REM -i 关闭多文件传输过程中的交互式提示
ftp -n -i <%commandfile% >>%logfile%
del %commandfile%
