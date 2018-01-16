#还原某个文件的指定版本
git checkout <commit-id> <filename>

#放弃修改, 放弃工作区的修改
git checkout -- <filename>

#切换分支
git checkout <branchname>

#创建+切换分支
git checkout -b <branchname>

#创建并关联分支, 在本地创建和远程分支对应的分支，使用: (前提是知道远程仓库有dev分支)
git checkout -b <branchname> origin/<branchname>


