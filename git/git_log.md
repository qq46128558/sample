#### 查看指定日期之后处理过的文件
    git log --after=2018-03-25 --name-only --pretty=format:''
    git log --after=2018-03-25 --name-status --pretty=format:''
    #排除空行显示出来
    git log --after=2018-03-25 --name-status --pretty=format:''|xargs -i echo {}


#### 查看指定日期之后的日志
    git log --after=2018-03-25 

#### 以一行的形式显示日志
git log --oneline

#### 查看某用户提交的文件及文件状态
git log --name-status --author=`author`

#### 查看日志带显示commit对应文件
git log --name-only

#### 查看某个文件的修改历史
git log -p `filename`

#### 查看最近2次更新内容
git log -p -2

#### 查看某用户提交的commit
git log --author=`author`

#### 查看分支合并图
git log --graph --pretty=oneline --abbrev-commit

#### ???
git log --all


