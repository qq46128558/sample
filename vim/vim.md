
## 命令

**插件/usr/share/vim/vim74/plugin/*.vim 中用了很多vim的命令,可研究学习**

#### 查看插件列表
    :scriptnames
    
#### 查看详细的版本信息
    :version
    #可以看到不支持python2(-python),及支持python3(+python3)
    #debugger.vim插件使用的是python2

#### echo
~~~
#都需要加上:
#安装目录
echo $VIM
#运行目录
echo $VIMRUNTIME
#是否支持python2
echo has('python')
#是否支持python3
echo has('python3')
~~~

#### python
~~~
#vim python2支持,可执行python命令,如:
python import sys;print(sys.version_info)
#或简写成py
py import sys;print(sys.version_info)
~~~

## 其他

#### 切换vim使用的版本
    update-alternatives --config vim

