#####查看帮助
tar --help

#####基本解压
tar -zxvf `gzip_filename` -C `directory`

- -z 处理gzip类型文件
- -x 解压
- -v 显示文件处理过程
- -f 指定处理的文件(gzip_filename)
- -C 解压到directory指定目录
