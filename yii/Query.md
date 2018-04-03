## 查询构建器
~~~
use \yii\db\Query;
$query = new Query;
// 或
$query = new \yii\db\Query();
// 你平时更多的时候会使用 yii\db\Query 而不是 [yii\db\QueryBuilder]]。 当你调用其中一个查询方法时，后者将会被前者隐式的调用。yii\db\QueryBuilder主要负责将 DBMS 不相关的 yii\db\Query 对象转换成 DBMS 相关的 SQL 语句

$rows = (new \yii\db\Query())
    ->select(['id', 'email'])
    ->from('user')
    ->where(['last_name' => 'Smith'])
    ->limit(10)
    ->all();
~~~

#### select()
~~~
$query->select(['id', 'email']);
// 等同于：
$query->select('id, email');

~~~