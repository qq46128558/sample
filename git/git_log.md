
####以一行的形式显示日志
git log --oneline

####查看某用户提交的文件及文件状态
git log --name-status --author=`author`

####查看日志带显示commit对应文件
git log --name-only

####查看某个文件的修改历史
git log -p `filename`

####查看最近2次更新内容
git log -p -2

####查看某用户提交的commit
git log --author=`author`

####查看分支合并图
git log --graph --pretty=oneline --abbrev-commit

####???
git log --all


