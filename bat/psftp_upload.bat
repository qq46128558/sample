@echo off
set commandfile=command.ftp
set logfile=upload.log

REM 创建ftp命令文件
REM 没有区分二进制传输?
REM 更改本地路径(注意最后不要再加 / 符号)
echo lcd d:/projects/www/sd_tounick/custom/base/lib>>%commandfile%
REM 更改远程目录
echo cd /data/httpd/b2b2c/custom/base/lib>>%commandfile%
REM 上传文件
echo mput tounickpub.php>>%commandfile%
echo quit>>%commandfile%

REM 记录执行时间
REM 使用for将命令的执行结果赋给变量
for /f "usebackq" %%i in (`date /t`) do @set a=%%i
for /f "usebackq" %%i in (`time /t`) do @set b=%%i
REM 创建日志文件
echo [%a% %b%]>>%logfile%

REM 需要安装PuTTY
"c:\Program Files\PuTTY\psftp.exe" 192.168.239.138 -l root -pw 123456 < %commandfile% >%logfile% 
del %commandfile%
