#### 拉取修改
git pull

#### 合并两个不同的仓库
    # refusing to merge unrelated histories
    git pull origin master --allow-unrelated-histories
    # origin 远程名 
    # master 本地分支
    # 应用场景
    # 带一个readme.md的远程空仓 与 初始init后的仓, 关联后拉取代码, 需要先合并
