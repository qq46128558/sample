#提交add与modified(包括untracked)
git add .

#提交modified和deleted
git add -u

#提交所有变化(包括untracked)
git add -A

#增加修改, 将修改(git管理的是修改, 不是文件)从工作区提交到版本库的stage(暂存区)
git add <filename>
	