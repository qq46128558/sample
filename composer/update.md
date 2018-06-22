为了获取依赖的最新版本，并且升级 composer.lock 文件，你应该使用 update 命令。

	php composer.phar update

这将解决项目的所有依赖，并将确切的版本号写入 composer.lock。

如果你只是想更新几个包，你可以像这样分别列出它们：

	php composer.phar update vendor/package vendor/package2

你还可以使用通配符进行批量更新：

	php composer.phar update vendor/*