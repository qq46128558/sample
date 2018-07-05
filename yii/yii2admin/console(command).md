## 控制台命令


#### 控制台命令配置控制的命名空间
    .\console\config\main.php
        'controllerNamespace' => 'console\controllers',

#### yii2admin安装所调用的控制器
    执行这个命令: php yii install
    调用控制器:
    .\console\controllers\InstallController.php

#### 是否已安装的判断
    storage/web/install.txt 文件存在

#### 执行当前控制器内的action
    # public function actionSetWritable()
    $this->runAction('set-writable', ['interactive' => $this->interactive]);


#### 执行其他控制器的action
    # 未找到
    Yii::$app->runAction('migrate/up', ['interactive' => false]);