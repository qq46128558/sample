## Yii 控制台命令

#### 配置文件
    config/console.php
    #主要配置
    'controllerNamespace' => 'app\commands',

#### 执行控制台类的控制器的方法
    #如:commands/HelloController.php
    #注意继承的是:yii\console\Controller类
    php yii hello/index 参数abc
    #或
    ./yii hello/index 参数abc

#### The Process class relies on XXXX, which is not available on your PHP installation
    #修改 /usr/local/php/etc/php.ini 配置文件的disable_functions属性

