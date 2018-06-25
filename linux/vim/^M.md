

## vim 文件^M替换
脚本正确,但某台机器总是执行错误,是因为隐藏了^M

~~~
vim -b xxx.sh
:%s/^M//g
~~~

**^M: 按ctrl+v ctrl+m**
