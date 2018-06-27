
#### 替换字符串
    REM 将显示 welcome to CMD world! 即用w替换了变量a中的b。
    set a=belcome to CMD borld! 
    set temp=%a:b=w% 
    echo %temp%

#### 截取字符串
    REM 将显示super 即显示了变量a的第0位至第5位中包括的所有元素。 
    set a=superhero 
    set temp=%a:~0,5% 
    echo %temp% 