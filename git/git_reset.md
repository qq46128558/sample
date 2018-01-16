#将远程仓某分支回滚到上一版本
git reset --hard HEAD^
git push origin master -f

#还原恢复内容到最新版本
git reset --hard HEAD

#还原恢复, 将工作区还原成版本库里的指定版本
git reset --hard <commit-id>

#放弃修改, 放弃暂存区的修改
git reset HEAD <filename>
	
