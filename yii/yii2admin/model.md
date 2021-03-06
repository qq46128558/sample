## Model中的方法
	$model=XXX::find()
	$result=static::find()->select('id')->where(['regexp','url','^'.$rule.'\\?'])->limit(1)->one();
	
#### like语句查询数据
	$result=$model->where(['like','title','xxx'])->orderBy('sort asc')->all();

#### or语句+and语句
	$query=$model->select(['name','title','value'])
        ->filterWhere(['name'=>$config])
        ->orFilterWhere(['title'=>$config])
        ->andWhere(['status'=>1])
        ->orderBy(['sort'=>SORT_ASC,'update_time'=>SORT_DESC]);
	// (name='xxx' or title='xxx') and (status=1)

#### \yii\db\Query支持防sql注入
	->where(['name'=>$name])
	// 或
	->where('name=:name')
	->addParams([':name'=>$name])

#### 根据ID查找一个Model
	<!-- backend\models\Menu -->
	$model = Menu::findOne($id)
	<!-- 验证findOne()使用limit(1)报错 -->

#### 加载数据库设置的默认值到model
	<!-- vendor/yiisoft/yii2/db/ActiveRecord.php -->
	$model->loadDefaultValues();


#### 修改model中record的字段值
	$model->pid = $pid;


#### 根据ID查找一行记录
	$result=Menu::findOne(123);
	// 或
	$result=$this::findOne(123);
	if ($result)
		return $result->title
	// 指定属性(若id不存在,则报错)
	$value=$this::findOne(123)->getAttribute('title');

#### 添加非表字段属性
~~~php
// 在model中增加方法
public function getPidname(){
    $name=Menu::findOne($this->pid);
    if ($name && $this->pid!=0)
        return $name->title;
    else
        return Yii::t('backend','一級菜單');
}
// 则可以通过$model->pidname取得值,也可以应用于view页面
// 也可以通过$model->getPidname()获取


// 使用另一个字符串填充字符串为指定长度
echo str_pad($input, 10, " ", STR_PAD_LEFT);

// 交换数组中的键和值
$exclude=array_flip(array('create_time','update_time'));
~~~


#### 操作过程出现错误的相关方法(一般如保存操作后)
~~~
// $model是否有错误产生
$model->hasErrors();

// 获取$model的错误信息
$attributes=$model->getErrors();
// array ('name' => array (0 => '編碼 的值 "1" 已經被佔用了。',),)
~~~


#### 获取模型的字段数组
	$fields=$model->attributeLabels();
	// 可以通过字段名称获取Label名称
	$fields['title']