## 以树形结构查看文件
    - 配置alias: alias tt='tree -apughDC'
    
### 常用
    tree -apughDCL 2 
    tree -apughDC `路径`d

#### 基本使用
    tree `路径`

#### 只显示目录
    #List directories only
    tree -d `路径`

#### 显示所有文件
    #All files are listed
    tree -a `路径`

#### 显示每个文件的全路径
    #Print the full path prefix for each file
    tree -f `路径`

#### 显示带上颜色
    #Turn colorization on always
    tree -C `路径`

#### 不显示缩进线
    #Don't print indentation lines
    tree -i `路径`

#### 显示文件大小
    #Print the size in a more human readable way
    tree -h `路径`

#### 显示最后修改日期
    #Print the date of last modification or (-c) status change
    tree -D `路径`

#### 显示权限/用户/组
    #-p Print the protections for each file.
    #-u Displays file owner or UID number
    #-g Displays file group owner or GID number
    tree -pug `路径`

#### 显示层数

    #-L level      Descend only level directories deep.
    tree -L 2 `路径`