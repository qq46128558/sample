#### 查找filename指定文件
find . -name `filename`

#### 按文件属主查找
find . -user `username`

#### 按文件属组查找
find . -group `groupname`

#### 查找1分钟以内修改过的文件
    find . -mmin -1

#### 查找15天以前修改过的文件
    find . -mtime +15

#### 查找文件类型
- 查找块设备
	~~~
	find . -type b
	~~~
- 查找目录
	~~~
	find . -type d
	~~~
- 查找字符设备
    ~~~
    find . -type c
    ~~~
- 查找管道
    ~~~
    find . -type p
    ~~~
- 查找符号链接
    ~~~
    find . -type l
    ~~~
- 查找普通文件
    ~~~
    find . -type f
    ~~~

#### 配合正则查找大写字母开头的普通文件
    find . -name "[A-Z]*"

#### 查找大小为0的文件或空目录
    find . -empty

