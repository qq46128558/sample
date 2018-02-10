#### 还原某个文件的指定版本
git checkout `commit-id` `filename`

#### 放弃修改, 放弃工作区的修改
git checkout -- `filename`

#### 切换分支
git checkout `branchname`

#### 创建+切换分支
git checkout -b `branchname`

#### 创建分支并关联远程分支
git checkout -b `branchname` origin/`branchname`

#### 用指定分支文件替换当前分支的该文件
git checkout `branchname` -- `filename`
