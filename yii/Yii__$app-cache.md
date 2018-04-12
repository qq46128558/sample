## 数据缓存

#### 配置
~~~
'components' => [
    'cache' => [
        'class' => 'yii\caching\FileCache',
    ],
],

// Tip：你可以注册多个缓存组件，很多依赖缓存的类默认调用 名为 cache 的组件（例如 yii\web\UrlManager）   
~~~

#### 支持的缓存存储器
- yii\caching\ApcCache：使用 PHP APC 扩展。 这个选项可以认为是集中式应用程序环境中 （例如：单一服务器，没有独立的负载均衡器等）`最快的缓存方案`。
- yii\caching\DbCache：使用一个数据库的表存储缓存数据。要使用这个缓存， 你必须创建一个与 yii\caching\DbCache::$cacheTable 对应的表。
- 为了增强 ArrayCache 的性能，您可以通过将 yii\caching\ArrayCache::$serializer 设置为 false 来禁用已存储数据的序列化。
- yii\caching\DummyCache：仅作为一个缓存占位符，`不实现任何真正的缓存功能`。 这个组件的目的是为了简化那些需要查询缓存有效性的代码。例如， 在开发中如果服务器没有实际的缓存支持，用它配置一个缓存组件。 一个真正的缓存服务启用后，可以再切换为使用相应的缓存组件。 两种条件下你都可以使用同样的代码 Yii::$app->cache->get($key) 尝试从缓存中取回数据而不用担心 Yii::$app->cache 可能是 null。
- yii\caching\FileCache：使用标准文件存储缓存数据。 这个特别适用于缓存大块数据，例如一个整页的内容。
- yii\caching\MemCache：使用 PHP memcache 和 memcached 扩展。 这个选项被看作分布式应用环境中（例如：多台服务器，有负载均衡等） `最快的缓存方案`。
- yii\redis\Cache：实现了一个基于 Redis 键值对存储器的缓存组件 （需要 redis 2.6.12 及以上版本的支持 ）。
- yii\caching\WinCache：使用 PHP WinCache （另可参考）扩展.
- yii\caching\XCache：使用 PHP XCache扩展。
- yii\caching\ZendDataCache：使用 [Zend Data Cache](http://files.zend.com/help/Zend-Server-6/zend- server.htm#data_cache_component.htm) 作为底层缓存媒介。

Tip：你可以在同一个应用程序中使用不同的缓存存储器。一个常见的策略是使用基于内存的缓存存储器 存储小而常用的数据（例如：统计数据），使用基于文件或数据库的缓存存储器 存储大而不太常用的数据（例如：网页内容）。

#### 基本使用
    $cache=Yii::$app->cache;

#### 简化数据的取回、计算和存储
~~~
$data = $cache->getOrSet($key, function () {
    return $this->calculateSomething();
});
~~~

#### 使用作用域外的数据(use语句)
~~~
$user_id = 42;
$data = $cache->getOrSet($key, function () use ($user_id) {
    return $this->calculateSomething($user_id);
});
~~~

#### 缓存API
- get()：通过一个指定的键（key）从缓存中取回一项数据。 如果该项数据不存在于缓存中或者已经过期/失效，则返回值 false。
- set()：将一个由键指定的数据项存放到缓存中。
- add()：如果缓存中未找到该键，则将指定数据存放到缓存中。
- getOrSet()：返回由键指定的缓存项，或者执行回调函数，把函数的返回值用键来关联存储到缓存中， 最后返回这个函数的返回值。
- multiGet()：由指定的键获取多个缓存数据项。
- multiSet()：一次存储多个数据项到缓存中，每个数据都由一个键来指明。
- multiAdd()：一次存储多个数据项到缓存中，每个数据都由一个键来指明。 如果某个键已经存在，则略过该数据项不缓存。
- exists()：返回一个值，指明某个键是否存在于缓存中。
- delete()：通过一个键，删除缓存中对应的值。
- flush()：删除缓存中的所有数据。

**千万别直接用 false 布尔值当做数据项缓存**，因为 get() 方法用 false 作为返回值来表名对应的缓存项不存在。 你可以把 false 放到一个数组里然后缓存这个数组来避免上述的混淆问题。

#### 像数组那样使用
~~~
// 由于 yii\caching\Cache 实现了 PHP ArrayAccess 接口， 缓存组件也可以像数组那样使用
$cache['var1'] = $value1;  // 等价于： $cache->set('var1', $value1);
$value2 = $cache['var2'];  // 等价于： $value2 = $cache->get('var2');
~~~


