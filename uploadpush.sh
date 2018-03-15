#普通修改后快捷更新到Git
result=`git status -s`
git add -A

if [ $? == 0 ]; then
	git commit -m "Sample code improved:${result}"
fi

if [ $? == 0 ]; then
	git push origin master
fi


