####提交add与modified(包括untracked)
git add .

#####提交modified和deleted
git add -u

#####提交所有变化(包括untracked)
git add -A

#####增加修改, 将修改(git管理的是修改, 不是文件)从工作区提交到版本库的stage(暂存区)
git add <filename>

#####将文件修改分段提交
git add -p `filename`

- y - stage this hunk
- n - do not stage this hunk
- q - quit; do not stage this hunk or any of the remaining ones
- a - stage this hunk and all later hunks in the file
- d - do not stage this hunk or any of the later hunks in the file
- g - select a hunk to go to
- / - search for a hunk matching the given regex
- j - leave this hunk undecided, see next undecided hunk
- J - leave this hunk undecided, see next hunk
- k - leave this hunk undecided, see previous undecided hunk
- K - leave this hunk undecided, see previous hunk
- s - split the current hunk into smaller hunks
- e - manually edit the current hunk
- ? - print help
