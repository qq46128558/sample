## 数据库访问DAO

#### 配置文件
~~~
config/web.php
'components' => [
    'db' => require(__DIR__ . '/db.php'),

config/db.php
return [
    'class' => 'yii\db\Connection',
    'dsn' => 'mysql:host=localhost;dbname=yii2basic',
    'username' => 'root',
    'password' => '123456',
    'charset' => 'utf8',
];
~~~

#### 建立连接时初始化环境
~~~
'db' => [
    // ...
    'on afterOpen' => function($event) {
        // $event->sender refers to the DB connection
        $event->sender->createCommand("SET time_zone = 'UTC'")->execute();
    }
],
~~~

#### 查询返回多行
    $posts = Yii::$app->db->createCommand('SELECT * FROM post')
            ->queryAll();

#### 查询返回一行
    $post = Yii::$app->db->createCommand('SELECT * FROM post WHERE id=1')
           ->queryOne();

#### 查询返回一列(第一列)
    $titles = Yii::$app->db->createCommand('SELECT title FROM post')
             ->queryColumn();

#### 查询返回一个标量值
    $count = Yii::$app->db->createCommand('SELECT COUNT(*) FROM post')
             ->queryScalar();

#### 查询绑定参数
    $post = Yii::$app->db->createCommand('SELECT * FROM post WHERE id=:id AND status=:status')
           ->bindValue(':id', $_GET['id'])
           ->bindValue(':status', 1)
           ->queryOne();
    #bindParam()：与 bindValue() 相似，但是也支持绑定参数引用

#### 查询绑定多个参数
    $params = [':id' => $_GET['id'], ':status' => 1];
    $post = Yii::$app->db->createCommand('SELECT * FROM post WHERE id=:id AND status=:status')
           ->bindValues($params)
           ->queryOne();
    $post = Yii::$app->db->createCommand('SELECT * FROM post WHERE id=:id AND status=:status', $params)
           ->queryOne();

#### 执行非查询语句
    Yii::$app->db->createCommand('UPDATE post SET status=1 WHERE id=1')
        ->execute();

#### INSERT (table name, column values)
    Yii::$app->db->createCommand()->insert('user', [
        'name' => 'Sam',
        'age' => 30,
    ])->execute();

#### UPDATE (table name, column values, condition)
    Yii::$app->db->createCommand()->update('user', ['status' => 1], 'age > 30')->execute();

#### DELETE (table name, condition)
    Yii::$app->db->createCommand()->delete('user', 'status = 0')->execute();

#### BATCH INSERT
~~~
// table name, column names, column values
Yii::$app->db->createCommand()->batchInsert('user', ['name', 'age'], [
    ['Tom', 30],
    ['Jane', 20],
    ['Linda', 25],
])->execute();
~~~

#### Yii引用表和列名称(通用DB)
~~~
// 在 MySQL 中执行该 SQL : SELECT COUNT(`id`) FROM `employee`
$count = Yii::$app->db->createCommand("SELECT COUNT([[id]]) FROM {{employee}}")
            ->queryScalar();
~~~

#### 使用表前缀
~~~
return [
    // ...
    'components' => [
        // ...
        'db' => [
            // ...
            'tablePrefix' => 'tbl_',
        ],
    ],
];

// 百分号将被自动地替换为你在配置 DB 组件时指定的表前缀
// 在 MySQL 中执行该 SQL: SELECT COUNT(`id`) FROM `tbl_employee`
$count = Yii::$app->db->createCommand("SELECT COUNT([[id]]) FROM {{%employee}}")
            ->queryScalar();
~~~

#### 执行事务
~~~
Yii::$app->db->transaction(function($db) {
    $db->createCommand($sql1)->execute();
    $db->createCommand($sql2)->execute();
    // ... executing other SQL statements ...
});

// 上述代码等价于下面的代码， 但是下面的代码给予了你对于错误处理代码的更多掌控：

$db = Yii::$app->db;
$transaction = $db->beginTransaction();

try {
    $db->createCommand($sql1)->execute();
    $db->createCommand($sql2)->execute();
    // ... executing other SQL statements ...
    
    $transaction->commit();
    
} catch(\Exception $e) {

    $transaction->rollBack();
    
    throw $e;
}
~~~

#### 指定隔离级别
~~~
$isolationLevel = \yii\db\Transaction::REPEATABLE_READ;

Yii::$app->db->transaction(function ($db) {
    ....
}, $isolationLevel);
 
// or alternatively

$transaction = Yii::$app->db->beginTransaction($isolationLevel);

Yii 为四个最常用的隔离级别提供了常量：
yii\db\Transaction::READ_UNCOMMITTED - 最弱的隔离级别，脏读、不可重复读以及幻读都可能发生。
yii\db\Transaction::READ_COMMITTED - 避免了脏读。
yii\db\Transaction::REPEATABLE_READ - 避免了脏读和不可重复读。
yii\db\Transaction::SERIALIZABLE - 最强的隔离级别， 避免了上述所有的问题。
~~~

#### 复制和读写分离
~~~
[
    'class' => 'yii\db\Connection',

    // 主库的配置
    'dsn' => 'dsn for master server',
    'username' => 'master',
    'password' => '',

    // 从库的通用配置
    'slaveConfig' => [
        'username' => 'slave',
        'password' => '',
        'attributes' => [
            // 使用一个更小的连接超时
            PDO::ATTR_TIMEOUT => 10,
        ],
    ],

    // 从库的配置列表
    'slaves' => [
        ['dsn' => 'dsn for slave server 1'],
        ['dsn' => 'dsn for slave server 2'],
        ['dsn' => 'dsn for slave server 3'],
        ['dsn' => 'dsn for slave server 4'],
    ],
]


你可以通过 Yii::$app->db->slave 来获取当前有效的从库连接

如果你想在从库上开启事务，你应该明确地像下面这样做：
$transaction = Yii::$app->db->slave->beginTransaction();

有时，你或许想要强制使用主库来执行读查询。 这可以通过 useMaster() 方法来完成：
$rows = Yii::$app->db->useMaster(function ($db) {
    return $db->createCommand('SELECT * FROM user LIMIT 10')->queryAll();
});

你也可以明确地将 `Yii::$app->db->enableSlaves` 设置为 false 来将所有的读操作指向主库连接。
~~~


#### 操纵数据库模式
~~~
createTable()：创建一张表
renameTable()：重命名一张表
dropTable()：删除一张表
truncateTable()：删除一张表中的所有行
addColumn()：增加一列
renameColumn()：重命名一列
dropColumn()：删除一列
alterColumn()：修改一列
addPrimaryKey()：增加主键
dropPrimaryKey()：删除主键
addForeignKey()：增加一个外键
dropForeignKey()：删除一个外键
createIndex()：增加一个索引
dropIndex()：删除一个索引

// CREATE TABLE
Yii::$app->db->createCommand()->createTable('post', [
    'id' => 'pk',
    'title' => 'string',
    'text' => 'text',
]);
~~~

#### 检索某张表的定义信息
    $table = Yii::$app->db->getTableSchema('post');

