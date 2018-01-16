#配置用户名与邮箱
git config --global user.name "<name>"
git config --global user.email "<email>"

#配置git显示颜色, 让命令的输出看来更醒目
git config --global color.ui true

#我的常用别名
git config --global alias.lg "log --graph --date=local --pretty=format:'%Cred%h%Creset %C(reset)%d%C(bold yellow)[%an] %Creset%Cgreen[%cd] %Cblue[P:%p]%Creset %s'"

git config --global alias.lg2 "log --name-status --graph --date=local --pretty=format:'%Cred%h%Creset %C(reset)%d%C(bold yellow)[%an] %Creset%Cgreen[%cd] %Cblue[P:%p]%Creset %s'"

git config --global alias.rlg "reflog --name-status --date=local"
