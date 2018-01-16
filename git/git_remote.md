#关联, 把本地仓库与远程仓库关联, origin就是远程仓库的名字, git的默认叫法, 建议不要改
git remote add origin git@github.com:xxx/xxx.git

#取消关联, 取消本地仓库与远程仓库的关联
git remote remove origin

#查看远程仓库详细信息
git remote -v