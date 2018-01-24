???
####git rebase -i HEAD~`numberofcommit`

将`branch`分支的所有改变添加到当前分支(类似git merge)

让当前分支历史看起来像没有经过任何合并一样

当前分支所修改的会放在后面

将当前分支里的每个提交`commit`取消掉,并且把它们临时保存为补丁`patch`(这些补丁放到".git/rebase"目录中),然后把当前分支更新为最新的`branch`分支,最后把保存的这些补丁应用到当前分支上 

####git rebase `branch`

rebase过程冲突,处理好后继续
####git rebase -continue

rebase过程冲突,放弃rebase
####git rebase -abort

rebase过程冲突,用`branch`分支取代当前分支的
####git rebase -skip
