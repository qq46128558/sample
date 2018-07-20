## 数据表查询
	use \yii\db\Query;
	$query = new Query;


#### 条件查询指定值
	$menutitle=$query->select('title')->from('{{%menu}}')->where(['!=','pid',0])->andWhere(['url'=>'menu/index'])->limit(1)->one()['title'];
	Yii::$app->view->params['menutitle']=$menutitle;

#### 防注入查询 addParams()
~~~
$query->where('status=:status')
    ->addParams([':status' => $status]);
~~~

#### 打印SQL createCommand()
~~~
$command = $query->select(['id', 'email'])
    ->from('{{%user}}')
    ->where(['last_name' => 'Smith'])
    ->limit(10)
    ->createCommand();
// 打印 SQL 语句
echo $command->sql;
// 打印被绑定的参数
print_r($command->params);
~~~~
