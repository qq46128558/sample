## runAction()方法

- 控制台命令一般用runAction方法执行控制器中的方法
- 优先查找console/config中controllerNamespace/controllerMap配置的控制器
- 其次有可能查找common/config中配置的控制器(未确定,如php yii cache/flush-all)


#### 执行当前控制器内的action
    # public function actionSetWritable()
    $this->runAction('set-writable', ['interactive' => $this->interactive]);

#### 执行其他控制器的action
    // console中的迁移action
    Yii::$app->runAction('migrate/up', ['interactive' => false]);
    # 如何找到migrate控制器?
    # 1 由于console\controllers内无Migrate控制器
    # 2 查看控制器名称映射(.\console\config\main.php),找到migrate映射为类'e282486518\migration\ConsoleController'
    # 3 找到对应类文件: vendor/e282486518/yii2-console-migration/ConsoleController.php
    # 4 找到继承类: vendor/yiisoft/yii2/console/controllers/MigrateController.php
    # 5 找到继承类: vendor/yiisoft/yii2/console/controllers/BaseMigrateController.php
    # 6 找到actionUp()方法

### 执行其他控制器2
    // console中的清缓存
    Yii::$app->runAction('cache/flush-all', ['interactive' => false]);
    # 未确认
    # common\config\main.php 中有component: cache 对应yii\caching\FileCache类
    # FileCache类及父类中均没找到flush-all的action?
    