[yii2-redis 扩展详解](http://www.yiichina.com/tutorial/1608 "http://www.yiichina.com/tutorial/1608")

[权威指南](http://www.yiichina.com/doc/guide/2.0/yii2-redis "http://www.yiichina.com/doc/guide/2.0/yii2-redis")

#### 安装
    composer require yiisoft/yii2-redis

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
        'password'  => '717f39',
    ],
]  
~~~

#### 获取 redis 组件
    $redis = Yii::$app->redis;

#### 通用方法
    $result = $redis->executeCommand('hmset', ['test_collection', 'key1', 'val1', 'key2', 'val2']);

#### 快捷方式
    $result = $redis->hmset('test_collection', 'key1', 'val1', 'key2', 'val2');
    

#### 缓存组件配置
~~~
// 使用文件缓存（FileCache）时，缓存是存储在 runtime/cache 目录下；使用 redis 缓存后，缓存将存储在 redis 数据库中，性能将大大提高。
'components' => [
    'cache' => [
        // 'class' => 'yii\caching\FileCache',
        'class' => 'yii\redis\Cache',
    ],
],
~~~

#### 缓存组件使用
~~~
// 获取 cache 组件
$cache = Yii::$app->cache;

// 判断 key 为 username 的缓存是否存在，有则打印，没有则赋值
$key = 'username';
if ($cache->exists($key)) {
    var_dump($cache->get($key));
} else {
    $cache->set($key, 'marko', 60);
}
~~~

#### 会话组件配置
~~~
'components' => [
    'session' => [
        'name' => 'advanced-frontend',
        'class' => 'yii\redis\Session'
    ],
],
~~~

#### 会话组件使用
    // 在开发过程中，切记一定不要使用 PHP 原生的 $_SESSION 去操作，而要使用 Yii 提供的 session 组件，获取方式如下
    $session = Yii::$app->session;


#### ActiveRecord
~~~
// yii\redis\ActiveRecord 实现了 Yii2 中的 ActiveRecord 相关接口，所以我们可以使用 AR 的方式操作 redis 数据库
// 要继承 yii\redis\ActiveRecord，并至少实现 attributes() 方法
// 主键可以通过 yii\redis\ActiveRecord::primaryKey() 定义，如果未指定，则默认为 id
class Customer extends \yii\redis\ActiveRecord
{
    public static function primaryKey()
    {
        return ['id'];
    }
    public function attributes()
    {
        return ['id', 'name', 'age', 'phone', 'status', 'created_at', 'updated_at'];
    }
    public function getOrders()
    {
         return $this->hasMany(Order::className(), ['customer_id' => 'id']);
    }
}
~~~

#### ActiveRecord 使用
~~~
// 使用 AR 方式新增一条记录
$customer = new Customer();
$customer->name = 'marko';
$customer->age = 18;
$customer->phone = 13888888888;
$customer->status = 1;
$customer->save();
echo $customer->id;

// 使用 AR 查询
$customer = Customer::findOne($customer->id);
$customer = Customer::find()->where(['status' => 1])->all();

// 由于 redis 没有表的概念，因此不能通过表定义关联关系，只能通过其它记录来定义关系
~~~