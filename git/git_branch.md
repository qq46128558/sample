#### 查看分支
git branch

#### 创建分支
git branch `branchname`

#### 删除分支
git branch -d `branchname`

#### 关联分支, 创建本地分支和远程分支的链接
git branch --set-upstream `branchname` origin/`branchname`

#### 将当前分支与远程分支关联
    git branch --set-upstream-to origin/master
    origin 远程名
    master 远程分支

#### 查看全部分支(含远程分支)
git branch -a

#### 查看远程分支
git branch -r

#### 查看分支的commit-id以及显示name of upstream
git branch -vv

