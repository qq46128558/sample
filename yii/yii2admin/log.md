## 日志

#### 配置
backend/config/main.php
~~~
'components' => [
        'log' => [
            'traceLevel' => YII_DEBUG ? 3 : 0,
            'targets' => [
                [
                    // 日志输出类型--文件输出
                    'class' => 'yii\log\FileTarget',
                    // 日志输出级别
                    'levels' => ['trace','info','warning','error'],
                ],
            ],
        ],
~~~

#### 文件日志位置
    查看代码vendor/yiisoft/yii2/log/FileTarget.php
    $this->logFile = Yii::$app->getRuntimePath() . '/logs/app.log';
    如: backend/runtime/logs/app.log

#### 输出日志
    Yii::info('XXX', __METHOD__);
    Yii::error('XXX');