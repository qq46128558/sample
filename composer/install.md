install 命令从当前目录读取 composer.json 文件，处理了依赖关系，并把其安装到 vendor 目录下

	php composer.phar install

如果当前目录下存在 composer.lock 文件，它会从此文件读取依赖版本，而不是根据 composer.json 文件去获取依赖。这确保了该库的每个使用者都能得到相同的依赖版本。

如果没有 composer.lock 文件，composer 将在处理完依赖关系后创建它。