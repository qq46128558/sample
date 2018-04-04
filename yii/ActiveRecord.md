## 活动记录(AR)
- AR yii\db\ActiveRecord 继承了模型 yii\base\Model
- 活动记录 AR 默认使用 db 组件 作为连接器
- 内容较多=>[中文资料地址](http://www.yiichina.com/doc/guide/2.0/db-active-record,"http://www.yiichina.com/doc/guide/2.0/db-active-record")

#### 声明AR类
~~~
namespace app\models;
use yii\db\ActiveRecord;
class Customer extends ActiveRecord
{
    // 后面AR查询数据示例用到
    const STATUS_INACTIVE = 0;
    const STATUS_ACTIVE = 1;
}
~~~

#### 设置表名
~~~
    /**
     * @return string AR 类关联的数据库表名称
     */
    public static function tableName()
    {
        return '{{customer}}';
    }
~~~

#### 使用其他DB
~~~
    // 如果你要用不同的数据库连接，而不仅仅是 db 组件， 你可以重写 getDb() 方法。
    public static function getDb()
    {
        // 使用 "db2" 组件
        return \Yii::$app->db2;  
    }
~~~

#### AR查询数据 find()
~~~
// yii\db\ActiveRecord::find() 去获得一个新的查询生成器对象，这个对象是 yii\db\ActiveQuery
// 由于 yii\db\ActiveQuery 继承 yii\db\Query，你可以使用 查询生成器 所描述的所有查询方法

// 返回 ID 为 123 的客户：
// SELECT * FROM `customer` WHERE `id` = 123
$customer = Customer::find()
    ->where(['id' => 123])
    ->one();

// 取回所有活跃客户并以他们的 ID 排序：
// SELECT * FROM `customer` WHERE `status` = 1 ORDER BY `id`
$customers = Customer::find()
    ->where(['status' => Customer::STATUS_ACTIVE])
    ->orderBy('id')
    ->all();

// 取回活跃客户的数量：
// SELECT COUNT(*) FROM `customer` WHERE `status` = 1
$count = Customer::find()
    ->where(['status' => Customer::STATUS_ACTIVE])
    ->count();

// 以客户 ID 索引结果集：
// SELECT * FROM `customer`
$customers = Customer::find()
    ->indexBy('id')
    ->all();
~~~

#### findOne()
~~~
// 返回 id 为 123 的客户 
// SELECT * FROM `customer` WHERE `id` = 123
$customer = Customer::findOne(123);

// 返回 id 是 123 的活跃客户
// SELECT * FROM `customer` WHERE `id` = 123 AND `status` = 1
$customer = Customer::findOne([
    'id' => 123,
    'status' => Customer::STATUS_ACTIVE,
]);

// 提示：yii\db\ActiveRecord::findOne() 和 yii\db\ActiveQuery::one() 都不会添加 LIMIT 1 到 生成的 SQL 语句中。如果你的查询会返回很多行的数据， 你明确的应该加上 limit(1) 来提高性能，比如 Customer::find()->limit(1)->one()。
~~~

#### findAll()
~~~
// 返回 id 是 100, 101, 123, 124 的客户
// SELECT * FROM `customer` WHERE `id` IN (100, 101, 123, 124)
$customers = Customer::findAll([100, 101, 123, 124]);

// 返回所有不活跃的客户
// SELECT * FROM `customer` WHERE `status` = 0
$customers = Customer::findAll([
    'status' => Customer::STATUS_INACTIVE,
]);
~~~

#### findBySql()
~~~
// 返回所有不活跃的客户
$sql = 'SELECT * FROM customer WHERE status=:status';
$customers = Customer::findBySql($sql, [':status' => Customer::STATUS_INACTIVE])->all();

// 不要在 findBySql() 方法后加其他查询方法了， 多余的查询方法都会被忽略
~~~

#### 访问数据
~~~
// 如上所述，从数据库返回的数据被填充到 AR 实例中， 查询结果的每一行对应于单个 AR 实例
// "id" 和 "email" 是 "customer" 表中的列名
$customer = Customer::findOne(123);
$id = $customer->id;
$email = $customer->email;

// AR 的属性以区分大小写的方式为相关联的表列命名的。 Yii 会自动为关联表的每一列定义 AR 中的一个属性。 您不应该重新声明任何属性。
~~~

#### 数据转换
~~~
    public function getBirthdayText()
    {
        return date('Y/m/d', $this->birthday);
    }
    
    public function setBirthdayText($value)
    {
        $this->birthday = strtotime($value);
    }
// 你可以访问 $customer->birthdayText， 来以 'YYYY/MM/DD' 的格式输入和显示客户生日，而不是访问$customer->birthday
~~~

#### asArray() 以数组形式获取数据
~~~
// 返回所有客户
// 每个客户返回一个关联数组
$customers = Customer::find()
    ->asArray()
    ->all();
~~~

#### 批量获取数据 batch()/each()
~~~
// 每次获取 10 条客户数据
foreach (Customer::find()->batch(10) as $customers) {
    // $customers 是个最多拥有 10 条数据的数组
}

// 每次获取 10 条客户数据，然后一条一条迭代它们
foreach (Customer::find()->each(10) as $customer) {
    // $customer 是个 `Customer` 对象
}

// 贪婪加载模式的批处理查询
foreach (Customer::find()->with('orders')->each() as $customer) {
    // $customer 是个 `Customer` 对象，并附带关联的 `'orders'`
}
~~~

#### save()/insert()/update()/isNewRecord()
~~~
// 插入新记录
$customer = new Customer();
$customer->name = 'James';
$customer->email = 'james@example.com';
$customer->save();

// 更新已存在的记录
$customer = Customer::findOne(123);
$customer->email = 'james@newexample.com';
$customer->save();

public function save($runValidation = true, $attributeNames = null)
{
    if ($this->getIsNewRecord()) {
        return $this->insert($runValidation, $attributeNames);
    } else {
        return $this->update($runValidation, $attributeNames) !== false;
    }
}

// 如果你确定你的数据不需要验证（比如说数据来自可信的场景）， 你可以调用 save(false) 来跳过验证过程
~~~

#### 块赋值
~~~
$values = [
    'name' => 'James',
    'email' => 'james@example.com',
];

$customer = new Customer();

$customer->attributes = $values;
$customer->save();
~~~

#### updateCounters() 更新计数
~~~
$post = Post::findOne(100);

// UPDATE `post` SET `view_count` = `view_count` + 1 WHERE `id` = 100
$post->updateCounters(['view_count' => 1]);
~~~

#### 脏属性
~~~
yii\db\ActiveRecord::getDirtyAttributes() 获取当前的脏属性
获取属性原先的值，你可以调用 yii\db\ActiveRecord::getOldAttributes() 或者 yii\db\ActiveRecord::getOldAttribute()
~~~

#### loadDefaultValues 默认属性值
~~~
// 调用 loadDefaultValues() 来填充 DB 定义的默认值 进入相应的 AR 属性
$customer = new Customer();
$customer->loadDefaultValues();
// $customer->xyz 将被 “zyz” 列定义的默认值赋值
~~~

#### updateAll()
~~~
// 这是一个静态方法
// UPDATE `customer` SET `status` = 1 WHERE `email` LIKE `%@example.com%`
Customer::updateAll(['status' => Customer::STATUS_ACTIVE], ['like', 'email', '@example.com']);
~~~

#### updateAllCounters()
~~~
// UPDATE `customer` SET `age` = `age` + 1
Customer::updateAllCounters(['age' => 1]);
~~~

#### delete()
~~~
$customer = Customer::findOne(123);
$customer->delete();
~~~

#### deleteAll()
~~~
Customer::deleteAll(['status' => Customer::STATUS_INACTIVE]);
// 不要随意使用 deleteAll() 
~~~

#### [AR生命周期](http://www.yiichina.com/doc/guide/2.0/db-active-record "http://www.yiichina.com/doc/guide/2.0/db-active-record")
    

#### 事务操作
~~~
// 方法一
$customer = Customer::findOne(123);
Customer::getDb()->transaction(function($db) use ($customer) {
    $customer->id = 200;
    $customer->save();
    // ...其他 DB 操作...
});
// 或者
$transaction = Customer::getDb()->beginTransaction();
try {
    $customer->id = 200;
    $customer->save();
    // ...other DB operations...
    $transaction->commit();
} catch(\Exception $e) {
    $transaction->rollBack();
    throw $e;
} catch(\Throwable $e) {
    $transaction->rollBack();
    throw $e;
}

// 第二种方法是在 yii\db\ActiveRecord::transactions() 方法中列出需要事务支持的 DB 操作
public function transactions()
    {
        return [
            'admin' => self::OP_INSERT,
            'api' => self::OP_INSERT | self::OP_UPDATE | self::OP_DELETE,
            // 上面等价于：
            // 'api' => self::OP_ALL,
        ];
    }
// yii\db\ActiveRecord::transactions() 方法应当返回以 场景 为键、 以需要放到事务中的 DB 操作为值的数组
~~~

#### 乐观锁
~~~
- 在与 AR 类相关联的 DB 表中创建一个列，以存储每行的版本号。 这个列应当是长整型（在 MySQL 中是 BIGINT DEFAULT 0）。
- 重写 yii\db\ActiveRecord::optimisticLock() 方法返回这个列的命名。
- 在用于用户填写的 Web 表单中，添加一个隐藏字段（hidden field）来存储正在更新的行的当前版本号。 （AR 类中）版本号这个属性你要自行写进 rules() 方法并自己验证一下。
- 在使用 AR 更新数据的控制器动作中，要捕获（try/catch） yii\db\StaleObjectException 异常。 实现一些业务逻辑来解决冲突（例如合并更改，提示陈旧的数据等等）。

// ------ 视图层代码 -------
use yii\helpers\Html;
// ...其他输入栏
echo Html::activeHiddenInput($model, 'version');


// ------ 控制器代码 -------
use yii\db\StaleObjectException;
public function actionUpdate($id)
{
    $model = $this->findModel($id);

    try {
        if ($model->load(Yii::$app->request->post()) && $model->save()) {
            return $this->redirect(['view', 'id' => $model->id]);
        } else {
            return $this->render('update', [
                'model' => $model,
            ]);
        }
    } catch (StaleObjectException $e) {
        // 解决冲突的代码
    }
}
~~~

#### 声明关联关系
~~~
class Customer extends ActiveRecord
{
    // ...
    public function getOrders()
    {
        // 一个客户可以有很多订单
        // customer_id 是 Order 的属性 id是 Customer 的属性
        // 先副表的主键，后主表的主键
        return $this->hasMany(Order::className(), ['customer_id' => 'id']);
    }
}

class Order extends ActiveRecord
{
    // ...
    public function getCustomer()
    {
        // 每个订单只有一个客户
        // 先副表的主键，后主表的主键
        // customer_id 是 Order 的属性 id是 Customer 的属性
        return $this->hasOne(Customer::className(), ['id' => 'customer_id']);
    }
}
// 上述的代码中，我们为 Customer 类声明了一个 orders 关联， 和为 Order 声明了一个 customer 关联
// 每个关联方法必须这样命名：getXyz。然后我们通过 xyz（首字母小写）调用这个关联名。 请注意关联名是大小写敏感的

// 你可以使用 $customer->orders 表达式访问客户的订单信息
~~~


#### 访问关联数据 
~~~
// SELECT * FROM `customer` WHERE `id` = 123
$customer = Customer::findOne(123);

// SELECT * FROM `order` WHERE `customer_id` = 123
// $orders 是由 Order 类组成的数组
$orders = $customer->orders;

// 当你第一次访问关联属性时，将执行 SQL 语句获取数据，如 上面的例子所示。如果再次访问相同的属性，将返回先前的结果，而不会重新执行 SQL 语句。要强制重新执行 SQL 语句，你应该先 unset 这个关联属性， 如：
unset（$customer-> orders）。

$customer->orders; // 获得 `Order` 对象的数组
$customer->getOrders(); // 返回 ActiveQuery 类的实例
~~~

#### 动态关联查询
~~~
$customer = Customer::findOne(123);

// SELECT * FROM `order` WHERE `customer_id` = 123 AND `subtotal` > 200 ORDER BY `id`
$orders = $customer->getOrders()
    ->where(['>', 'subtotal', 200])
    ->orderBy('id')
    ->all();

// 与访问关联属性不同，每次通过关联方法执行动态关联查询时， 都会执行 SQL 语句，即使你之前执行过相同的动态关联查询。
// 有时你可能需要给你的关联声明传递参数，以便您能更方便地执行 动态关系查询。例如，您可以声明一个 bigOrders 关联如下
class Customer extends ActiveRecord
{
    public function getBigOrders($threshold = 100) // 老司机的提醒：$threshold 参数一定一定要给个默认值
    {
        return $this->hasMany(Order::className(), ['customer_id' => 'id'])
            ->where('subtotal > :threshold', [':threshold' => $threshold])
            ->orderBy('id');
    }
}
// 然后你就可以执行以下关联查询：
// SELECT * FROM `order` WHERE `customer_id` = 123 AND `subtotal` > 200 ORDER BY `id`
$orders = $customer->getBigOrders(200)->all();

// SELECT * FROM `order` WHERE `customer_id` = 123 AND `subtotal` > 100 ORDER BY `id`
$orders = $customer->bigOrders;
~~~

#### [中间关联表_未理解](http://www.yiichina.com/doc/guide/2.0/db-active-record "http://www.yiichina.com/doc/guide/2.0/db-active-record")


#### 延迟加载和即时加载
~~~
// （又称惰性加载与贪婪加载）
// SQL 语句仅在 你第一次访问关联属性时执行

// SELECT * FROM `customer` LIMIT 100
$customers = Customer::find()->limit(100)->all();
foreach ($customers as $customer) {
    // SELECT * FROM `order` WHERE `customer_id` = ...
    $orders = $customer->orders;
}
// 上面的代码会产生 101 次 SQL 查询！ 这是因为每次你访问 for 循环中不同的 Customer 对象的 orders 关联属性时，SQL 语句 都会被执行一次

// 为了解决上述的性能问题，你可以使用所谓的 即时加载
// SELECT * FROM `customer` LIMIT 100;
// SELECT * FROM `orders` WHERE `customer_id` IN (...)
$customers = Customer::find()
    ->with('orders')
    ->limit(100)
    ->all();

foreach ($customers as $customer) {
    // 没有任何的 SQL 执行
    $orders = $customer->orders;
}
// 通过调用 yii\db\ActiveQuery::with() 方法，你使 AR 在一条 SQL 语句里就返回了这 100 位客户的订单。 结果就是，你把要执行的 SQL 语句从 101 减少到 2 条！
~~~


#### 嵌套关联
~~~
//  即时加载 "orders" and "country"
$customers = Customer::find()->with('orders', 'country')->all();
// 等同于使用数组语法 如下
$customers = Customer::find()->with(['orders', 'country'])->all();
// 没有任何的 SQL 执行
$orders= $customers[0]->orders;
// 没有任何的 SQL 执行
$country = $customers[0]->country;

// eager loading "orders" and the nested relation "orders.items"
$customers = Customer::find()->with('orders.items')->all();
// access the items of the first order of the first customer
// no SQL executed
$items = $customers[0]->orders[0]->items;

// 你也可以即时加载更深的嵌套关联，比如 a.b.c.d。所有的父关联都会被即时加载。 那就是, 当你调用 yii\db\ActiveQuery::with() 来 with a.b.c.d, 你将即时加载 a, a.b, a.b.c and a.b.c.d

// 如果你在即时加载的关联中调用 select() 方法，你要确保 在关联声明中引用的列必须被 select。否则，相应的模型（Models）可能 无法加载。例如，
$orders = Order::find()->select(['id', 'amount'])->with('customer')->all();
// $orders[0]->customer 会一直是 `null`。你应该这样写，以解决这个问题：
$orders = Order::find()->select(['id', 'amount', 'customer_id'])->with('customer')->all();
~~~


#### 通过匿名函数自定义相应的关联查询
~~~
// 查找所有客户，并带上他们国家和活跃订单
// SELECT * FROM `customer`
// SELECT * FROM `country` WHERE `id` IN (...)
// SELECT * FROM `order` WHERE `customer_id` IN (...) AND `status` = 1
$customers = Customer::find()->with([
    'country',
    'orders' => function ($query) {
        $query->andWhere(['status' => Order::STATUS_ACTIVE]);
    },
])->all();
~~~


#### 关联关系的 JOIN 查询
~~~
// SELECT `customer`.* FROM `customer`
// LEFT JOIN `order` ON `order`.`customer_id` = `customer`.`id`
// WHERE `order`.`status` = 1
// 
// SELECT * FROM `order` WHERE `customer_id` IN (...)
$customers = Customer::find()
    ->select('customer.*')
    ->leftJoin('order', '`order`.`customer_id` = `customer`.`id`')
    ->where(['order.status' => Order::STATUS_ACTIVE])
    ->with('orders')
    ->all();

// 但是，更好的方法是通过调用 yii\db\ActiveQuery::joinWith() 来利用已存在的关联声明
$customers = Customer::find()
    ->joinWith('orders')
    ->where(['order.status' => Order::STATUS_ACTIVE])
    ->all();

// 将 yii\db\ActiveQuery::with() 和 joinWith() 组合起来使用
$customers = Customer::find()->joinWith([
    'orders' => function ($query) {
        $query->andWhere(['>', 'subtotal', 100]);
    },
])->with('country')
    ->all();

// 有时，当连接两个表时，你可能需要在 JOIN 查询的 ON 部分中指定一些额外的条件。 这可以通过调用 yii\db\ActiveQuery::onCondition() 方法来完成
// SELECT `customer`.* FROM `customer`
// LEFT JOIN `order` ON `order`.`customer_id` = `customer`.`id` AND `order`.`status` = 1 
// 
// SELECT * FROM `order` WHERE `customer_id` IN (...)
$customers = Customer::find()->joinWith([
    'orders' => function ($query) {
        $query->onCondition(['order.status' => Order::STATUS_ACTIVE]);
    },
])->all();
~~~

#### 关联表别名
~~~
// 连接 `orders` 关联表并根据 `orders.id` 排序
$query->joinWith(['orders o'])->orderBy('o.id');

// 上述语法适用于简单的关联。如果在 join 嵌套关联时， 需要用到中间表的别名，例如 $query->joinWith(['orders.product'])， 你需要嵌套 joinWith 调用
$query->joinWith(['orders o' => function($q) {
        $q->joinWith('product p');
    }])
    ->where('o.amount > 100');
~~~

#### 反向关联
~~~
// SELECT * FROM `customer` WHERE `id` = 123
$customer = Customer::findOne(123);

// SELECT * FROM `order` WHERE `customer_id` = 123
$order = $customer->orders[0];

// SELECT * FROM `customer` WHERE `id` = 123
$customer2 = $order->customer;

// 显示 "not the same"
echo $customer2 === $customer ? 'same' : 'not the same';

// 我们原本认为 $customer 和 $customer2 是一样的，但不是！其实他们确实包含相同的 客户数据，但它们是不同的对象。 访问 $order->customer 时，需要执行额外的 SQL 语句， 以填充出一个新对象 $customer2

// 为了避免上述例子中最后一个 SQL 语句被冗余执行，我们应该告诉 Yii customer 是 orders 的 反向关联，可以通过调用 yii\db\ActiveQuery::inverseOf() 方法声明
class Customer extends ActiveRecord
{
    public function getOrders()
    {
        return $this->hasMany(Order::className(), ['customer_id' => 'id'])->inverseOf('customer');
    }
}

// 提示:反向关联不能用在有 连接表 关联声明中。 也就是说，如果一个关联关系通过 yii\db\ActiveQuery::via() 或 viaTable() 声明， 你就不能再调用 yii\db\ActiveQuery::inverseOf() 了。
~~~

#### 保存关联数据
~~~
$customer = Customer::findOne(123);
$order = new Order();
$order->subtotal = 100;
// ...

$order->link('customer', $customer);
// yii\db\ActiveRecord::link() 方法需要指定关联名 和要建立关联的目标 AR 实例

// yii\db\ActiveRecord::link() 方法的反向操作是 yii\db\ActiveRecord::unlink() 方法
$customer = Customer::find()->with('orders')->where(['id' => 123])->one();
$customer->unlink('orders', $customer->orders[0]);
~~~

#### 跨数据库关联
~~~
// Customer 对应的表是关系数据库中（比如 MySQL）的 "customer" 表
class Customer extends \yii\db\ActiveRecord
{
    public static function tableName()
    {
        return 'customer';
    }

    public function getComments()
    {
        // 一个 customer 有很多条评论（comments）
        return $this->hasMany(Comment::className(), ['customer_id' => 'id']);
    }
}

// Comment 对应的是 MongoDB 数据库中的  "comment" 集合（译者注：MongoDB 中的集合相当于 MySQL 中的表）
class Comment extends \yii\mongodb\ActiveRecord
{
    public static function collectionName()
    {
        return 'comment';
    }

    public function getCustomer()
    {
        // 一条评论对应一位 customer
        return $this->hasOne(Customer::className(), ['id' => 'customer_id']);
    }
}

$customers = Customer::find()->with('comments')->all();
~~~


#### 自定义查询类
~~~
// file Comment.php
namespace app\models;
use yii\db\ActiveRecord;

class Comment extends ActiveRecord
{
    public static function find()
    {
        return new CommentQuery(get_called_class());
    }
}

// 现在，对于 Comment 类，不管你执行查询（比如 find()、findOne()），还是定义一个关联（比如 hasOne()）， 你都将调用到 CommentQuery 实例，而不再是 ActiveQuery 实例。

// 现在你可以定义 CommentQuery 类了，发挥你的奇技淫巧，以改善查询构建体验
// file CommentQuery.php
namespace app\models;

use yii\db\ActiveQuery;

class CommentQuery extends ActiveQuery
{
    // 默认加上一些条件（可以跳过）
    public function init()
    {
        $this->andOnCondition(['deleted' => false]);
        parent::init();
    }

    // ... 在这里加上自定义的查询方法 ...

    public function active($state = true)
    {
        return $this->andOnCondition(['active' => $state]);
    }
}

// 然后你就可以先下面这样构建你的查询了：
$comments = Comment::find()->active()->all();
$inactiveComments = Comment::find()->active(false)->all();

// 提示：在大型项目中，建议您使用自定义查询类来容纳大多数与查询相关的代码， 以使 AR 类保持简洁

// 您还可以在 Comment 关联关系的定义中或在执行关联查询时，使用刚刚新建查询构建方法：
class Customer extends \yii\db\ActiveRecord
{
    public function getActiveComments()
    {
        return $this->hasMany(Comment::className(), ['customer_id' => 'id'])->active();
    }
}

$customers = Customer::find()->joinWith('activeComments')->all();

// 或者这样
class Customer extends \yii\db\ActiveRecord
{
    public function getComments()
    {
        return $this->hasMany(Comment::className(), ['customer_id' => 'id']);
    }
}

$customers = Customer::find()->joinWith([
    'comments' => function($q) {
        $q->active();
    }
])->all();
~~~

#### 选择额外的字段
~~~
class Room extends \yii\db\ActiveRecord
{
    public $volume;

    // ...
}

// 然后，你需要撰写一个查询，它可以计算房间的大小并执行排序
$rooms = Room::find()
    ->select([
        '{{room}}.*', // select all columns
        '([[length]] * [[width]] * [[height]]) AS volume', // 计算体积
    ])
    ->orderBy('volume DESC') // 使用排序
    ->all();

foreach ($rooms as $room) {
    echo $room->volume; // 包含了由 SQL 计算出的值
}

//使用此方法的一个缺点是，如果数据不是从 SQL 查询上加载的，它必须再单独计算一遍。 
$room = new Room();
$room->length = 100;
$room->width = 50;
$room->height = 2;

$room->volume; // 为 `null`, 因为它没有被声明（赋值）

// 通过 __get() 和 __set() 魔术方法 我们可以将属性赋予行为特性
class Room extends \yii\db\ActiveRecord
{
    private $_volume;
    
    public function setVolume($volume)
    {
        $this->_volume = (float) $volume;
    }
    
    public function getVolume()
    {
        if (empty($this->length) || empty($this->width) || empty($this->height)) {
            return null;
        }
        
        if ($this->_volume === null) {
            $this->setVolume(
                $this->length * $this->width * $this->height
            );
        }
        
        return $this->_volume;
    }

    // ...
}
~~~