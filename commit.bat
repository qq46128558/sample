
@echo off
REM 普通修改后快捷更新到Git(未完善)

REM CMD 中用 %i
REM for /f "usebackq delims==" %i in (`git status -s`) do @set comment= %i
REM 将命令执行结果赋值给变量(目前只有最后一行)<<<<<
for /f "usebackq delims==" %%i in (`git status -s`) do @set comment= %%i
REM 字符串替换 ?=>空白
set comment=%comment:?=%
git add -A
if %errorlevel% EQU 0 (
    git commit -m "%comment%"
)


