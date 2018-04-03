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

