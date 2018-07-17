## Model中的方法

#### 根据ID查找一个Model
	<!-- backend\models\Menu -->
	$model = Menu::findOne($id)

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

