#普通修改后快捷更新到Git
result=`git status -s|sed 's/??/ A/g'`
git add -A

if [ $? == 0 ]; then
	git commit -m "Sample code improved:${result}"
fi

function nopush(){
if [ $? == 0 ]; then
	git push origin master
fi
}


