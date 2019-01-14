#### 配置用户名与邮箱
git config --global user.name `name`

git config --global user.email `email`

#### 配置git显示颜色, 让命令的输出看来更醒目
git config --global color.ui true

#### 我的常用别名
git config --global alias.lg "log --graph --date=local --pretty=format:'%Cred%h%Creset %C(reset)%d%C(bold yellow)[%an] %Creset%Cgreen[%cd] %Cblue[P:%p]%Creset %s'"

git config --global alias.lg2 "log --name-status --graph --date=local --pretty=format:'%Cred%h%Creset %C(reset)%d%C(bold yellow)[%an] %Creset%Cgreen[%cd] %Cblue[P:%p]%Creset %s'"

git config --global alias.rlg "reflog --name-status --date=local"


#### 生成SSH公钥
ssh-keygen -t rsa -C "youremail@example.com"


#### 查看配置信息
git config --global --list

#### 查看指定项配置信息
git config xxxxxx

#### 在CMD终端中设置在全局Git环境中，长期存储密码
	
	# push一次后,会自动保存密码至/root/.git-credentials
	git config --global credential.helper store

#### 其他设置密码方式

	# 记住密码（默认15分钟）：
	git config --global credential.helper cache
	# 自定义存储时间
	git config credential.helper 'cache --timeout=3600'
	
#### 使用HTTPS协议，有一种简单粗暴的方式是在远程地址中带上密码
	
	git remote set-url origin http://yourname:password@bitbucket.org/yourname/project.git
	
