

#### 将命令执行结果赋值给变量k(目前是最后一行赋值)
    REM CMD 中用 %i BAT中用 %%i
    REM for /f "usebackq delims==" %i in (`git status -s`) do @set comment= %i
    for /f "usebackq delims==" %%i in (`git status -s`) do @set comment= %%i    