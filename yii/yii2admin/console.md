## 控制台目录

#### 配置文件
    console\config\*

#### 控制台控制器(可配置)
    console\controllers\*

#### 迁移的脚本文件
    console\migrations\*


#### 配置console控制器的命名空间
    console\config\main.php
        'controllerNamespace' => 'console\controllers',

#### 配置console控制器名称映射
    console\config\main.php
        'controllerMap' => [
            'migrate' => [
                'class' => 'e282486518\migration\ConsoleController',
            ],
        ],


