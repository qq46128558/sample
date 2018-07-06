## 数据迁移

#### 数据库迁移脚本位置
    console/migrations

#### 查看迁移的命令
    php yii help migrate
    # 如报错: exec() has been disabled for security reasons
    # 需要删除php.ini中的disable_funciton里面的值exec

#### 创建一个新的迁移(其实就是建表)
    php yii migrate/create <name>
    # 如上命令将会在 @app/migrations 目录下创建一个新的名为mXXXXXX_XXXXXX_name.php 的 PHP 类文件
    # 在此文件中写建表代码即可(参考源码的写法)
