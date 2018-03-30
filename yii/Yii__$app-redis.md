[yii2-redis 扩展详解](http://www.yiichina.com/tutorial/1608 "http://www.yiichina.com/tutorial/1608")

#### 配置
config/web.php  
config/console.php  
~~~
'components' => [
    'redis' => [
        'class' => 'yii\redis\Connection',
        'hostname' => 'localhost',
        'port' => 6379,
        'database' => 0,
    ],
]  
~~~

#### 获取 redis 组件
    $redis = Yii::$app->redis;

#### 通用方法
    $result = $redis->executeCommand('hmset', ['test_collection', 'key1', 'val1', 'key2', 'val2']);

#### 快捷方式
    $result = $redis->hmset('test_collection', 'key1', 'val1', 'key2', 'val2');
    