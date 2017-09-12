npm install
<!-- 根据package.json进行npm依赖包的安装 -->

npm outdated
<!-- 检查包的版本 -->

npm install -g bower
<!-- 最新版的bootstrap 4跟廖老师写好的html好像有点不兼容，显示有问题。可以用bower安装对应版本bootstrap 3.3.7 -->

bower install bootstrap#3.3.7
<!-- bower是一个css/js/fonts这些东西的包管理器 -->

<!-- 注意，很多文章会让你用命令npm install -g mocha把mocha安装到全局module中。这是不需要的。尽量不要安装全局模块，因为全局模块会影响到所有Node.js的工程。 -->
npm install -g mocha