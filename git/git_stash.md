#保存当前工作现场
git stash

#查看已保存的工作现场
git stash list

#恢复工作现场(stash内容不删除)
git stash apply

#删除工作现场
git stash drop

#恢复工作现场同时删除stash内容
git stash pop

#恢复指定stash
git stash apply stash@{<stashid>}
	