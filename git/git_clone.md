####克隆远程仓的指定分支
git clone -b `branch` git@github.com:`account`/`project`.git

####克隆远程仓库, 但不checkout (用于处理将内容放到非空目录)
git clone --no-checkout git@github.com:`account`/`project`.git `folder`
