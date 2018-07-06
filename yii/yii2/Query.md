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

$query->select(['user.id AS user_id', 'email']);
// 等同于：
$query->select('user.id AS user_id, email');
$query->select(['user_id' => 'user.id', 'email']);

// 当你使用到包含逗号的数据库表达式的时候， 你必须使用数组的格式，以避免自动的错误的引号添加
$query->select(["CONCAT(first_name, ' ', last_name) AS full_name", 'email']); 
~~~

#### sub select()
~~~
$subQuery = (new Query())->select('COUNT(*)')->from('user');

// SELECT `id`, (SELECT COUNT(*) FROM `user`) AS `count` FROM `post`
$query = (new Query())->select(['id', 'count' => $subQuery])->from('post');
~~~

#### distinct()
~~~
// SELECT DISTINCT `user_id` ...
$query->select('user_id')->distinct();
~~~

#### addSelect()
~~~
$query->select(['id', 'username'])
    ->addSelect(['email']);
~~~

#### from()
~~~
// SELECT * FROM `user`
$query->from('user');

$query->from(['public.user u', 'public.post p']);
// 等同于：
$query->from('public.user u, public.post p');
$query->from(['u' => 'public.user', 'p' => 'public.post']);
~~~

#### sub from()
~~~
$subQuery = (new Query())->select('id')->from('user')->where('status=1');

// SELECT * FROM (SELECT `id` FROM `user` WHERE status=1) u 
$query->from(['u' => $subQuery]);
~~~

#### where()
~~~
$query->where('status=1');

// or use parameter binding to bind dynamic parameter values
$query->where('status=:status', [':status' => $status]);

// raw SQL using MySQL YEAR() function on a date field
$query->where('YEAR(somedate) = 2015');
~~~

#### addParams()
~~~
$query->where('status=:status')
    ->addParams([':status' => $status]);
~~~

#### AND
~~~
// 哈希格式
// ...WHERE (`status` = 10) AND (`type` IS NULL) AND (`id` IN (4, 8, 15))
$query->where([
    'status' => 10,
    'type' => null,
    'id' => [4, 8, 15],
]);
~~~

#### IN
~~~
$userQuery = (new Query())->select('id')->from('user');

// ...WHERE `id` IN (SELECT `id` FROM `user`)
$query->where(['id' => $userQuery]);

$query->where(['id'=>[4,8,15]]);
~~~

#### 操作符格式
~~~
[操作符, 操作数1, 操作数2, ...]
['and', 'id=1', 'id=2'] 将会生成 id=1 AND id=2
['and', 'type=1', ['or', 'id=1', 'id=2']] 将会生成 type=1 AND (id=1 OR id=2)
or: 用法和 and 操作符类似

['between', 'id', 1, 10] 将会生成 id BETWEEN 1 AND 10

['in', 'id', [1, 2, 3]] 将生成 id IN (1, 2, 3)
not in: 用法和 in 操作符类似

['like', 'name', 'tester'] 会生成 name LIKE '%tester%'
['like', 'name', ['test', 'sample']] 将会生成 name LIKE '%test%' AND name LIKE '%sample%'

exists: 需要一个操作数，该操作数必须是代表子查询 yii\db\Query 的一个实例， 它将会构建一个 EXISTS (sub-query) 表达式

['>', 'age', 10] 将会生成 age>10
~~~

#### andWhere()/orWhere()
~~~
$status = 10;
$search = 'yii';

$query->where(['status' => $status]);

// ... WHERE (`status` = 10) AND (`title` LIKE '%yii%')
if (!empty($search)) {
    $query->andWhere(['like', 'title', $search]);
}
~~~

#### filterWhere()
~~~
// yii\db\Query::filterWhere() 和 where() 唯一的不同就在于，前者 将忽略在条件当中的hash format的空值。所以如果 $email 为空而 $username 不为空，那么上面的代码最终将生产如下 SQL ...WHERE username=:username。
// $username 和 $email 来自于用户的输入
$query->filterWhere([
    'username' => $username,
    'email' => $email,		
]);
// 你可以使用 yii\db\Query::andFilterWhere() 和 yii\db\Query::orFilterWhere() 方法 来追加额外的过滤条件
~~~

#### orderBy()
~~~
// ... ORDER BY `id` ASC, `name` DESC
$query->orderBy([
    'id' => SORT_ASC,
    'name' => SORT_DESC,
]);
// PHP 的常量 SORT_ASC 指的是升序排列，SORT_DESC 指的则是降序排列

$query->orderBy('id ASC, name DESC');
~~~

#### addOrderBy()
~~~
$query->orderBy('id ASC')
    ->addOrderBy('name DESC');
~~~

#### groupBy()
~~~
// ... GROUP BY `id`, `status`
$query->groupBy(['id', 'status']);
$query->groupBy('id, status');
~~~


#### addGroupBy()
~~~
$query->groupBy(['id', 'status'])
    ->addGroupBy('age');
~~~

#### having()
~~~
// ... HAVING `status` = 1
$query->having(['status' => 1]);
~~~

#### addHaving()/orHaving()
~~~
// 你可以调用 andHaving() 或者 orHaving() 方法来为 HAVING 子句追加额外的条件
// ... HAVING (`status` = 1) AND (`age` > 30)
$query->having(['status' => 1])
    ->andHaving(['>', 'age', 30]);
~~~


#### limit() offset()
~~~
// ... LIMIT 10 OFFSET 20
$query->limit(10)->offset(20);
~~~

#### join()
~~~~
// ... LEFT JOIN `post` ON `post`.`user_id` = `user`.`id`
$query->join('LEFT JOIN', 'post', 'post.user_id = user.id');
~~~~

#### leftjoin()/innerJoin()/rightJoin()
~~~
$query->leftJoin('post', 'post.user_id = user.id');

// 除了连接表以外，你还可以连接子查询
$subQuery = (new \yii\db\Query())->from('post');
$query->leftJoin(['u' => $subQuery], 'u.id = author_id');
~~~

#### union()
~~~
$query1 = (new \yii\db\Query())
    ->select("id, category_id AS type, name")
    ->from('post')
    ->limit(10);

$query2 = (new \yii\db\Query())
    ->select('id, type, name')
    ->from('user')
    ->limit(10);

$query1->union($query2);
~~~


#### 查询方法
~~~
// SELECT `id`, `email` FROM `user`
$rows = (new \yii\db\Query())
    ->select(['id', 'email'])
    ->from('user')
    ->all();
    
// SELECT * FROM `user` WHERE `username` LIKE `%test%`
$row = (new \yii\db\Query())
    ->from('user')
    ->where(['like', 'username', 'test'])
    ->one();

// 执行 SQL: SELECT COUNT(*) FROM `user` WHERE `last_name`=:last_name
$count = (new \yii\db\Query())
    ->from('user')
    ->where(['last_name' => 'Smith'])
    ->count();

all()：将返回一个由行组成的数组，每一行是一个由名称和值构成的关联数组（译者注：省略键的数组称为索引数组）。
one()：返回结果集的第一行。
    one() 方法只返回查询结果当中的第一条数据， 条件语句中不会加上 LIMIT 1 条件。如果你清楚的知道查询将会只返回一行或几行数据 （例如， 如果你是通过某些主键来查询的），这很好也提倡这样做。但是，如果查询结果 有机会返回大量的数据时，那么你应该显示调用 limit(1) 方法，以改善性能。 例如， (new \yii\db\Query())->from('user')->limit(1)->one()。
column()：返回结果集的第一列。
scalar()：返回结果集的第一行第一列的标量值。
exists()：返回一个表示该查询是否包结果集的值。
count()：返回 COUNT 查询的结果。

其它集合查询方法：包括 sum($q), average($q), max($q), min($q) 等。$q 是一个必选参数， 既可以是一个字段名称，又可以是一个 DB 表达式。
~~~


#### createCommand()
~~~
$command = (new \yii\db\Query())
    ->select(['id', 'email'])
    ->from('user')
    ->where(['last_name' => 'Smith'])
    ->limit(10)
    ->createCommand();
    
// 打印 SQL 语句
echo $command->sql;
// 打印被绑定的参数
print_r($command->params);

// 返回查询结果的所有行
$rows = $command->queryAll();
~~~

#### indexBy()
~~~
// 当你在调用 all() 方法时，它将返回一个以连续的整型数值为索引的数组。 而有时候你可能希望使用一个特定的字段或者表达式的值来作为索引结果集数组。那么你可以在调用 all() 之前使用 yii\db\Query::indexBy() 方法来达到这个目的。
// 返回 [100 => ['id' => 100, 'username' => '...', ...], 101 => [...], 103 => [...], ...]
$query = (new \yii\db\Query())
    ->from('user')
    ->limit(10)
    ->indexBy('id')
    ->all();

$query = (new \yii\db\Query())
    ->from('user')
    ->indexBy(function ($row) {
        return $row['id'] . $row['username'];
    })->all();
// 该匿名函数将带有一个包含了当前行的数据的 $row 参数，并且返回用作当前行索引的 标量值（译者注：就是简单的数值或者字符串，而不是其他复杂结构，例如数组）。
~~~

#### batch()/each()
~~~
// 当需要处理大数据的时候，像 yii\db\Query::all() 这样的方法就不太合适了， 因为它们会把所有数据都读取到内存上。为了保持较低的内存需求， Yii 提供了一个 所谓的批处理查询的支持。批处理查询会利用数据游标 将数据以批为单位取出来
// 你可以通过给 batch() 或者 each() 方法的第一个参数传值来改变每批行数的大小。
use yii\db\Query;

$query = (new Query())
    ->from('user')
    ->orderBy('id');

foreach ($query->batch() as $users) {
    // $users 是一个包含100条或小于100条用户表数据的数组
}

// or if you want to iterate the row one by one
foreach ($query->each() as $user) {
    // $user 指代的是用户表当中的其中一行数据
}
~~~