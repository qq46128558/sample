## [yii2-queue 队列扩展的使用](https://github.com/yiisoft/yii2-queue/tree/master/docs/guide-zh-CN "https://github.com/yiisoft/yii2-queue/tree/master/docs/guide-zh-CN")



#### 安装
    #yii2框架根目录内执行
    php composer.phar require --prefer-dist yiisoft/yii2-queue
    #或
    composer require --prefer-dist yiisoft/yii2-queue

#### 配置
~~~
#config/console.php
#<driver>表示使用哪个驱动存储队列信息:一般Redis/Db/File等
return [
'bootstrap' => [
    'queue', // 把这个组件注册到控制台
],
'components' => [
        'queue' => [
            'class' => \yii\queue\<driver>\Queue::class,
            'as log' => \yii\queue\LogBehavior::class,
            // 驱动的其他选项
            'redis' => 'redis', // 连接组件或它的配置
            'channel' => 'queue', // Queue channel key
        ],
    ],
];
~~~

#### 代码中使用

每个被发送到队列的任务应该被定义为一个单独的类

~~~
namespace app\commands\timinglottery\dev;
// 实现接口首位要加\
class CalcJob extends \yii\base\BaseObject implements \yii\queue\Job
{
    public $activityId;

    public function __construct($activityId)
    {
        $this->activityId=$activityId;
    }

    public function execute($queue)
    {
        // 调用控制台控制器进行计算(很多值在里面)
        \Yii::$app->runAction('timinglottery/dev/main/calc',$this->activityId);
    }
}
~~~

下面是将任务添加到队列

~~~
$id=\Yii::$app->queue->push(new CalcJob([$activityId]));
~~~

#### 作业状态(部份未验证)
~~~
// 将作业推送到队列并获得其ID
$id = Yii::$app->queue->push(new SomeJob());

// 这个作业是否等待执行。
Yii::$app->queue->isWaiting($id);

// Worker 从队列获取作业，并执行它。
Yii::$app->queue->isReserved($id);

// Worker 作业是否执行完成。
Yii::$app->queue->isDone($id);
~~~


#### 事件处理
~~~
#例如，如果它的执行失败了，那么让我们延迟它:
Yii::$app->queue->on(Queue::EVENT_AFTER_ERROR, function ($event) {
    if ($event->error instanceof TemporaryUnprocessableJobException) {
        $queue = $event->sender;
        $queue->delay(7200)->push($event->job);    
    }
});
~~~

#### 重试作业接口
~~~
class SomeJob extends \yii\base\BaseObject implements \yii\queue\RetryableJob
{
    public function execute($queue)
    {
        //...
    }

    public function getTtr()
    {
        return 15 * 60;
    }

    public function canRetry($attempt, $error)
    {
        return ($attempt < 5) && ($error instanceof TemporaryException);
    }
}
~~~


#### Worker starting control
~~~
#Cron
#您可以用cron开始worker。需要使用 queue/run 命令。只要队列包含作业，它就能进行执行。
#配置示例
* * * * * /usr/bin/php /var/www/my_project/yii queue/run

#还有Supervisor及Systemd
~~~


#### 调试
~~~
为了使开发过程更加友好，您可以向Yii2调试模块添加一个面板。面板显示 计数器和队列任务列表。
yiisoft/yii2-debug 应该安装在你的应用程序中，以便在调试面板中显示
将您的应用程序配置如下：
return [
    'modules' => [
        'debug' => [
            'class' => \yii\debug\Module::class,
            'panels' => [
                'queue' => \yii\queue\debug\Panel::class,
            ],
        ],
    ],
];
~~~

#### Redis驱动
~~~
驱动程序使用Redis存储队列数据。
您需要添加 yiisoft/yii2-redis 扩展到你的应和中。
配置示例:
return [
    'bootstrap' => [
        'queue', // 把这个组件注册到控制台
    ],
    'components' => [
        'redis' => [
            'class' => \yii\redis\Connection::class,
            // ...
        ],
        'queue' => [
            'class' => \yii\queue\redis\Queue::class,
            'redis' => 'redis', // 连接组件或它的配置
            'channel' => 'queue', // Queue channel key
        ],
    ],
];
~~~

控制台

~~~
#启动一个守护进程,当命令正确地通过supervisor来实现时，这种方法是最有效的
yii queue/listen [timeout]

#run命令获取并执行循环中的任务，直到队列为空。适用与cron
yii queue/run
    --verbose, -v: 将执行状态输出到控制台。
    --isolate: 详细模式执行作业。如果启用，将打印每个作业的执行结果。
    --color: 高亮显示输出结果。

#info 命令打印关于队列状态的信息。
yii queue/info

#clear command clears a queue.
yii queue/clear

#remove command removes a job.
yii queue/remove [id]
~~~