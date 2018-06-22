require 命令增加新的依赖包到当前目录的 composer.json 文件中

	php composer.phar require

在添加或改变依赖时， 修改后的依赖关系将被安装或者更新。

如果你不希望通过交互来指定依赖包，你可以在这条令中直接指明依赖包。

	php composer.phar require vendor/package:2.* vendor/package2:dev-master


#### 安装依赖包(如php dotenv)
	php composer.phar require vlucas/phpdotenv

