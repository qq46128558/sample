#!/bin/bash(dircolors)
#修改目录颜色
if [ ! -f ~/.dircolors ]; then sudo dircolors -p > ~/.dircolors; fi;
sed -i 's/DIR 01;34/DIR 01;33/g' ~/.dircolors
#shell进程不同,执行也无效果
#if [ -f ~/.bashrc ]; then source ~/.bashrc; fi;

#VIM配置(vimrc)
#修改vim注释颜色
if [ ! -f  ~/.vimrc ]; then sudo cp /etc/vimrc ~/.vimrc; fi;
sed -i '/hi comment ctermfg=/d' ~/.vimrc
echo "hi comment ctermfg=6">>~/.vimrc
#默认显示行号
exists=`grep "set nu" ~/.vimrc`
if [ -z "$exists" ]; then sed -i '$a\set nu' ~/.vimrc; fi;

#环境变量(profile)
if [ ! -f ~/.profile ]; then cp /etc/profile ~/.profile; fi;
sed -i '/export PS1=/d' ~/.profile
ps="export PS1='[\u\#_\A@\033[36m\w\033[0m]$'"
echo ${ps}>>~/.profile
#shell进程不同,执行也无效果
#source ~/.profile
